#Create function find(file, key)
#This function parses json-file and returns all unique values of the key.
#1.json: [{"name": "user_1”, "password": "pass_1”}, {"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
#find("1.json", "password") returns ["pass_1", "qwerty"]
#2.json: [{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
#find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]

import json

def find(file, key):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
        result = []
        stack = [data]

        while stack:
            current = stack.pop()

            if isinstance(current, dict):
                for k, v in current.items():
                    if k == key:
                        if isinstance(v, list):
                            result.extend(v)
                        else:
                            result.append(v)
                    stack.append(v)
            elif isinstance(current, list):
                stack.extend(current)

        return list(set(result))

    except FileNotFoundError:
        return "File doesn't exist"
    except json.JSONDecodeError:
        return "Error format JSON"


