from pydantic import BaseModel

from .user import User


class AppConfig(BaseModel):
    """Application Configuration"""

    user: list[User]


def get_app_config_json_schema() -> str:
    return AppConfig.schema_json(indent=2)
