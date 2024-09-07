from pytube import YouTube

url="https://youtu.be/oRGhqUjWF6U?si=cS8r9GuQXLD8xyC0"

yt=YouTube(url)

print(f"Title: {yt.title}")
print(f"Author: {yt.author}")
print(f"Publish date: {yt.publish_date}")
print(f"Description: {yt.description}")

video=yt.streams.filter(res="720p", type="video").first()
video.download(output_path="Download/")
#video.download()

print("Video Download Successful!")