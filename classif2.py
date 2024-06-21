from ultralytics import YOLO
import os

# Load the model
model = YOLO(path_model)

# Directory where the images are located
image_directory = path_validation

# List all image files in the directory
image_paths = [os.path.join(image_directory, f) for f in os.listdir(image_directory) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Process each image individually
for img_path in image_paths:
    result = model(source=img_path, show=False, conf=0.5, save=True)
    print(f"Results for {img_path}:")
    print(result)
