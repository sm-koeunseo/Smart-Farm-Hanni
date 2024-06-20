import os
import time
from datetime import datetime
import subprocess
import pytz
import torch

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
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error capturing image: {e}")
        return None

def detect_objects(image_path, model, output_dir):
    # �̹��� �ε�
    img = cv2.imread(image_path)
    
    # ��ü ���� ����
    results = model(img)
    
    # ���� ��� ����
    save_path = os.path.join(output_dir, os.path.basename(image_path))
    results.save(save_path)
    
    print(f"Object detection completed. Results saved in: {save_path}")

def main():
    time.sleep(10)  # preparing time
    capture_dir = "/home/leechaeyoung/Documents/kidneyBean/capture"
    model_path = "/home/leechaeyoung/Downloads/kidney_yolov5s_results/best.pt"
    output_dir = "/home/leechaeyoung/Documents/kidneyBean/model_results"
    
    # Create the capture directory if it doesn't exist
    os.makedirs(capture_dir, exist_ok=True)
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # model load
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    
    # Capture an image
    image_path = capture_image(capture_dir)
    
    if image_path:
        # Perform object detection on the captured image
        detect_objects(image_path, model, output_dir)
    
    time.sleep(10)

if __name__ == "__main__":
    main()