from pytube import Playlist, YouTube
import sys

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100
    sys.stdout.write(f"\rProgress: {progress:.2f}%")
    sys.stdout.flush()

playlist_url = input("Enter the YouTube playlist URL: ")

playlist = Playlist(playlist_url)

print("Playlist Name:", playlist.title)
playlist_title = playlist.title

video_urls = playlist.video_urls

for index, video_url in enumerate(video_urls, start=1):
    yt = YouTube(video_url, on_progress_callback=progress_callback)

    video_stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='720p').first()

    if not video_stream:
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    output_path = f"D:\\PROJECTS\\Python\\Tools\\Youtube_download\\videos\\{playlist_title}"
    video_title = video_stream.title

    video_filename = f"{index:02d}_{video_title}.mp4"

    try:
        video_stream.download(output_path=output_path, filename=video_filename)
        sys.stdout.write("\n")
        sys.stdout.flush()
        print(f"'{video_title}' downloaded successfully!")
    except Exception as e:
        sys.stdout.write("\n")
        sys.stdout.flush()
        print(f"'{video_title}' download unsuccessful")
