import sys
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_file_path, output_audio_path):
    """
    Extracts audio from a video file and saves it as a .wav file.

    :param video_file_path: Path to the video file
    :param output_audio_path: Path where the .wav file will be saved
    """
    try:
        # Load the video file
        video = VideoFileClip(video_file_path)

        # Extract the audio
        audio = video.audio

        # Write the audio to a file
        audio.write_audiofile(output_audio_path, codec='pcm_s16le')

        print(f"Audio extracted and saved to {output_audio_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Check if the script is being run directly and ensure enough arguments are provided
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <source_video_path> <output_audio_path>")
        sys.exit(1)

    source_video_path = sys.argv[1]
    output_audio_path = sys.argv[2]

    extract_audio_from_video(source_video_path, output_audio_path)
