from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    employees = get_employees()
    for employee in employees:
        print(calculate_salary(employee))
