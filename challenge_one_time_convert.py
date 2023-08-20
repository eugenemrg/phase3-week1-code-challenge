def convert_time(hour, minutes, period):
    if period == 'am' and hour == 12:
        time = '00'
    elif period == 'am':
        time = f'{hour}' if hour > 10 else f'0{hour}'
    elif period == 'pm':
        time = '12' if hour == 12 else f'{hour + 12}'
 
    time = f'{time}{minutes}' if minutes > 10 else f'{time}0{minutes}'
    return time