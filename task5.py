import datetime
import os


def log(old_function):
    def new_function(*args, **kwargs):
        date = datetime.datetime.today()
        log_string = f'{date} - {old_function.__name__} - {args}, {kwargs} - {old_function(*args, **kwargs)}\n'
        with open ('log_file.txt', 'a') as f:
            f.write(log_string)
        return old_function(*args, **kwargs)
    return new_function


def log_path(file_path):
    def log(old_function):
        def new_function(*args, **kwargs):
            date = datetime.datetime.today()
            log_string = f'{date} - {old_function.__name__} - {args}, {kwargs} - {old_function(*args, **kwargs)}\n'
            with open(file_path, 'a') as f:
                f.write(log_string)
            return old_function(*args, **kwargs)
        return new_function
    return log


@log_path(os.path.join(os.getcwd(),'log_file.txt'))
def get_zodiac(month_of_birth, day_of_birth):
    if month_of_birth == 12 and day_of_birth in range(23, 32) or month_of_birth == 1 and day_of_birth <= 20:
        zodiac = 'Козерог'
    elif month_of_birth == 1 and day_of_birth in range(21, 32) or month_of_birth == 2 and day_of_birth <= 19:
        zodiac = 'Водолей'
    elif month_of_birth == 2 and day_of_birth in range(20, 30) or month_of_birth == 3 and day_of_birth <= 20:
        zodiac = 'Рыбы'
    elif month_of_birth == 3 and day_of_birth in range(21, 32) or month_of_birth == 4 and day_of_birth <= 20:
        zodiac = 'Овен'
    elif month_of_birth == 4 and day_of_birth in range(21, 31) or month_of_birth == 5 and day_of_birth <= 21:
        zodiac = 'Телец'
    elif month_of_birth == 5 and day_of_birth in range(22, 32) or month_of_birth == 6 and day_of_birth <= 21:
        zodiac = 'Близнецы'
    elif month_of_birth == 6 and day_of_birth in range(22, 31) or month_of_birth == 7 and day_of_birth <= 22:
        zodiac = 'Рак'
    elif month_of_birth == 7 and day_of_birth in range(23, 32) or month_of_birth == 8 and day_of_birth <= 21:
        zodiac = 'Лев'
    elif month_of_birth == 8 and day_of_birth in range(23, 32) or month_of_birth == 9 and day_of_birth <= 23:
        zodiac = 'Дева'
    elif month_of_birth == 9 and day_of_birth in range(24, 31) or month_of_birth == 10 and day_of_birth <= 23:
        zodiac = 'Весы'
    elif month_of_birth == 10 and day_of_birth in range(24, 32) or month_of_birth == 11 and day_of_birth <= 22:
        zodiac = 'Скорпион'
    elif month_of_birth == 11 and day_of_birth in range(23, 31) or month_of_birth == 12 and day_of_birth <= 22:
        zodiac = 'Стрелец'
    return zodiac

get_zodiac(3, 22)
