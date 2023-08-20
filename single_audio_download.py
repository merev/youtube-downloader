import os
from main import clean_title
from pytube import YouTube  # Execute the following command to install the library: pip install pytube


while True:

    # Input: YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Select the audio only
        stream = yt.streams.filter(only_audio=True).first()

        # Define the download path
        download_path = r"E:\temp\music"  # Change this to your desired directory

        # Ensure the directory exists, create it if necessary
        os.makedirs(download_path, exist_ok=True)

        # Download the video
        title = clean_title(yt.title)
        audio_file_name = f"{title}.mp3"
        audio_file_path = os.path.join(download_path, audio_file_name)
        print(f"Downloading audio from {title}...")
        stream.download(output_path=download_path, filename=audio_file_name)
        print(f"Downloaded audio from {title} as {audio_file_name}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        