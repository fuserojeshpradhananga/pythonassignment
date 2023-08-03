def create_student_report(name, age, **kwargs):
    student_info = {
        'name': name,
        'age': age,
    }
    subjects = []
    for subject, score in kwargs.items():
        subjects.append({
            'subject': subject,
            'score': score
        })

    student_info['subjects'] = subjects
    return student_info

# Test case 1
print(create_student_report("John Doe", 20)) 
