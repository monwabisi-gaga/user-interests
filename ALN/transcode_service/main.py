import subprocess
import os

def transcode_video(input_path: str, output_dir: str):
    """
    Transcodes a video into two variants: 1080p H.264 and 1440p H.265.

    Args:
        input_path: The path to the input video file.
        output_dir: The directory to save the transcoded videos.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1080p H.264 transcoding
    output_1080p = os.path.join(output_dir, "1080p.mp4")
    ffmpeg_1080p_cmd = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "22",
        "-c:a", "copy",
        output_1080p
    ]
    print(f"Running command: {' '.join(ffmpeg_1080p_cmd)}")
    subprocess.run(ffmpeg_1080p_cmd, check=True)

    # 1440p H.265 transcoding
    output_1440p = os.path.join(output_dir, "1440p.mp4")
    ffmpeg_1440p_cmd = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "libx265",
        "-preset", "slow",
        "-crf", "28",
        "-c:a", "copy",
        output_1440p
    ]
    print(f"Running command: {' '.join(ffmpeg_1440p_cmd)}")
    subprocess.run(ffmpeg_1440p_cmd, check=True)