import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]
def find_path(maze,stdscr):
    start='O'
    end='X'
    path=[]
    start_position=find_start(maze,start)
    row=len(maze)
    col=len(maze[0])
    parent={}
    parent[start_position]=None
    direction=[
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]
    q=queue.Queue()
    visited=set()
    q.put(start_position)
    while not q.empty():
        value=q.get()
        visited.add(value)
        i,j=value
        stdscr.clear()
        print_maze(maze, stdscr)
        for vr, vc in visited:
            stdscr.addstr(vr, vc*2, 'X', curses.color_pair(3))
        stdscr.refresh()
        time.sleep(1)
        if maze[i][j]=='X':
            end=(i,j)
            break
        for ni, nj in direction:
            nr=i+ni
            nc=j+nj
            newvalue=(nr,nc)
            if 0 <= nr < row and 0 <= nc < col:
                if maze[nr][nc] != '#':
                    if newvalue not in visited:
                        visited.add(newvalue)
                        q.put(newvalue)
                        parent[(nr,nc)]=(i,j)
    cur=(i,j)
    while cur is not None:
        path.append(cur)
        cur=parent[cur]
    path.reverse()
    return path
         
def find_start(maze,start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value==start:
                return i,j
            

def print_maze(maze, stdscr, path=None):
    if path is None:
        path = set()

    Blue = curses.color_pair(1)
    Red = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "*", Red)   # 🔥 path visible
            else:
                stdscr.addstr(i, j*2, value, Blue)

def main(stdscr):
    curses.start_color()   # 🔥 REQUIRED
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_BLUE, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)

    stdscr.clear()

    # find path
    path = find_path(maze, stdscr)

    # draw maze + path
    print_maze(maze, stdscr, set(path))

    stdscr.refresh()
    stdscr.getch()


wrapper(main)
    