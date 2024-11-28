import random
import datetime

def random_date(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

start_date = datetime.date(1950, 1, 1)
end_date = datetime.date(2000, 1, 1)
hire_start_date = datetime.date(2000, 1, 1)
hire_end_date = datetime.date(2020, 1, 1)

employees = []
departments = []
dept_manager = []
dept_emp = []
titles = []
salaries = []

# Generate 100 employees
for i in range(100):
    emp_no = 10000 + i
    birth_date = random_date(start_date, end_date)
    first_name = f'FirstName{i}'
    last_name = f'LastName{i}'
    gender = random.choice(['M', 'F'])
    hire_date = random_date(hire_start_date, hire_end_date)
    employees.append((emp_no, birth_date, first_name, last_name, gender, hire_date))

# Generate departments
for i in range(10):
    dept_no = f'd{i:03}'
    dept_name = f'Department{i}'
    departments.append((dept_no, dept_name))

# Generate dept_manager, dept_emp, titles, and salaries
for i in range(100):
    emp_no = 10000 + i
    dept_no = departments[i % 10][0]
    from_date = random_date(hire_start_date, hire_end_date)
    to_date = random_date(from_date, hire_end_date)
    
    dept_manager.append((emp_no, dept_no, from_date, to_date))
    dept_emp.append((emp_no, dept_no, from_date, to_date))
    
    title = f'Title{i}'
    titles.append((emp_no, title, from_date, to_date))
    
    salary = random.randint(30000, 100000)
    salaries.append((emp_no, salary, from_date, to_date))

# Print SQL insert statements
print("-- Insert employees")
for emp in employees:
    print(f"INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES ({emp[0]}, '{emp[1]}', '{emp[2]}', '{emp[3]}', '{emp[4]}', '{emp[5]}');")

print("-- Insert departments")
for dept in departments:
    print(f"INSERT INTO departments (dept_no, dept_name) VALUES ('{dept[0]}', '{dept[1]}');")

print("-- Insert dept_manager")
for dm in dept_manager:
    print(f"INSERT INTO dept_manager (emp_no, dept_no, from_date, to_date) VALUES ({dm[0]}, '{dm[1]}', '{dm[2]}', '{dm[3]}');")

print("-- Insert dept_emp")
for de in dept_emp:
    print(f"INSERT INTO dept_emp (emp_no, dept_no, from_date, to_date) VALUES ({de[0]}, '{de[1]}', '{de[2]}', '{de[3]}');")

print("-- Insert titles")
for title in titles:
    print(f"INSERT INTO titles (emp_no, title, from_date, to_date) VALUES ({title[0]}, '{title[1]}', '{title[2]}', '{title[3]}');")

print("-- Insert salaries")
for salary in salaries:
    print(f"INSERT INTO salaries (emp_no, salary, from_date, to_date) VALUES ({salary[0]}, {salary[1]}, '{salary[2]}', '{salary[3]}');")
