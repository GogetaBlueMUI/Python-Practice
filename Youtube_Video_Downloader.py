import yt_dlp as yt
import tkinter as tk
from tkinter import filedialog
def download_youtube_video(url, path):
    try:
      video_parameters={
            'outtmpl': f'{path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'no_warnings': 'True'
      }
      ydl=yt.YoutubeDL(video_parameters)
      ydl.download(url)
    except Exception as e:
        print("Error:", e)
def open_file_dialog():
    path=filedialog.askdirectory()
    if path:
      print(f"Path Selected is: {path}")
    return path 
if __name__== "__main__":
   root=tk.Tk()
   root.withdraw()
   videourl=input("Enther the Video URL: ")
   path=open_file_dialog()
   if path:
      download_youtube_video(videourl,path)
      print("Video is Started Downloaded")
   else:
      print("Invalid Path")