from pytube import YouTube

class YoutubeConverter:
    
    def convert(url):
        file= YouTube(url)
        title = file.title
        file = file.streams.get_lowest_resolution()
        file.download()