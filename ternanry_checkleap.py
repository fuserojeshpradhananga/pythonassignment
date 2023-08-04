def check_leap_year(year):
    leap_year = "Leap Year" 
      if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
      else "Not a Leap Year"
    return leap_year

#Test1
print(check_leap_year(2024))

#Twat2

print(check_leap_year(2020))
