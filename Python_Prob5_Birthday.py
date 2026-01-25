# CREATE CALANDAR FOR A GIVEN MONTH AND YEAR
# display the day , month and year in the calender and say what is the day

import calendar
def create_calendar(year, month, day_of_month):
    # Create a TextCalendar instance
    #cal = calendar.TextCalendar()
    cal= calendar.TextCalendar(calendar.MONDAY)
    # Generate the calendar for the specified month and year
    month_calendar = cal.formatmonth(year, month, day_of_month)
                                          
    return month_calendar
if __name__ == "__main__":
    year = int(input("Enter year (e.g., 2024): "))
    month = int(input("Enter month (1-12): "))
    day=int(input("Enter day (1-31): "))
    month_calendar = create_calendar(year, month, day)
   
    print("Look your the month and the day you were born or any auspicious day:")
    print(month_calendar)
           
    day_name = calendar.day_name[calendar.weekday(year, month, day)]
    print("Your auspicious day is:", day_name)
