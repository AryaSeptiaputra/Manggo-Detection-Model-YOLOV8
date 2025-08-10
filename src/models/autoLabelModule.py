from ultralytics import YOLO
import os
import shutil

# Load the trained YOLO model with the specified weights
model = YOLO("C:/Project/Manggo Detection Model/models/manggo-detection-yolo8l-50/weights/best.pt")

# Define the paths for images, labels, and temporary output directory
images_folder = "C:/Project/Manggo Detection Model/data/interim/Manggo-Detection-2/train/images"
labels_folder = "C:/Project/Manggo Detection Model/data/interim/Manggo-Detection-2/train/labels"
temp_output = "temp_labels"

# Run prediction on all images in the images_folder
# Save the predicted labels as text files in the temp_output directory
model.predict(
    source=images_folder,
    conf=0.9,
    save_txt=True,
    save_conf=True,
    project=temp_output,
    name="pred",
    exist_ok=True
)

# Copy all predicted label files from the temporary output to the labels folder
pred_labels = os.path.join(temp_output, "pred", "labels")
for file in os.listdir(pred_labels):
    shutil.copy2(os.path.join(pred_labels, file), os.path.join(labels_folder, file))

# Print a success message
print("✅ Old labels have been replaced with new auto-label results")