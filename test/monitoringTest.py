import os
import time
from datetime import datetime
import subprocess
import pytz

def capture_image(output_dir):
    kst = pytz.timezone('Asia/Seoul')
    timestamp = datetime.now(kst).strftime("%Y%m%d_%H%M%S")
    output_file = f"{output_dir}/capture_{timestamp}.jpg"
    
    cmd = [
        "libcamera-still",
        "-o", output_file,
        "--width", "640",
        "--height", "480",
        "-t", "1",
        "-n"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Image captured and saved as: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing image: {e}")

def main():
    output_dir = "/home/leechaeyoung/Documents/capture-pi"
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    capture_image(output_dir)

if __name__ == "__main__":
    main()
