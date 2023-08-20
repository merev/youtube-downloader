import os
import re
from pytube import YouTube  # Execute the following command to install the library: pip install pytube


# Function to clean the title by removing problematic characters
def clean_title(title):
    # Define a regular expression pattern to match problematic characters
    pattern = r'[\/:*?"<>|]'
    # Replace problematic characters with underscores
    cleaned_title = re.sub(pattern, '_', title)
    return cleaned_title


while True:

    # Input: YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Select the highest resolution video stream (you can customize this as needed)
        stream = yt.streams.get_highest_resolution()

        # Define the download path
        download_path = r"E:\temp\videos"  # Change this to your desired directory

        # Ensure the directory exists, create it if necessary
        os.makedirs(download_path, exist_ok=True)

        # Download the video
        title = clean_title(yt.title)
        video_file_name = f"{title}.mp4"  # You can change the file extension if needed (e.g., .mkv, .webm)
        video_file_path = os.path.join(download_path, video_file_name)
        print(f"Downloading video: {title}...")
        stream.download(output_path=download_path, filename=video_file_name)
        print(f"Downloaded video: {title} as {video_file_name}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
