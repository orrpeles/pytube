#!/bin/python
# Get audio from YouTube
# Ref: https://stackoverflow.com/questions/49204113/download-audio-from-youtube-using-pytube
# ref as to OS: https://stackoverflow.com/questions/2057045/pythons-os-makedirs-doesnt-understand-in-my-path

from pytube import YouTube
import os

yt = YouTube(str(input("Enter the link you wish to download: \n")))
t = yt.streams.filter(only_audio=True).all()
my_dir = os.path.expanduser('~/Music/')
t[0].download(my_dir)


