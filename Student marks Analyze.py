
marks = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks)
print("List:", marks)
print("Type of List:", type(marks))
print("Tuple:", marks_tuple)
print("Type of Tuple:", type(marks_tuple))
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))
count = marks.count(40)
count = (marks[0] >= 40) + (marks[1] >= 40) + (marks[2] >= 40) + (marks[3] >= 40) + (marks[4] >= 40)
print("Students scoring at least 40:", count)
valid = (
    marks[0] >= 0 and marks[0] <= 100 and
    marks[1] >= 0 and marks[1] <= 100 and
    marks[2] >= 0 and marks[2] <= 100 and
    marks[3] >= 0 and marks[3] <= 100 and
    marks[4] >= 0 and marks[4] <= 100
)
print("Are all marks valid?", valid)
marks[0] = 80
print("After changing list:", marks)
