import datetime

today = datetime.date.today

now = datetime.datetime.now()

now = now.strftime("%I:%M %p")

print(now)
