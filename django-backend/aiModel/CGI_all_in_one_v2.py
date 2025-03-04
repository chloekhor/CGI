import cv2
import easyocr
import re
from googletrans import Translator
from ultralytics import YOLO
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from keras._tf_keras.keras.applications.resnet50 import preprocess_input
from keras._tf_keras.keras.preprocessing.image import img_to_array

####################################
# Entertainment Evaluation Module
####################################
def run_entertainment(image_path):
    """
    Evaluate the entertainment aspect of the image using:
      - OCR (with translation) to check for exclamation marks.
      - Brightness measurement (score: 1-4).
      - Sharpness measurement (score: 1-2).
      - YOLO detection for food and face (adds 2 if food area > face area).
    Returns the final entertainment score.
    """
    def perform_ocr(img_path):
        reader_ch = easyocr.Reader(['ch_sim', 'en'], gpu=False)
        reader_ms = easyocr.Reader(['ms', 'en'], gpu=False)
        results_ch = reader_ch.readtext(img_path, detail=0)
        results_ms = reader_ms.readtext(img_path, detail=0)
        return " ".join(results_ch + results_ms)

    def translate_to_english(text):
        translator = Translator()
        try:
            return translator.translate(text, dest='en').text
        except Exception as e:
            print("Translation error:", e)
            return text

    def check_exclamation(text):
        return 2 if "!" in text else 0

    def measure_brightness(img_path):
        image = cv2.imread(img_path)
        if image is None:
            print("Error: Unable to read image for brightness measurement.")
            return 1
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        avg = gray.mean()
        # Map average brightness (0-255) to a score between 1 and 4.
        score = (avg / 255) * (4 - 1) + 1
        return max(1, min(4, round(score)))

    def measure_sharpness(img_path):
        image = cv2.imread(img_path)
        if image is None:
            print("Error: Unable to read image for sharpness measurement.")
            return 1
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        return 2 if variance > 100.0 else 1

    def detect_food_and_face(img_path):
        model_food = YOLO("/Users/timzz/CGI/django-backend/aiModel/best.pt")
        model_face = YOLO("/Users/timzz/CGI/django-backend/aiModel/face.pt")
        food_area = face_area = 0

        results_food = model_food.predict(source=img_path, save=False, verbose=False)
        if results_food and len(results_food) > 0:
            boxes = results_food[0].boxes
            if boxes is not None and boxes.shape[0] > 0:
                for box in boxes:
                    coords = box.xyxy.cpu().numpy()[0]
                    area = (coords[2] - coords[0]) * (coords[3] - coords[1])
                    food_area = max(food_area, area)

        results_face = model_face.predict(source=img_path, save=False, verbose=False)
        if results_face and len(results_face) > 0:
            boxes = results_face[0].boxes
            if boxes is not None and boxes.shape[0] > 0:
                for box in boxes:
                    coords = box.xyxy.cpu().numpy()[0]
                    area = (coords[2] - coords[0]) * (coords[3] - coords[1])
                    face_area = max(face_area, area)
        return food_area, face_area

    def compare_food_face(img_path):
        food_area, face_area = detect_food_and_face(img_path)
        return 2 if food_area > face_area else 0

    # Process image for entertainment evaluation
    ocr_text = perform_ocr(image_path)
    translated = translate_to_english(ocr_text)
    marks = (check_exclamation(translated) +
             measure_brightness(image_path) +
             measure_sharpness(image_path) +
             compare_food_face(image_path))
    return round(marks)

