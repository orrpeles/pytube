#!/bin/python
# Get audio from YouTube
# Ref: https://stackoverflow.com/questions/49204113/download-audio-from-youtube-using-pytube
# ref as to OS: https://stackoverflow.com/questions/2057045/pythons-os-makedirs-doesnt-understand-in-my-path
# ref progress_func: https://stackoverflow.com/questions/49185538/how-to-add-progress-bar

from pytube import YouTube
import os

def progress_func(self, stream, chunk, file_handle, bytes_remaining):
    size = video.filesize
    p=0
    while p<=100:
        progress = p
        print(str(p)+'%')
        p = percent(bytes_remaining, size)

def percent(self, tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc

dowLink = YouTube(str(input("Enter the link you wish to download: \n")))
yt = YouTube(dowLink, on_progress_callback=progress_func)
t = yt.streams.filter(only_audio=True).all()
my_dir = os.path.expanduser('~/Music/')
t[0].download(my_dir)


