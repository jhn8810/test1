from pytube import YouTube  
import pytube  
try:
<<<<<<< HEAD
    video_url = 'https://www.youtube.com/watch?v=lTTajzrSkCw'   
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.first()  
    video.download('C:/Windows/System32/httpd-2.4.52-win64-VS16/Apache24/test/hello-git/loc-git/youtube')  
    print("Download Successfull !!")
=======
        video_url = 'https://www.youtube.com/watch?v=lTTajzrSkCw'   
            youtube = youube.YouTube(video_url)  
                video = youtube.streams.first()  
                    video.download('C:/Windows/System32/httpd-2.4.52-win64-VS16/Apache24/test/hello-git/loc-git/youtube')  
                        print("Download Successfull !!")
>>>>>>> cd3548cc3623212d11c3fa48a57fb0c7f3738a20
except:
    print("Something Went Wrong !!")
