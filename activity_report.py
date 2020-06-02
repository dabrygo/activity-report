import csv
import datetime
import os.path

DATA_FILE = "activity_report.dat"

def load_data(file_=DATA_FILE):
    if os.path.exists(file_):
        with open(file_) as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    return []

option = int(input("What do you want to do?\n  1. Add entry\n  2. Make report\n>>> "))
if option == 1:
    date = datetime.datetime.now()
    contract = input("Contract #: ")
    time_spent = input("Time spent (hr): ")

    records = load_data()
    contracts = set(r['contract'] for r in records)
    print(contracts)
    if contract in contracts:
        goals = set(r['goal'] for r in records if r['contract'] == contract)
        print("Contract currently has these goals:")
        for goal in goals:
            print(f"  * {goal}")
    goal = input("What goal? ")

    action = input("What action? ")
    print(f"You spent {time_spent} hrs on '{contract}' doing '{action}' in order to achieve '{goal}'")

    file_exists = os.path.exists(DATA_FILE)
    if not file_exists:
        record_id = 0
    else:
        record_id = max(int(r['id']) for r in records) + 1
    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            header = ['id', 'date', 'contract', 'time_spent', 'goal', 'action']
            writer.writerow(header)
        date_id = date.strftime("%Y%m%d")
        writer.writerow([record_id, date_id, contract, time_spent, goal, action])
elif option == 2:
    pass
else:
    print(f"I don't recognize option '{option}'")
