import os
from pytube import YouTube
link = input("Link:")
directory = input("Directory:")
try:
    yt = YouTube(link)
except:
    print("Invalid link")
    exit()

mp3 = yt.streams.filter(only_audio=True).first()
print("Downloading..")
output = mp3.download(directory)
base, ext = os.path.splitext(output)
to_mp3=base + ".mp3"
os.rename(output, to_mp3)
print("Download Complete!")