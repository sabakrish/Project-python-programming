# CREATE CALENDAR FOR A GIVEN MONTH AND YEAR
# display the day, month and year in the calendar and say what day of the week it is

import calendar


def create_calendar(year, month):
    """Return a text calendar for the given month/year, weeks starting on Monday."""
    cal = calendar.TextCalendar(calendar.MONDAY)
    return cal.formatmonth(year, month)


def get_day_name(year, month, day):
    """Return the weekday name for a specific date, or None if the date is invalid."""
    try:
        return calendar.day_name[calendar.weekday(year, month, day)]
    except ValueError:
        return None


if __name__ == "__main__":
    try:
        year = int(input("Enter year (e.g., 2024): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))

        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")

        month_calendar = create_calendar(year, month)
        print("Here is the month containing your birthday or any special day:")
        print(month_calendar)

        day_name = get_day_name(year, month, day)
        if day_name is None:
            print(f"{day} is not a valid day for month {month}.")
        else:
            print("Your special day falls on:", day_name)

    except ValueError as e:
        print(f"Invalid input: {e}")
