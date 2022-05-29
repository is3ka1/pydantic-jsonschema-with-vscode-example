import pathlib
from pydantic_jsonschema_auto_completion.config import get_app_config_json_schema


def gen_json_schema():
    with open(pathlib.Path().absolute() / "schema.yaml", "w") as schema_file:
        schema_file.write(get_app_config_json_schema())


if __name__ == "__main__":
    gen_json_schema()
