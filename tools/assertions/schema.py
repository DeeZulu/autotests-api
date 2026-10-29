from typing import Any, Dict
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: Dict):
    """
    Валидирует объект instance согласно JSON схеме schema
    :param instance: проверяемый объект
    :param schema: JSON схема
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )
