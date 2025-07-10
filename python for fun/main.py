import os
from moviepy import VideoFileClip

def split_video(input_path, output_folder, segment_duration=120):
    """
    Split a video file into multiple segments of specified duration.
    
    Args:
        input_path (str): Path to the input video file
        output_folder (str): Folder to save the output segments
        segment_duration (int): Duration of each segment in seconds (default: 120 = 2 minutes)
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Load the video file
    video = VideoFileClip(input_path)
    duration = video.duration
    
    # Calculate number of segments needed
    num_segments = int(duration // segment_duration) + 1
    
    print(f"Splitting {input_path} ({duration/3600:.2f} hours) into {num_segments} segments of {segment_duration/60} minutes each")
    
    # Split the video into segments
    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = min((i + 1) * segment_duration, duration)
        
        # Skip very short segments at the end
        if end_time - start_time < 10:  # less than 10 seconds
            continue
            
        segment = video.subclip(start_time, end_time)
        output_path = os.path.join(output_folder, f"segment_{i+1:03d}.mp4")
        segment.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Saved {output_path}")
    
    video.close()
    print("Splitting completed!")

if __name__ == "__main__":
    # Example usage
    input_video = "large_video.mp4"  # Replace with your video path
    output_dir = "video_segments"
    
    split_video(input_video, output_dir)