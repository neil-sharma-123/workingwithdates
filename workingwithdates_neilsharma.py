import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month == 12:
        return 31
    else:
        day = datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)
        return int(day.days)

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if 1 <= month <= 12 and datetime.MINYEAR <= year <= datetime.MAXYEAR and 1 <= day <= days_in_month(year, month):
        return True
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """

    if not(is_valid_date(year1, month1, day1)):
        return 0
    elif not(is_valid_date(year2, month2, day2)):
        return 0

    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    if date1 > date2:
        return 0
    else:
        diff = date2 - date1
        return diff.days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if not(is_valid_date(year, month, day)):
        return 0
    if datetime.date.today() < datetime.date(year, month, day):
        return 0
    else:
        age = datetime.date.today() - datetime.date(year, month, day)
        return age.days
