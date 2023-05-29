from pytube import YouTube

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100
    print(f"Progress: {progress:.2f}%")


video_url = input("Enter the YouTube video URL: ")

yt = YouTube(video_url, on_progress_callback=progress_callback)

video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')

print("Available Resolutions:")
for i, stream in enumerate(video_streams, start=1):
    print(f"{i}. Resolution: {stream.resolution}")

choice = int(input("Enter the number corresponding to your desired resolution: ")) - 1

if 0 <= choice < len(video_streams):
    chosen_stream = video_streams[choice]
    output_path = "D:\\PROJECTS\\Python\\Tools\\Youtube_download\\videos"
    chosen_stream.download(output_path=output_path)
    print("Video downloaded successfully!")
else:
    print("Invalid choice. Please try again.")

