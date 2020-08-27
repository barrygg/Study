from datetime import date, timedelta


# Working days counter
def working_days_1(start_date, end_date):
    days = (start_date + timedelta(x) for x in range((end_date - start_date).days + 1))
    working_days = 0
    for day in days:
        if day.weekday() < 5:
            working_days += 1
    return(working_days)


def working_days_2(start_date, end_date):
    working_days = (((end_date - start_date).days) // 7) * 5
    i = start_date.isoweekday()
    while i != end_date.isoweekday():
        if i < 6:
            working_days +=1
            i +=1
        elif i == 6:
            i +=1
        else:
            i = 1
    return(working_days)

date_entry = input('Enter the start date in YYYY-MM-DD format:')
year, month, day = map(int, date_entry.split('-'))
start_date = date(year, month, day)
date_entry = input('Enter the end date in YYYY-MM-DD format:')
year, month, day = map(int, date_entry.split('-'))
end_date = date(year, month, day)

print(working_days_1(start_date, end_date))
print(working_days_2(start_date, end_date))
