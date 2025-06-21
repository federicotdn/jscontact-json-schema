import json
import sys
from jsonschema import Draft202012Validator, validate


if __name__ == "__main__":
    with open("jscontact-schema.json") as f:
        schema = json.load(f)
        if len(sys.argv) >= 2 and sys.argv[1] == "--self":
            Draft202012Validator.check_schema(schema)
        else:
            instance = json.load(sys.stdin)
            validate(instance, schema)
