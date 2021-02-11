#!/usr/bin/env python3
"""
This script invokes swagger-marshmallow-codegen program on nearby swagger-spec.yaml.
Modifies the output a bit and pipes it into directory specified by the first argument to the program.
In the end it creates a "generated_models.py" file.
"""

import os
import subprocess
import sys

path_to_script = os.path.realpath(__file__)
path = os.path.split(path_to_script) 
path_to_spec = path[0] + "/swagger-spec.yaml"
completed = subprocess.run(["swagger-marshmallow-codegen", path_to_spec], capture_output=True)

# Format
generated_output = completed.stdout.decode("utf-8")
std_error = completed.stderr.decode('utf-8')
print(std_error)
print(generated_output)

index = generated_output.find("class")
generated_output = generated_output[index:]
generated_output = generated_output.replace("    class Meta:\n        unknown = INCLUDE", "")
generated_output = generated_output.replace("(Schema)", "(OpenAPISchema)")


generated_filename = "generated_models.py"
if len(sys.argv) > 1:
    generated_filename = sys.argv[1] + generated_filename    

f = open(generated_filename, "w")
f.write( \
"""\"\"\"This file is auto generated\"\"\"
from marshmallow import ( Schema, fields, EXCLUDE )
from marshmallow.validate import OneOf
from marshmallow import Schema, SchemaOpts, fields, ValidationError
from marshmallow import pre_load, pre_dump


class PrimitiveValueSchema:
    schema_class = None
    key = "value"
    missing_value = None

    def __init__(self, *args, **kwargs):
        self.schema = self.__class__.schema_class(*args, **kwargs)

    def _fix_exception(self, exc):  # xxx: side effect
        if hasattr(exc, "data") and self.key in exc.data:
            exc.data = exc.data[self.key]
        if (
            hasattr(exc, "messages")
            and hasattr(exc.messages, "keys")
            and self.key in exc.messages
        ):
            exc.messages = exc.messages[self.key]
            exc.args = tuple([exc.messages, *exc.args[1:]])
        if hasattr(exc, "valid_data") and self.key in exc.valid_data:
            exc.valid_data = exc.valid_data[self.key]
        return exc

    def load(self, value):  # don't support many
        try:
            r = self._do_load(value)
        except ValidationError as e:
            self._fix_exception(e)
            raise e.with_traceback(e.__traceback__)
        return r.get(self.key) or self.missing_value

    def _do_load(self, value):
        data = {self.key: value}
        return self.schema.load(data)

    def dump(self, value):  # don't support many
        try:
            r = self._do_dump(value)
        except ValidationError as e:
            self._fix_exception(e)
            raise e.with_traceback(e.__traceback__)
        return r.get(self.key) or self.missing_value

    def _do_dump(self, value):
        data = {self.key: value}
        return self.schema.dump(data)


class AdditionalPropertiesOpts(SchemaOpts):
    def __init__(self, meta, **kwargs):
        super().__init__(meta, **kwargs)
        self.additional_field = getattr(meta, "additional_field", fields.Field)


def make_additional_properties_schema_class(Schema):
    class AdditionalPropertiesSchema(Schema):
        \"\"\"
        support addtionalProperties
        class MySchema(AdditionalPropertiesSchema):
            class Meta:
                additional_field = fields.Integer()
        \"\"\"

        OPTIONS_CLASS = AdditionalPropertiesOpts

        @pre_load
        def wrap_load_dynamic_additionals(self, data, *, many=False, partial=False):
            diff = set(data.keys()).difference(self.load_fields.keys())
            for name in diff:
                f = self.opts.additional_field
                self.load_fields[name] = f() if callable(f) else f
            return data

        @pre_dump
        def wrap_dump_dynamic_additionals(self, data, *, many=False, partial=False):
            diff = set(data.keys()).difference(self.dump_fields.keys())
            for name in diff:
                f = self.opts.additional_field
                self.dump_fields[name] = f() if callable(f) else f
            return data

    return AdditionalPropertiesSchema


AdditionalPropertiesSchema = make_additional_properties_schema_class(Schema)

class OpenAPISchema(Schema):
    class Meta:
        unknown = EXCLUDE

    
""")
f.write(generated_output)

f.close()
