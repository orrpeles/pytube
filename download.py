#!/bin/python
# Get audio from YouTube
# Ref: https://stackoverflow.com/questions/49204113/download-audio-from-youtube-using-pytube

from pytube import YouTube
yt = YouTube(str(input("Enter the link you wish to download: \n")))
t = yt.streams.filter(only_audio=True).all()
t[0].download('/home/op/Music')

