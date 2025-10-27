x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

point1 = (x1, y1)
point2 = (x2, y2)

slope = (point1[1] - point2[1]) / (point1[0] - point2[0])
b = point1[1] - slope * point1[0]

print("y-int is", b)