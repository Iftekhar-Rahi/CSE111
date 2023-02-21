#Task 8
def counter(day):
    year=day//365
    year_remaining=day%365
    month=year_remaining//30
    days=year_remaining%30
    print(f"{year} years, {month} months and {days} days")
counter(4320)