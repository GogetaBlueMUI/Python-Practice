import random as rand
max_no_of_rows=3
max_no_of_cols=3
max_no_of_lines=3
max_bet=100
min_bet=1
Symbols={
    "A":3,
    "B":4,
    "C":6,
    "D":8
}
Symbol_Value={
    "A":5,
    "B":3,
    "C":4,
    "D":2
}
def deposit():
    while(True):
        amount=input("Please Enter a Deposit Amout: $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Please Enter amount greater then 0")
        else:
            print("Please Enter a Digit")
    return amount
def no_of_lines():
    while(True):
        lines=input("Please Enter number of lines between (1-" + str(max_no_of_lines)+ ") you want to bet on? ")
        if lines.isdigit():
            lines=int(lines)
            if 0 < lines <= max_no_of_lines:
                break
            else:
                print("Please Enter Valied no of lines")
        else:
            print("Please Enter a Digit")
    return lines
def get_bet():
    while(True):
        amount=input("Please Enter the amount you want to bet on: $")
        if amount.isdigit():
            amount=int(amount)
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f"Amount must be between ${min_bet}-${max_bet}")
        else:
            print("Please Enter a Digit")
    return amount
def get_slot_machine(max_no_of_rows,max_no_of_cols,Symbols):
    all_symbols=[]
    for symbol,symbol_count in Symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    Column=[]
    for _ in range(max_no_of_cols):
        temp_col=[]
        temp_all_symbol=all_symbols[:]
        for _ in range(max_no_of_rows):
            value=rand.choice(temp_all_symbol)
            temp_all_symbol.remove(value)
            temp_col.append(value)
        Column.append(temp_col)
    return Column
def print_slot_machine(Column,max_no_of_cols,max_no_of_rows):
    for i in range(max_no_of_rows):
        for j in range(max_no_of_cols):
            if(j<max_no_of_cols-1):
                print(Column[j][i],end=" | ")
            else:
                print(Column[j][i],end="")
        print()        
def cal_winnings(Column,lines,bet,values):
    winning=0
    Winning_lines=[]
    for line in range(lines):
        symbol=Column[0][line]
        for col in Column:
            if symbol!=col[line]:
                break
        else:
            winning=values[symbol]*bet 
            Winning_lines.append(line+1)
    return winning,Winning_lines      
def spin(balance):
    lines=no_of_lines()
    while(True):
        bet=get_bet()
        total_bet=bet*lines
        if balance < total_bet:
            print(f"You dont have enought Balance. Your current Balance is ${balance}")
        else:
            break    
    print(f"You are betting ${bet} on ${lines}. Total bet is ${total_bet}")
    Column=get_slot_machine(max_no_of_rows,max_no_of_cols,Symbols)
    print_slot_machine(Column,max_no_of_cols,max_no_of_rows)
    win,win_lines=cal_winnings(Column,lines,bet,Symbol_Value)
    print(f"You Won Total of &{win}")
    if win_lines:
        print(f"You won on line", *win_lines)
    return win - total_bet
 
def main():
    balance=deposit()
    while(True):
        if balance == 0:
            break
        print(f"Current Balance is ${balance}")
        responce=input("Press Enter to Roll and q to Quit: ")
        responce.lower()
        if responce=="q":
            break
        balance=balance+spin(balance)
    print(f"Your Left with ${balance}")
main()