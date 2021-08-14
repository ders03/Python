"""Find the next friday the 13th.

Write a function named friday_the_13th, which takes no parameter, and just returns the date of the next friday the 13th.

If today is a friday the 13th, return it, not the next one.

Return the date as a string of the following format: YYYY-MM-DD."""

import datetime
import pandas

def friday_the_13th():
    today = datetime.datetime.today()
    today1 = today.strftime("%Y-%m-%d-%a")
    want_date = datetime.strptime(want, "%Y-%m-%d-%a")

friday_the_13th()


    
