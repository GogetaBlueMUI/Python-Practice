import random
import time
Operator=["+","-","*"]
max=13
min=3
total=10
def probelem_generator():
    left=random.randint(min,max)
    right=random.randint(min,max)
    op=random.choice(Operator)
    question=str(left) + " " + op + " " + str(right)
    answer=eval(question)
    return answer,question
wrong=0
input("Press Enter to Start ")
print("---------------------")
start_time=time.time()
answer,question=probelem_generator()
for i in range(total):
    answer,problem=probelem_generator()
    while(True):
        guess=input("Enter your Answer for "+ str(i+1) + " Problem# "+ problem+": ")
        if guess==str(answer):
            break
        wrong+=1
end_time=time.time()
total_time=end_time-start_time
accuracy=((total)/(total+wrong))*100
print("----------------------")
print("Nice Work You Finished in ",total_time," with accuracy of ",accuracy)


