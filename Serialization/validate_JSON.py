import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import csv

class DepartmentName(Exception):
    pass

class InvalidInstanceError(Exception):
    pass

student_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "department_id": {"type": "integer"}
        },
    "required": ["name", "department_id"],
    "additionalProperties": False
    }
}

department_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
    "required": ["id", "name"],
    "additionalProperties": False
    }
}


def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError:
        return False


def user_with_department(csv_file, user_json, department_json):
    with open(user_json, "r") as f:
        students_data = json.load(f)
    with open(department_json, "r") as f:
        departments_data = json.load(f)

    if not validate_json(students_data, student_schema):
        raise InvalidInstanceError

    if not validate_json(departments_data, department_schema):
        raise InvalidInstanceError

    departments_dict = {}
    for d in departments_data:
        departments_dict[d["id"]] = d["name"]
    rows = []
    for student in students_data:
        if student["department_id"] not in departments_dict:
            raise DepartmentName(f"{student["department_id"]} not found")
        rows.append([student["name"], departments_dict[student["department_id"]]])

    with open(csv_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "department"])
        writer.writerows(rows)



