import curses 
from curses import wrapper
import time
import random
def load_file():
    with open("WPM_Test.txt","r")as f:
        lines=f.readlines()
    return random.choice(lines).strip()

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Typing Test")
    stdscr.addstr("\nPress any Key to Begin!")
    stdscr.getkey()
    stdscr.refresh()
def display_text(stdscr,target,user_text,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"{wpm}")
    for i, char in enumerate(user_text):
        correct_char=target[i]
        if char==correct_char:
            color=curses.color_pair(1)
        else:
            color=curses.color_pair(2)
        stdscr.addstr(0,i,char,color)

def wpm_test(stdscr):
    target_text=load_file()
    User_text=[]
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True)
    while(True):
        time_elapsed=max(time.time()-start_time,1)
        wpm=round(((len(User_text))/(time_elapsed/60))/5)
        stdscr.clear()
        display_text(stdscr,target_text,User_text,wpm)
        stdscr.refresh()
        if "".join(User_text)==target_text:
            stdscr.nodelay(False)
            break
        try:
            key=stdscr.getkey()
        except:
            continue
        if ord(key)==27:
            return False
        if key in ["\n", "\r", "KEY_ENTER"]:
            continue
        if key in ("KEY_BACKSPACE", '\b',"\x7f"):
            if len(User_text)>0:
                User_text.pop()
        elif len(User_text)< len(target_text):
            User_text.append(key)
      


    
def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    start_screen(stdscr)
    while(True):
        flag=wpm_test(stdscr)
        if flag==False:
            break
        stdscr.addstr(2,0,"You have completed the test!! Press any key to continue")
        key=stdscr.getkey()
        if ord(key)==27:
            break

wrapper(main)
