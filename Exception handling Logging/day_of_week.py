def day_of_week(day):
    week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    try:
        num = int(day)
        if num < 1 or num > 7:
            return 'There is no such day of the week! Please try again.'
        return f'{week[num]}'
    except ValueError:
        return "You did not enter a number! Please try again."


print(day_of_week(2)) #Tuesday
print(day_of_week(11)) #There is no such day of the week! Please try again.
print(day_of_week("Monday")) #You did not enter a number! Please try again.
