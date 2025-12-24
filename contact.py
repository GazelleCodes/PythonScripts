# Getting email information of students from a dictionary
contacts = {
    'number':4,
    'students':
        [
            {'name':'Alice Smith', 'email':'alice@example.com'},
            {'name':'Bob Johnson', 'email':'bob@example.com'},
            {'name':'Charlie Lee', 'email':'charlie@example.com'},
            {'name':'Diana King', 'email':'diana@example.com'}
        ]
}

print('students email addresses:')
for student in contacts['students']:
    print(student['email'])
    # print(student['name'])
