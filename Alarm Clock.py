from playsound import playsound as ps
import time
CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"
def alarm(seconds):
    time_elapsed=0
    print(CLEAR)
    while(time_elapsed<seconds):
        time.sleep(1)
        time_elapsed +=1
        time_left=seconds-time_elapsed
        min_left=time_left // 60
        seconds_left=time_left % 60
        print(f"{CLEAR_AND_RETURN}{min_left:02d}:{seconds_left:02d}")
    ps("alarm.mp3")

min=int(input("How many minutes to wait: "))
sec=int(input("How many seconds to wait: "))
total_seconds=min*60 + sec
alarm(total_seconds)        