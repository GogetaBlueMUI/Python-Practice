import random

COLORS=["R","G","B","Y","W","O"]
TRIES=10
CODE_LENGTH=4

def generate_code():
    code=[]
    for _ in range(CODE_LENGTH):
        color=random.choice(COLORS)
        code.append(color)
    return code
def guess_code():
    while True:
        guess=input("Enter you Guess with space between each guess: ").upper().split(" ")
        if len(guess)<CODE_LENGTH:
            print(f"Enter Code of Length {CODE_LENGTH}")
            continue
        for code in guess:
            if code not in COLORS:
                print("Invalid Code")
                break
        else:
            break
    return guess
def check_code(guess,real_code):
    correct_position=0
    used_position=[]
    used_guess=[]
    incorrect_position=0
    for i, g in enumerate(guess):
        if g==real_code[i]:
            correct_position+=1
            used_position.append(i)
            used_guess.append(i)
    for i,g in enumerate(guess):
        if i in used_guess:
            continue
        else:
            for j,c in enumerate(real_code):
                if g != c:
                    continue
                else:
                    if j not in used_position:
                        used_position.append(j)
                        used_guess.append(i)
                        incorrect_position+=1
                        break
    return correct_position, incorrect_position
def game():
    print(f"Welcome to mastermind game you have {TRIES} tries to guess the Code....")
    print("The Valid Colors are: ",*COLORS)
    code=generate_code()
    for attempts in range(1,TRIES+1):
        guess=guess_code()
        correct_position,incorrect_position=check_code(guess,code)
        if correct_position==CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries ")
            break
        print(f"Correct Position are {correct_position}")
        print(f"Incorrect Position are {incorrect_position}")
    else:
        print("You ran out of Tries: ",*code)
if __name__=="__main__":
    game()