####################################
# Information Evaluation Module
####################################
def run_information(image_path):
    """
    Evaluate the informational content of the image by:
      - Detecting food using YOLO.
      - Extracting and translating OCR text.
      - Checking the text for food, event, date/time, and pricing keywords.
    Returns the final information score (capped at 10).
    """
    def load_keywords():
        food_df = pd.read_csv("/Users/timzz/CGI/django-backend/aiModel/malaysian_food_list_full.csv")
        event_df = pd.read_csv("/Users/timzz/CGI/django-backend/aiModel/Cleaned_Malaysian_Event.csv")
        postcode_df = pd.read_csv("/Users/timzz/CGI/django-backend/aiModel/cleaned_Malaysia_Postcode.csv")
        food_keywords = food_df.iloc[:, 0].dropna().astype(str).str.lower().tolist()
        event_keywords = event_df.iloc[:, 0].dropna().astype(str).str.lower().tolist()
        postcode_keywords = postcode_df.iloc[:, 0].dropna().astype(str).str.lower().tolist()
        return food_keywords, postcode_keywords, event_keywords

    def load_food_ingredient_keywords():
        df = pd.read_csv("/Users/timzz/CGI/django-backend/aiModel/food_ingredients.csv")
        if df.shape[1] < 2:
            raise ValueError("food_ingredients.csv should have at least two columns")
        food_names = df.iloc[:, 0].dropna().astype(str).str.lower().tolist()
        food_ingredients = df.iloc[:, 1].dropna().astype(str).str.lower().tolist()
        return list(set(food_names + food_ingredients))

    def check_category(text, keywords):
        return any(word in text.lower() for word in keywords)

    def check_date(text):
        pattern = r'\b(?:\d{1,2}[-/_]\d{1,2}[-/_]\d{2,4}|\d{4}[-/_]\d{1,2}[-/_]\d{1,2})\b'
        return re.search(pattern, text) is not None

    def check_pricing(text):
        pattern = r'\bRM\s*\d+(?:\.\d+)?\b'
        return re.search(pattern, text, re.IGNORECASE) is not None

    def check_day(text):
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
                "mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        return any(day in text.lower() for day in days)

    def check_time(text):
        pattern24 = r'\b(?:[01]?\d|2[0-3])(?::?[0-5]\d)\b'
        pattern_ampm = r'\b\d{1,2}(?::\d{2})?\s?(?:am|pm)\b'
        return (re.search(pattern24, text, re.IGNORECASE) or 
                re.search(pattern_ampm, text, re.IGNORECASE)) is not None

    def correct_pricing_errors(text):
        return re.sub(r'(?i)(RM\s*\d+)[Oo]\b', lambda m: m.group(1) + '0', text)

    def perform_ocr(img_path):
        reader_ch = easyocr.Reader(['ch_sim', 'en'])
        reader_ms = easyocr.Reader(['ms', 'en'])
        results = reader_ch.readtext(img_path, detail=0) + reader_ms.readtext(img_path, detail=0)
        return " ".join(results)

    def translate_to_english(text):
        translator = Translator()
        try:
            return translator.translate(text, dest='en').text
        except Exception as e:
            print("Translation error:", e)
            return text

    def detect_food(img_path):
        model_non = YOLO("/Users/timzz/CGI/django-backend/aiModel/best.pt")
        model_my = YOLO("/Users/timzz/CGI/django-backend/aiModel/MYfood.pt")
        food_detected = False
        for model in (model_non, model_my):
            results = model.predict(source=img_path)
            if results and len(results) > 0 and results[0].boxes is not None and len(results[0].boxes) > 0:
                food_detected = True
        return food_detected

    # Execution for Information evaluation
    food_detected = detect_food(image_path)
    ocr_text = perform_ocr(image_path)
    corrected_text = correct_pricing_errors(ocr_text)
    translated = translate_to_english(corrected_text)
    food_keywords, _, event_keywords = load_keywords()
    food_ing_keywords = load_food_ingredient_keywords()

    score = 0
    if food_detected:
        score += 2
    if check_category(translated, food_keywords) or check_category(translated, food_ing_keywords):
        score += 2
    if check_category(translated, event_keywords):
        score += 2
    if check_date(translated) or check_day(translated) or check_time(translated):
        score += 2
    if check_pricing(translated):
        score += 2
    return min(score, 10)

