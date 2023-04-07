from pytube import Playlist, YouTube

# Ask user for the YouTube playlist URL
url = input("Enter the YouTube playlist URL: ")

# Create a Playlist object
playlist = Playlist(url)

# Print the playlist title and number of videos
print(f"Downloading playlist: {playlist.title}")
print(f"Number of videos: {len(playlist.video_urls)}")

# Ask user for the desired video resolution
resolution = input("Enter the desired video resolution (e.g. 720p): ")

# Ask user for the destination folder
destination_folder = input("Enter the destination folder path: ")

# Download each video in the playlist
for video_url in playlist.video_urls:
    # Create a YouTube object for the video
    yt = YouTube(video_url)

    # Get the video stream with the desired resolution
    stream = yt.streams.filter(res=resolution, progressive=True).first()

    # Download the video to the specified folder
    stream.download(output_path=destination_folder)

    # Print the video title and download status
    print(f"Downloaded: {yt.title}")