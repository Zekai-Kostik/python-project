import pytube

url= "https:// "
youtube = pytube.YouTube(url)
video = youtube.streams.first()
video = youtube.streams.get_highest_resolution()
video.download()
video.download('/Downloads')
video.title
video.video_video_id
video.age_restricted

video.streams.all()
stream=video.streams.all()
for i in range:
    print(i)