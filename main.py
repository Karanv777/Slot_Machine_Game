import random as rnd

MAX_LINES = 3
MAX_BET = 100000
MIN_BET = 100

ROWS = 3
COLS = 3

symbol_count = { "A" : 2, "B" : 5, "C" : 8, "D" : 10 }

symbol_value = { "A" : 2, "B" : 1.5, "C" : 1.25, "D" : 1 }

def check_winning(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]         # here we get the first symbol of the line
        for column in columns:
            symbol_to_check = column[line] # here we fetching the next symbol to check if it is equal to the previous symbol
            if symbol != symbol_to_check:  # here we checking if the symbol = to the previous symbol
                break                      # if previous and current does not match we will break out.
        else:                              # this else will execute if break did not happen in the for loop.
            winning += values[symbol] * bet
            winning_lines.append(line + 1 )
    
    return winning, winning_lines

def spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count): #_ is used for looping in something :: _ is an anonymous variable.
            all_symbols.append(symbol)
    
    # columns = [[], [], []]  this is nested list :: here it is used to store the symbols in each column. generally it stores in rows but we are assuming it is storing in columns.
    columns = []
    for _ in range (cols):
        column = []
        current_symbol = all_symbols[:] # [:] is used to make a copy of list
        # here i am making a copy of all_symbols because once a value is selected by random from symbol_count, we have to remove it so that we dont get same value again.
        # suppose there are 2 A's selected so we have to remove it so that we dont get a third A.
        for _ in range (rows):
           value = rnd.choice(current_symbol)
           current_symbol.remove(value) 
           column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):        # [0] means we are assuming there is atleast one value ||  now i am transposing the columns so that they become elements of rows
        for i, column in enumerate(columns):  # enumerate gives the index as well as item. 
            if i != len(columns) - 1:
                print(column[row], end = " | ") # end = "" is for the slots to be on same line like a machine     # the number of rows we have is the number of elements in columns. 
            else:
                print(column[row], end = "\n")            # this is the last column so we dont need to print "|"

def deposit():
    while True:
        amount = input("Enter amount to deposit : ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid amount! Amount must be greater than 0.")
                
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True: 
        lines = input("Enter number of lines you want to bet on (1 - "+ str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Invalid number of Lines!")
                
        else:
            print("Please enter valid number of Lines.")

    return lines

def get_bet():
    while True:
        amount = input("Enter amount to Bet on each line: ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Invalid amount! Amount must be between ₹{MIN_BET} - ₹{MAX_BET}.")
                
        else:
            print("Please enter a number.")

    return amount

def Play(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if balance < total_bet:
            print(f"\nInsufficient balance! Balance : ₹{balance}.\n")
        else:
            break
    # if MIN_BET <= bet <= MAX_BET :    
    #     print(f"Please deposit amonut more than or eqaul to ₹{bet * lines}")
    
    print(f"You have dposited ₹{balance}")
    print(f"\nYou are betting ₹{bet} on {lines} lines.\nTotal Bet is ₹{total_bet}.\nRemaining Balance is ₹{balance - total_bet}")
    
    slots = spin(ROWS, COLS, symbol_count)
    print_slot(slots)

    winning, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"\nYou Won ₹{winning}.")
    print(f"You Won on lines : ", *winning_lines) # * is called unpack operator and its going to pass every single line from winning_lines list to print function
    # print(f"\nRemaining Balance : ₹{balance - total_bet + winning}")
    return winning - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance : ₹{balance}")
        start = input("Press enter to play or 'q' to quit.")
        if start.lower() == "q":
            exit(0)
        else:
            balance += Play(balance)
    print(f"Remaing Balance : ₹{balance}")
main()