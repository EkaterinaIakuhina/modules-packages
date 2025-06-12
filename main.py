from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary
import art 

today = datetime.date(datetime.today())

def ascii_art():
    '''
    return 1-line art, if there is no such art then return ASCII text
    '''
    text = input()
    try:
        ascii_art = art.art(text)
        print(ascii_art)
    except art.errors.artError as e:
        print(art.text2art(text))

if __name__ == '__main__':
    print(today)
    get_employees()
    calculate_salary()

    ascii_art()