
# Ask for total time
PAY_PERIOD = 40 # hours

###
# Add a new contract
###
contracts = {}
# Ask for contract ID
contract_id = int(input("Enter new contract number:\n>>> "))
# Ask for contract name
contract_name = input("Enter contract name:\n>>> ")
# Ask for contract time percentage/allocation
expected_time = float(input(f"Enter time to spend on {contract_id}:\n>>> "))
contract = (contract_id, contract_name, expected_time)
contracts[contract_id] = contract

###
# Log time spent on contract
###
# Ask for contract ID
worked_id = int(input("What is the contract number?\n>>> "))

# Ask for time spent
worked_time = float(input(f"How much time did you spend on {worked_id}?\n>>> "))

# Ask for goal
goal = input("What did you want to accomplish?\n>>> ")

# Ask for action
action = input("What steps did you take to meet your goal?\n>>> ")

# Emit report
worked_contract = contracts[worked_id]
worked_id, worked_name, expected_time = worked_contract
print("# Weekly Report")
print(f"## '{worked_id} - {worked_name}' (worked_time hours)")
print(f"* {goal}")
print(f"    + {action}")

# Save to file when done
