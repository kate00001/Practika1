grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #список с изменяемыми объектами
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # множество
names = list(students)
names.sort()
print(names)
average_grade = {names[0] : sum(grades[0])/len(grades[0]),
                 names[1] : sum(grades[1])/len(grades[1]),
                 names[2] : sum(grades[2])/len(grades[2]),
                 names[3] : sum(grades[3])/len(grades[3]),
                 names[4] : sum(grades[4])/len(grades[4])}
print(average_grade)






# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}