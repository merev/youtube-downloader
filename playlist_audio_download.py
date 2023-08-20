import os
from pytube import YouTube  # Execute the following command to install the library: pip install pytube
from pytube import Playlist

while True:

    # Input: YouTube playlist URL
    playlist_url = input("Enter the YouTube playlist URL: ")

    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Define the download path
        download_path = r"E:\temp\music"  # Change this to your desired directory

        # Ensure the directory exists, create it if necessary
        os.makedirs(download_path, exist_ok=True)

        counter = 1

        # Iterate through the videos in the playlist and download their audio
        for video_url in playlist.video_urls:
            yt = YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            title = yt.title
            audio_file_name = f"{counter}) {title}.mp3"
            audio_file_path = os.path.join(download_path, audio_file_name)
            print(f"Downloading audio from {title}...")
            audio_stream.download(output_path=download_path, filename=audio_file_name)
            print(f"Downloaded audio from {title} as {audio_file_name}")
            counter += 1

        print("Download of all audio tracks completed!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
