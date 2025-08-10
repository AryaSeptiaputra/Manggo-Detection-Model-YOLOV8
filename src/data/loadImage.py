import os
from datasets import load_from_disk

# Load dataset from disk
dataset = load_from_disk("data/external")
train_data = dataset["train"]
test_data = dataset["test"]

# Prepare output directories for images
train_output_dir = "./data/external/images/train"
os.makedirs(train_output_dir, exist_ok=True)

test_output_dir = "./data/external/images/test"
os.makedirs(test_output_dir, exist_ok=True)

# Save train images with label 1 or 3
for i, item in enumerate(train_data):
    image = item["image"]
    label = item["label"]
    if label in [1, 3]:
        image.save(f"{train_output_dir}/img_{i}_label_{label}.jpg")

# Save test images with label 1 or 3
for i, item in enumerate(test_data):
    image = item["image"]
    label = item["label"]
    if label in [1, 3]:
        image.save(f"{test_output_dir}/img_{i}_label_{label}.jpg")

# Print success message
print("Success save image to:", train_output_dir, 'and', test_output_dir)