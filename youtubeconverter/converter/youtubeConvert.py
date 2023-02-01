from pytube import YouTube

class YoutubeConverter:
    
    def convert(url,id):
        file= YouTube(url)
        title = file.title
        file = file.streams.get_lowest_resolution()
        file.download("converter/videos",filename=id+".mp4")
        return title        
    
    def getThumb(url):
         file= YouTube(url)
         return file.thumbnail_url