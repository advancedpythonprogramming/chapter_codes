# 4.py

name = 'John Smith'
grade = 4.5
if grade >= 5.0:
    result = 'passed'
else:
    result = 'failed'

template = "Hi {0}, you have {1} the exam. Your grade was {2}"
print(template.format(name, result, grade))