####################################
# Relational Evaluation Module
####################################
def run_relational(image_path):
    """
    Evaluate the relational aspect by detecting faces using YOLO and classifying emotions.
    Returns the relational score (capped at 10).
    """
    def load_models():
        face_detector = YOLO("/Users/timzz/CGI/django-backend/aiModel/face.pt")
        emotion_model = tf.keras.models.load_model("/Users/timzz/CGI/django-backend/aiModel/resnet50_emotion_model.h5")
        return face_detector, emotion_model

    def preprocess_face(face_img):
        face_resized = cv2.resize(face_img, (224, 224))
        face_array = img_to_array(face_resized)
        face_array = np.expand_dims(face_array, axis=0)
        return preprocess_input(face_array)

    def evaluate_score(emotions):
        positive = {"happy", "neutral", "surprise"}
        score = sum(1 + (2 if e in positive else 0) for e in emotions)
        return min(score, 10)

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image at {image_path}")
        return 0

    face_detector, emotion_model = load_models()
    results = face_detector(image)
    detection = results[0]
    if not hasattr(detection, "boxes") or detection.boxes is None or len(detection.boxes) == 0:
        return 0

    emotions = []
    for box in detection.boxes:
        coords = box.xyxy[0].tolist()  # [x1, y1, x2, y2]
        x1, y1, x2, y2 = map(int, coords)
        face_roi = image[y1:y2, x1:x2]
        if face_roi.size == 0:
            continue
        preprocessed = preprocess_face(face_roi)
        preds = emotion_model.predict(preprocessed)
        idx = int(np.argmax(preds[0]))
        labels = ['angry', 'happy', 'sad', 'surprise', 'neutral', 'fear', 'disgust']
        emotions.append(labels[idx])
    return evaluate_score(emotions)

####################################
# Remunerative Evaluation Module
####################################
def run_remunerative(image_path):
    """
    Evaluate the remunerative content by performing OCR (with translation) and
    checking for specific keywords and symbols. Returns the final score (capped at 10).
    """
    def perform_ocr(img_path):
        reader_ch = easyocr.Reader(['ch_sim', 'en'], gpu=False)
        reader_ms = easyocr.Reader(['ms', 'en'], gpu=False)
        results = reader_ch.readtext(img_path, detail=0) + reader_ms.readtext(img_path, detail=0)
        return " ".join(results)

    def translate_to_english(text):
        translator = Translator()
        try:
            return translator.translate(text, dest='en').text
        except Exception as e:
            print("Translation error:", e)
            return text

    def check_remunerative_elements(text):
        keywords = ["limited", "free", "only", "discount", "cashback", "share", "like"]
        found = {}
        for kw in keywords:
            if kw in text.lower():
                found[kw] = True
        if "%" in text:
            found["%"] = True
        if "~~" in text:
            found["strike_text"] = True
        return len(found) * 3, found

    ocr_text = perform_ocr(image_path)
    translated = translate_to_english(ocr_text)
    score, _ = check_remunerative_elements(translated)
    return min(score, 10)

####################################
# Main Combined Execution
####################################
def main(image_path):
    # Single hard-coded image path used by all modules
    # image_path = "/Users/timzz/CGI/django-backend/uploads/461277069_961375746033879_5393122898144942911_n.jpg"  # UPDATE with your actual image path

    info_score = run_information(image_path)
    rel_score = run_relational(image_path)
    rem_score = run_remunerative(image_path)
    ent_score = run_entertainment(image_path)

    # Output final scores in desired format
    print("\n=== Final Evaluation Scores ===")
    print(f"Information: {info_score}")
    print(f"Relational: {rel_score}")
    print(f"Remunerative: {rem_score}")
    print(f"Entertainment: {ent_score}")

    scores = {
        "Remunerative": rem_score,
        "Informative": info_score, 
        "Relational": rel_score,
        "Entertainment": ent_score
    }

    return scores



if __name__ == "__main__":
    main()
