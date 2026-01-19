def can_make(length,large,small):
    total_large=min(large,int(length/5))
    remain=length-total_large*5
    if(small<remain):
        return False
    else:
        return True
def main():
    length=int(input("Enter the Length of the Line in Meters: "))
    large=int(input("Enter the Number of Large Bricks: "))
    small=int(input("Enter the Number of Small Bricks: "))
    flag=can_make(length,large,small)
    if(flag):
        print("Line can be build")
    else:
        print("Line can not be build")
main()    
