from datetime import date
import calendar


def main():
#    print(schedule_for_an_even_week)
    weekday()
    print_menu_options()

# def option2():
#    print('Handle option \'Option 2\'')



# def option3():
#    print('Handle option \'Option 3\'')

    option = int(input('Enter your choice: '))
# Check what choice was entered and act accordingly
    if option == 1:
       university()
#    elif option == 2:
#        option2()
#    elif option == 3:
#        option3()
    elif option == 4:
        print('See you soon')
        exit()
#    else:
#        print('Invalid option. Please enter a number between 1 and 4.')

menu_options = {
    1: 'University',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

menu_options_university = {
    1: 'Четная неделя сегодня',
    2: 'Четная неделя завтра',
    3: 'Нечетная неделя сегодня',
    4: 'Нечетная неделя завтра',
    5: 'Назад',
}

schedule_for_an_even_week1 = {  # Четная неделя сегодня
    "Monday": "Архитектура вычислительных систем Х2(Лекция)(c-20) - Нужно выйти в 16:40",
    "Tuesday": "Деловые коммуникации(1 лекция, 1 практика)(c-20) - Нужно выйти в 16:40",
    "Wednesday": "Интелектуальные системы и технологии Х2(Лекция)(с-20) - Нужно выйти в 16:40",
    "Thursday": "Логика и методология науки Х2(Практика)(в-86) - Нужно выйти в ",
    "Friday": "WOW, u can chill!",
    "Saturday": "Программная инженерия Х2(Лекция+практика)(В-78) - нужно выйти в 9:00",
    "Sunday": "WOW, u can chill!"
}

schedule_for_an_even_week2 = {  # Четная неделя завтра
    "Monday": "Деловые коммуникации(1 лекция, 1 практика)(c-20) - Нужно выйти в 16:40",
    "Tuesday": "Интелектуальные системы и технологии Х2(Лекция)(с-20) - Нужно выйти в 16:40",
    "Wednesday": "Логика и методология науки Х2(Практика)(в-86) - Нужно выйти в",
    "Thursday": "WOW, u can chill!",
    "Friday": "Программная инженерия Х2(Лекция+практика)(В-78) - нужно выйти в 9:00",
    "Saturday": "WOW, u can chill!",
    "Sunday": "Архитектура вычислительных систем Х2(Лекция)(c-20) - Нужно выйти в 16:40"
}

odd_week_schedule = {  # Нечетная неделя сегодня
    "Monday": "Социология и педагогика высшей школы, логика и метадология науки(лекции)(МП-1)",
    "Tuesday": "Модели информационных процессов и систем X2(практика)(с-20)",
    "Wednesday": "Интелектуальные системы и технологии Х2(практика)(с-20)",
    "Thursday": "Модели информационных процессов и систем(лекция)(с-20)",
    "Friday": "WOW, u can chill!",
    "Saturday": "Информационная безопасность интелектуальных систем(1 практика + 2 лекции)(В-78) ",
    "Sunday": "WOW, u can chill!"
}

odd_week_schedule = {  # Нечетная неделя завтра
    "Monday": "Модели информационных процессов и систем X2(практика)(с-20)",
    "Tuesday": "Интелектуальные системы и технологии Х2(практика)(с-20)",
    "Wednesday": "Модели информационных процессов и систем(лекция)(с-20)",
    "Thursday": "WOW, u can chill!",
    "Friday": "Информационная безопасность интелектуальных систем(1 практика + 2 лекции)(В-78)",
    "Saturday": "WOW, u can chill!",
    "Sunday": "Социология и педагогика высшей школы, логика и метадология науки(лекции)(МП-1)"
}

##############################################################################################

def salutation():
    print(
        "Привет!\nМеня зовут ХХХ, я буду твоим личным помошником. Я владею магией времени.\nЯ смогу помочь наладить твои дела, найти свободное время и никуда не опоздать!")


def weekday():
    global y
    x = date.today()
    y = calendar.day_name[x.weekday()]


def print_menu_options():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def print_menu_options_university():
    for key in menu_options_university.keys():
        print(key, '--', menu_options_university[key])


####################################################################
def option_university_1():  # Четная неделя сегодня
#    print(schedule_for_an_even_week)
#   print(y)
    x = schedule_for_an_even_week1.get(y)
    print(x)


def option_university_2():  # Четная неделя завтра
#    print(schedule_for_an_even_week)
#    print(y)
    x = schedule_for_an_even_week2.get(y)
    print(x)

def option_university_3():  # Нечетная неделя сегодня
#    print(odd_week_schedule)
#   print(y)
    x = odd_week_schedule.get(y)
    print(x)

def option_university_4():  # Нечетная неделя завтра
#    print(schedule_for_an_even_week)
#   print(y)
    x = odd_week_schedule.get(y)
    print(x)
####################################################################

def university():
    print(
        '\nСейчас я проверю твое расписание и скажу, когда тебе нужно будет выйти.\nТолько скажи, сегодня или завтра?')
    print_menu_options_university()
    option1 = int(input('Enter your choice: '))
    if option1 == 1:
        option_university_1()
        main()
    elif option1 == 2:
        option_university_2()
        main()
    elif option1 == 3:
        option_university_3()
        main()
    elif option1 == 4:
        option_university_4()
        main()
    elif option1 == 5:
        main()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')
        university()
#    while True:
#        flag = input('Ещё раз? [да/нет]: ')
#
#        if flag == 'да':
#            university()
#        else:
#            break





main()

