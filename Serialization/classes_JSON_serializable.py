import json
from pathlib import Path

#Class Student has attributes full_name:str, avg_rank: float, courses: list
#Class Group has attributes title: str, students: list. Make both classes JSON serializable.
#Json-files represent information about student (students).
#Create methods:
#Student.from_json(json_file) that return Student instance from attributes from json-file;
#Student.serialize_to_json(filename)
#Group.serialize_to_json(list_of_groups, filename)
#Group.create_group_from_file(students_file)
#Parse given files, create instances of Student class and create instances of Group class (title for group is name of json-file without extension).


class StudentsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Student, Group)):
            return obj.__dict__
        return super().default(obj)


class Student:
    def __init__(self, full_name: str, avg_rank: float,  courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __repr__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    def serialize_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self, f, cls=StudentsEncoder)

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                if len(data) > 0:
                    return cls(**data[0])
                else:
                    raise ValueError
            return cls(**data)


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    def __repr__(self):
        return f"{self.title}: {[str(s) for s in self.students]}"

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(list_of_groups, f, cls=StudentsEncoder)

    @classmethod
    def create_group_from_file(cls, students_file):
        group_title = Path(students_file).stem

        with open(students_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                students = []
                for s in data:
                    student_obj = Student(**s)
                    students.append(student_obj)
            else:
                student_obj = Student(**data)
                students = [student_obj]

            return cls(group_title, students)


