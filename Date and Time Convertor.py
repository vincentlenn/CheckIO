from datetime import datetime

def date_time(time):
    """
    Convert the input date and time from computer format into a 'human' format.
    """
    t = datetime.strptime(time, '%d.%m.%Y %H:%M')
    date = f"{t.day} {t.strftime('%B %Y year')}"
    hour = f"{t.hour} hour{'s'[:t.hour != 1]}"
    minute = f"{t.minute} minute{'s' * (t.minute != 1)}"
    return f"{date} {hour} {minute}"

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
