#!/bin/python
# Get audio from YouTube
# Ref: https://stackoverflow.com/questions/49204113/download-audio-from-youtube-using-pytube
# ref as to OS: https://stackoverflow.com/questions/2057045/pythons-os-makedirs-doesnt-understand-in-my-path
# ref progress_func: https://stackoverflow.com/questions/49185538/how-to-add-progress-bar

from pytube import YouTube
import os

# ask for input
link = (str(input("Enter the link you wish to download: \n")))

# define progress bar
def progress_function(stream, chunk, file_handle, bytes_remaining):
    print(round((1-bytes_remaining/tube.filesize)*100, 3), '% done...')

# define YouTube object
yt = YouTube(link, on_progress_callback=progress_function)
# specify stream
tube = yt.streams.filter(progressive=True, file_extension='mp4').first()
# define path and download file
my_dir = os.path.expanduser('~/Music/')
tube.download(my_dir)

