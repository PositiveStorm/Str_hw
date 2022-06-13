from application.salary import calculate_salary
from db.people import get_employees
from datetime import date

def current_date():
    current_date = date.today()
    print(f'Today is: {current_date}')

def main():
    command = input('Command c/e?: ')

    if command == 'c':
        calculate_salary()
        current_date()
    elif command == 'e':
        get_employees()
        current_date()

if __name__ == '__main__':

    main()