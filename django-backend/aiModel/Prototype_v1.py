#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ultralytics import YOLO
import easyocr
import cv2
import numpy as np
import os

# In[3]:


# We will be using 3 diff models for evaluate the image, since each model does different things

food_detector = YOLO(os.path.join(os.path.dirname(__file__), "best.pt")) # Food detector, This one can replace with your file path with trained model
person_detector = YOLO("yolov8n.pt")  # seperate YOLOv8n model for people detection
reader = easyocr.Reader(['en'])  # EasyOCR for text recognition


# In[17]:


# Detect if got food or not
def detect_food(image_path):
    results = food_detector(image_path)
    for result in results:
        if len(result.boxes) > 0:
            return True  # Food detected
    return False  # No food found

# Detect if got big words such as BUY, FREE, DISCOUNT, OFFER
def detect_promotional_text(image_path):
    """Check for promotional words like 'Buy 1 Free 1' or 'Discount'."""
    image = cv2.imread(image_path)
    results = reader.readtext(image)

    promo_keywords1 = ["BUY", "FREE"]
    promo_keywords2 = ["DISCOUNT", "OFF"]
    for _, text, _ in results:
        text = text.upper()
        if any(keyword in text for keyword in promo_keywords1):
            return 10  # Max score if promo detected
        elif any(keyword in text for keyword in promo_keywords2):
            return 7
    return 0  # Lowest score if no promo text found

# Count how many peeps in the image
def count_people(image_path):
    results = person_detector(image_path)
    num_people = sum(1 for box in results[0].boxes if box.cls == 0)
    
    # Scale 1-10 based on people count
    if num_people == 0:
        return 0  # No people
    elif num_people == 1:
        return 3
    elif num_people <= 3:
        return 7
    else:
        return 10  # Many people

# Evaluate the color and brightness of image
def compute_colorfulness(image_path):
    image = cv2.imread(image_path)
    (B, G, R) = cv2.split(image)
    rg = np.absolute(R - G)
    yb = np.absolute(0.5 * (R + G) - B)
    std_rg, mean_rg = np.std(rg), np.mean(rg)
    std_yb, mean_yb = np.std(yb), np.mean(yb)
    colorfulness = np.sqrt((std_rg**2 + std_yb**2) + (mean_rg**2 + mean_yb**2))

    # This scales to 1-10
    min_c, max_c = 20, 150
    normalized_score = ((colorfulness - min_c) / (max_c - min_c)) * 9 + 1
    return round(min(max(normalized_score, 1), 10), 2)

# Combine all the variables above
def evaluate_food_image(image_path):
    if not detect_food(image_path):
        return {"Message": "Not a food picture"}

    scores = {
        "Remunerative": detect_promotional_text(image_path),
        "Informative": 5,  # Placeholder for now
        "Relational": count_people(image_path),
        "Entertainment": compute_colorfulness(image_path)
    }
    return scores


# In[19]:

# result = evaluate_food_image(image_path)
# print(result)

