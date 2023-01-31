from pytube import YouTube

class YoutubeConverter:
    
    def convert(url):
        file= YouTube(url)
        title = file.title
        file = file.streams.get_lowest_resolution()
        file.download("converter/videos")
        return title        
    

    def getThumb(url):
        file= YouTube(url)
        return file.thumbnail_url
