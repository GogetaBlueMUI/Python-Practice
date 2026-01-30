import os
import shutil
import datetime
import schedule
import time
import tkinter as tk
from tkinter import filedialog

def get_source_location():
    source_path=filedialog.askdirectory()
    if source_path:
        print(f"The Selected File Location is {source_path}")
    return source_path
def get_des_location():
    des_path=filedialog.askdirectory()
    if des_path:
        print(f"The Destination Selected File Location is {des_path}")
    return des_path
def backup():
    root=tk.Tk()
    root.withdraw()
    today=datetime.date.today()
    spath=get_source_location()
    dpath=get_des_location()
    dest_path=os.path.join(dpath,str(today))
    try:
        shutil.copytree(spath,dest_path)
        print(f"Folder Copied to: {dest_path}")
    except FileExistsError:
        print(f"Folder already exit in {dpath}")
if __name__=="__main__":
    backup()
    