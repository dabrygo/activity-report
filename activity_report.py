from collections import defaultdict as ddict
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


prompt = '''\
What do you want to do?
  1. Add entry
  2. Make report
  3. Exit
>>> \
'''
while (option := int(input(prompt))) != 3:
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

        # Save data
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
        records = load_data()
        organized = ddict(list)
        for record in records:
            contract = record['contract']
            goal = record['goal']
            key = (contract, goal)

            date = record['date']
            time_spent = record['time_spent']
            action = record['action']
            value = (date, time_spent, action)
            organized[key].append(value)
        print(f'# Activity Report')
        previous_contract = None
        previous_goal = None
        for key, values in organized.items():
            contract, goal = key

            if contract != previous_contract:
                print(f'## {contract}')
            previous_contract = contract

            if goal != previous_goal:
                print(f"  * {goal}")
            previous_goal = goal

            for value in values:
                date, time_spent, action = value
                print(f"    - {action} ({time_spent} hrs)")
    else:
        print(f"I don't recognize option '{option}'")
