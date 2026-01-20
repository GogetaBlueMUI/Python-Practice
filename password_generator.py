import random
import string

def generate_password(min_length,Has_Numbers=True,Has_Special=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    character=""
    character=character+letters
    if Has_Numbers==True:
        character=character+digits
    if Has_Special==True:
        character=character+special
    
    meet_criteria=False
    has_digit=False
    has_special=False
    pd=""

    while not meet_criteria or len(pd) < min_length:
        rd=random.choice(character)

        pd=pd+rd
        if rd in digits:
            has_digit=True
        elif rd in special:
            has_special=True
        meet_criteria=True
        if Has_Numbers:
            meet_criteria=has_digit
        if Has_Special:
            meet_criteria=meet_criteria and has_special
    return pd

min_length=int(input("Enter the minimun number of length: "))
has_number=input("Do you want number in your password 'y' or 'n': ").lower()== 'y'
has_special=input("Do you want Special Character in your password 'y' or 'n': ").lower()== 'y'
pwd=generate_password(min_length,has_number,has_special)
print(f"Your Password is {pwd}")

