class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap_year(year: int) -> bool:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def get_days(date: str) -> int:
            y, m, d = map(int, date.split('-'))

            days = d + int(is_leap_year(y) and m > 2)
            days += sum(365 + int(is_leap_year(y)) for y in range(1971, y))
            days += sum([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m])

            return days

        return abs(get_days(date1) - get_days(date2))

        


        # final solution 
        # This code parses each date, converts it to a total days count since January 1, 1971.

        # It does so by summing days from years, months, and the current month's day, adjusting for leap years.

        # The result is the number of days between the two dates, as an absolute value.