grades = {
    "Alice":[20,68,90,100,65],
    "bob":[100,96,91,98,100],
    "Mark":[98,89,76,45,90],
    "jason":[90,98,89,88,83]
}
print(grades)

def Calc_Avg(grades):
    total = sum(grades)
    count = len(grades)
    return total/count

def catg(avg):
    
    if avg > 90:
        return "Honor Roll"
    elif avg > 80 and avg < 90:
        return "Good"
    else:
        return "Average"
'''
def report(data):  
    for student,marks in data.items():
        average = Calc_Avg(marks)
        status = catg(average)
        
        print(f"{student} holded {status} for average of {average} \n")

report(grades)
'''

for student,marks in grades.items():
    for mark in marks:
        print(f"{student} scored {mark}")    