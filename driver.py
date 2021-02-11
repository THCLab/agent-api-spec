from swagger_marshmallow_codegen.driver import Driver


class MyDriver(Driver):
    codegen_factory = Driver.codegen.override(schema_class_path="foo.bar.schema:MySchema"))
