from swagger_marshmallow_codegen.codegen.context import OutputData
from swagger_marshmallow_codegen.driver import Driver
from swagger_marshmallow_codegen.codegen import Codegen, ConfigDict
import typing as t
from prestring.output import output as create_separated_output
from swagger_marshmallow_codegen.langhelpers import normalize
from marshmallow import Schema, EXCLUDE

# class ConfigDict(tx.TypedDict, total=False):
#     emit_schema: bool  # emit definitions schemas
#     emit_input: bool  # emit input schema
#     emit_output: bool  # emit output schema

#     separated_output: bool  # activate separated output

#     explicit: bool  # emit Meta.unknown=RAISE, explicitly
#     additional_properties_default: bool  # if true meta.unknown=INCLUDE

#     emit_schema_even_primitive_type: bool  # emit not used toplevel definitions
#     header_comment: str  # header comment


class MyDriver(Driver):
    def __init__(self, *args, **kwargs):
        config = {
            "emit_schema_even_primitive_type": True,
            "header_comment": False,
            "emit_output": True,
            "emit_schema": True,
            "emit_input": True,
            "separeted_output": True,
            "explicit": False,
            "additional_properties_default": False,
        }
        super().__init__(config)
