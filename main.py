import datetime



def leap_year(y):
  if y % 400 == 0:
    return True
  if y % 100 == 0:
    return False
  if y % 4 == 0:
    return True
  else:
    return False

def days_in_month(year, month):
  """
  Inputs:
    year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
            representing the year
    month - an integer between 1 and 12 representing the month
    
  Returns:
    The number of days in the input month.
  """
  leap = 0
  if year% 400 == 0:
    leap = 1
  elif year % 100 == 0:
    leap = 0
  elif year % 4 == 0:
    leap = 1
  if month==2:
    return 28 + leap
  list = [1,3,5,7,8,10,12]
  if month in list:
    return 31
  return 30

days = days_in_month(1995, 4)

print(days)

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
  month_range = list(range(1,13))
  date_range = list(range(1,32))
  if year <= datetime.MAXYEAR and year >= datetime.MINYEAR:
    if month in month_range and day in date_range:
      
      if month==2:
        if leap_year(year):
          if day>=29:
            return False
        else:
          if not leap_year(year):
            if day>=28:
              return False
      return True

    else:
      return False
  else:
    return False

  return False
    
validity = is_valid_date(2017, 2, 29)
print(validity)

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
  if is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2):
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    
    if date1<=date2:
      diff = (date2 - date1).days
      return diff
    else:
      return 0
  return 0



differ = days_between(2014, 5, 5, 2014, 5, 6)
print(differ)

def age_in_days(year, month, day):
  """
  Inputs:
    year  - an integer representing the birthday year
    month - an integer representing the birthday month
    day   - an integer representing the birthday day
    
  Returns:
    The age of a person with the input birthday as of today.
    Returns 0 if the input date is invalid of if the input
    date is in the future.
  """
  date_today = datetime.date.today()

  if is_valid_date(year,month,day):
    bd_date = datetime.date(year,month,day)

    
    
    if bd_date<=date_today:
      age = (date_today - bd_date).days
      return age
  return 0

birthday = age_in_days(2017, 1, 1)
print(birthday)
