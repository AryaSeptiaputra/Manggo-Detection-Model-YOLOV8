# Mango-Detection-Model-YOLOV8

A mini self-project in computer vision that applies YOLOv8 to detect and localize mangoes in images and videos. The project demonstrates the end-to-end workflow of building a custom object detection model, starting from image annotation, through model training, and ending with performance evaluation using a dedicated dataset.

## Key Features  
- **Custom Mango Dataset from Hugging Face** – Downloaded from Hugging Face and manually annotated for improved accuracy.  
- **YOLOv8-Based Object Detection with Transfer Learning** – Utilizes pretrained YOLOv8 weights to speed up training and improve model performance. 
- **Complete Workflow** – Covers image annotation, model training, and evaluation in one streamlined process.  
- **Flexible Configuration** – Adjustable hyperparameters such as image size, batch size, and training epochs.  
- **Evaluation Metrics** – Includes mAP, precision, recall, and loss tracking (box, cls, dfl) for model performance analysis.  

## Dataset & Annotation

- The dataset was originally sourced from [Hugging Face](https://huggingface.co/datasets/darthraider/fruit-ripeness-detection-dataset) and consists of images containing mangoes in various conditions and backgrounds.  
- Image annotation was done manually by me using [Roboflow](https://universe.roboflow.com/arya-septiaputra/mango-detection-bsees) to draw bounding boxes around mangoes.  
- Annotations are exported in YOLOv8 format (`.txt` files) with normalized bounding box coordinates.  
- The dataset is organized into three subsets:  
  - `train` – for training the model  
  - `val` – for validation during training  
  - `test` – for final evaluation  

## Evaluation
The model was evaluated on the test subset to measure its performance in detecting mangoes. Evaluation metrics include:
- mAP@0.5: 99.4%
- Precision: 98.9%
- Recall: 99.6%
- Losses:
  - Box Loss: 23.75%
  - Class Loss: 14.55%
  - DFL Loss: 79.28%
