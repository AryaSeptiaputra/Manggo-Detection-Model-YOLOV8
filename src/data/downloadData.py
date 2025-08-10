from datasets import load_dataset
import os

# Load dataset from Hugging Face
dataset = load_dataset("darthraider/fruit-ripeness-detection-dataset")

# Define the path 
save_path = "./data/external"

# Create the directory
os.makedirs(save_path, exist_ok=True)

# Save the downloaded dataset to the specified directory
dataset.save_to_disk(save_path)

# Print a message indicating the dataset has been saved successfully
print("Dataset has been saved to:", os.path.abspath(save_path))