import re
"""
The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"
 LB - Left Bottom point
 LT - Left Top point
 RT - Right Top point
 RB - Right Bottom point
numbers after letters are the coordinates of a point.
Write a function figure_perimetr() that calculates the perimeter of a quadrilateral
"""
def figure_perimetr(str):
    pattern = r"#([LBTR]+)(\d+):(\d+)"
    matches = re.findall(pattern, str)
    points = {name: (int(x), int(y)) for name, x, y in matches}
    directions = {
                'LB': ('LT', 'RB'),
                'RT': ('RB', 'LT'),
                 }
    perimetr = []
    for start_node,neighbors in directions.items():
        for neighbor in neighbors:
            p1 = points[start_node]
            p2 = points[neighbor]
            dist = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
            perimetr.append(dist)
    return sum(perimetr)

print(figure_perimetr("#LB1:1#RB4:1#LT1:3#RT4:3")) #10.0




