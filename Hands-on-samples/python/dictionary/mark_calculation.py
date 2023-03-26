def get_average(ls):
    return sum(ls)/len(ls)

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else: 
        return 'E'
    

jack = { "name":"Jack Frost",
        "assignment" : [80, 50, 40, 20],
        "test" : [75, 75],
        "lab" : [78.20, 77.20]
    }         

james = { "name":"James Potter",
        "assignment" : [82, 56, 44, 30],
        "test" : [80, 80],
        "lab" : [67.90, 78.72]
        } 

dylan = { "name" : "Dylan Rhodes",
        "assignment" : [77, 82, 23, 39],
        "test" : [78, 77],
        "lab" : [80, 80]
        }
         
jess = { "name" : "Jessica Stone",
        "assignment" : [67, 55, 77, 21],
        "test" : [40, 50],
        "lab" : [69, 44.56]
    }         

tom = { "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]
    }

students = [jack, james, dylan, jess, tom]

for student in students:
    assignment_average = get_average(student['assignment']) * 0.10
    test_average = get_average(student['test']) * 0.70
    lab_average = get_average(student['lab']) * 0.20
    total_avg = assignment_average + test_average + lab_average
    grade = get_grade(total_avg)
    print(f"{student.get('name')} secured grade {grade}")