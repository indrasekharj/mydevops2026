# first_name = 'John'
# last_name = 'Doe'
# full_name = first_name + ' ' + last_name
# address = '123 Main Street'
# address += ', Apartment 4B'
# employee_age = 28
# employee_info = full_name + ' is ' + str(employee_age) + ' years old'
# print(employee_info)
# experience_years = 5
# experience_info = 'Experience: ' + str(experience_years) + ' years'
# print(experience_info)
# position = 'Data Analyst'
# salary = 75000
# employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
# print(employee_card)
# employee_code = 'DEV-2026-JD-001'
# department = employee_code[0:3]
# print(department)
# year_code = employee_code[4:8]
# print(year_code)
# initials = employee_code[9:11]
# print(initials)
# last_three = employee_code[-3:]
# print(last_three)

from sys import prefix


item_name = 'Router'
price = 500
total = 'price of 3 ' + item_name + 's is ' + str(price * 3)
print(total)
prefix = 'Cisco_'
suffix = 'Device'
device_id = prefix + suffix
print(device_id)

data_centers = ["San Jose", "London", "Tokyo", "Berlin"]
print(data_centers[1])
print(data_centers[-1])

running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays  = round(final_bill,2)
print ('Each person pays:', each_pays)

