import os
from main import clean_title
from pytube import YouTube  # Execute the following command to install the library: pip install pytube
from pytube import Playlist


while True:

    # Input: YouTube playlist URL
    playlist_url = input("Enter the YouTube playlist URL: ")

    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Define the download path
        download_path = r"E:\temp\videos"  # Change this to your desired directory

        # Ensure the directory exists, create it if necessary
        os.makedirs(download_path, exist_ok=True)

        counter = 1

        # Iterate through the videos in the playlist and download them
        for video_url in playlist.video_urls:
            yt = YouTube(video_url)
            video_stream = yt.streams.get_highest_resolution()  # Get the highest resolution video stream
            title = clean_title(yt.title)
            video_file_name = f"{counter}) {title}.mp4"  # You can change the file extension if needed (e.g., .mkv, .webm)
            video_file_path = os.path.join(download_path, video_file_name)
            print(f"Downloading video: {title}...")
            video_stream.download(output_path=download_path, filename=video_file_name)
            print(f"Downloaded video: {title} as {video_file_name}")
            counter += 1

        print("Download of all videos completed!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
