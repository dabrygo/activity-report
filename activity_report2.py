import csv
import datetime

date = datetime.datetime.now()
contract = input("Contract #: ")
time_spent = input("Time spent (hr): ")
goal = input("What goal? ")
action = input("What action? ")

print(f"You spent {time_spent} hrs on '{contract}' doing '{action}' in order to achieve '{goal}'")

with open("activity_report.dat", 'w') as f:
    writer = csv.writer(f)
    header = ['date', 'contract', 'time_spent', 'goal', 'action']
    writer.writerow(header)
    date_id = date.strftime("%Y%m%d")
    writer.writerow([date_id, contract, time_spent, goal, action])
