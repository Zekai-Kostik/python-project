from asyncio import streams
from pytube import YouTube

def video_download():
    i = YouTube (input("Please input your link : "))
    stream = i.streams.filter(progressive=True).first()
    stream.download()
    print("-"*45)
    print("Download Completed...")
    print("The name of the downloaded file :",i.title)

def audio_download():
    i= YouTube(input("Please input your link:"))
    stream = i.streams.filter(only_audio=True).first()
    stream.download()
    print("-"*45)
    print("Download Completed...")
    print("The name of the downloaded file :",i.title)

while True :
    print("Welcome to the audio and video download page. Please make a choose.\n")
    make_choose = input("1-Video Download :\n2-Mp3 Download : \n")

    if make_choose=="1":
        video_download()
        input("Do you want to continue?")

    elif make_choose=="2":
        audio_download() 
        input("Do you want to continue?")
        