from pytube import YouTube  
import pytube  
try:
        video_url = 'https://www.youtube.com/watch?v=lTTajzrSkCw'   
            youtube = youube.YouTube(video_url)  
                video = youtube.streams.first()  
                    video.download('c:/Programs Files (x86)/httpd-2.4.52-win64-VS16/Apache24/hello-git/loc-git/youtube')  
                        print("Download Successfull !!")
except:
    print("Something Went Wrong !!")
