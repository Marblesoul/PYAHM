import pyjokes
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    employees = get_employees()
    for employee in employees:
        print(calculate_salary(employee))

    print(datetime.now().date().strftime('%d-%m-%Y'))
    print(pyjokes.get_joke())
