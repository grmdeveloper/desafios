action_values = []
days = 0
buy_day = -1
best_profit = 0

days = input('Insert number of days: ')
while not days.isnumeric():
    days = input('Please, insert a valid number: ')
days = int(days)

for counter in range(days):
    value = input('Value in day {}: '.format( len(action_values)+1 ))
    while not value.isnumeric():
        value = input('Please insert a valid number to day {}: '.format(len(action_values) + 1))
    action_values.append(int(value))

while buy_day >= days or buy_day < 0:
    buy_day = input('On which day the store was purchased? ')
    buy_day = int(buy_day)-1

for c in range(buy_day+1, len(action_values)):
    profit = action_values[c] - action_values[buy_day]
    if profit > best_profit:
        best_val = action_values[c]
        best_profit = profit

if best_profit > 0:
    sell_day = action_values.index(best_val)
    print("best action in day {}, profit: {}".format(sell_day+1, best_profit))

else:
    print("No transactions should be made")