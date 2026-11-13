from datetime import date

eventt = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day:"))

event_date = date(year, month, day)

print("\n Formatted Output")
print("Event:", eventt.upper())
print("Date:", f"{event_date.strftime('%B')} {event_date.day}, {event_date.year}")
print("Year:", event_date.year)
print("Month:", event_date.strftime("%B"))
print("Day:", event_date.day)
print("Weekday", event_date.strftime("%A"))
