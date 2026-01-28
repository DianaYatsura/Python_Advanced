import re
"""
Please specify a regular expression for matching publication formats such as 
"Head First. Python: PROSystem, 2021" and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022" 
to ('Head First. Python', 'PROSystem', '2021')
('Coding for Kids Python & Blockchain Programming', 'Elliot Davis', '2022')
"""
def pretty_message(data):
    pattern = r'"([^"]+):\s*([^,]+),\s*(\d{4})"'
    matches = re.findall(pattern, data)
    return matches

data = '"Head First. Python: PROSystem, 2021"# and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022"'
print(pretty_message(data)) #[('Head First. Python', 'PROSystem', '2021'), ('Coding for Kids Python & Blockchain Programming', 'Elliot Davis', '2022')]

data = '"Artificial Intelligence: A Modern Approach: Stuart Russell, 2003"'
print(pretty_message(data)) #[('Artificial Intelligence: A Modern Approach', 'Stuart Russell', '2003')]