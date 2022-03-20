#  to display date and time
print("------simple program to display current date and time------")

import datetime

current_time = datetime.datetime.now()
print(f"current time is :- {current_time}")
print(f"current year is :- {current_time.year}")
print(current_time.strftime("%A"))
