
# Ask for total time
PAY_PERIOD = 40 # hours

contracts = {}

###
# Add a new contract
###
def add_contract():
    # Ask for contract ID
    contract_id = int(input("Enter new contract number:\n>>> "))
    # Ask for contract name
    contract_name = input("Enter contract name:\n>>> ")
    # Ask for contract time percentage/allocation
    expected_time = float(input(f"Enter time to spend on {contract_id}:\n>>> "))
    contract = (contract_id, contract_name, expected_time)
    contracts[contract_id] = contract


exit = False

while not exit:
    print('1. Add new contract\n2. Log time\n3. View Report\n4. Exit')
    option = int(input(">>> "))

    if option == 1:
        add_contract()
    elif option == 2:
        # Ask for contract ID
        worked_id = int(input("What is the contract number?\n>>> "))
        # Ask for time spent
        worked_time = float(input(f"How much time did you spend on {worked_id}?\n>>> "))

        # Ask for goal
        goal = input("What did you want to accomplish?\n>>> ")

        # Ask for action
        action = input("What steps did you take to meet your goal?\n>>> ")
    elif option == 3:
        # Emit report
        worked_contract = contracts[worked_id]
        worked_id, worked_name, expected_time = worked_contract
        print("# Weekly Report")
        print(f"## '{worked_id} - {worked_name}' (worked_time hours)")
        print(f"* {goal}")
        print(f"    + {action}")
    elif option == 4:
        exit = True

# Save to file when done
