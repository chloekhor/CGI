import logging
import requests
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

GEMINI_API_KEY = "AIzaSyC4uAMKCk72MPNQl-oo_9mhM7TrbrjqFAo"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

def get_gemini_recommendation(evaluation_result, target_values):
    try:
        dimensions = ["Remunerative", "Informative", "Relational", "Entertainment"]
        improvement_suggestions = []
        adjustment_suggestions = []

        for i, dimension in enumerate(dimensions):
            target = target_values[i]
            result = evaluation_result.get(dimension, 0)

            if target == result:
                improvement_suggestions.append(f"✅ **{dimension}（{result}/{target}）: Target Achieved!** No further adjustments needed.")
            elif target > result:
                improvement_suggestions.append(f"⚠️ **{dimension}（{result}/{target}）: Below Target!** Needs improvement.")
                adjustment_suggestions.append(f"- **{dimension} Enhancement**: The current score is **{result}**, which is below the target **{target}**. Focus on optimizing this area to improve effectiveness.")
            else:
                improvement_suggestions.append(f"✅ **{dimension}（{result}/{target}）: Exceeds Target!** Consider balancing other factors.")

        prompt = f"""
        The user uploaded a food advertisement poster and set the target values:
        - **Target Values**: {target_values}
        - **AI Evaluation Scores**: {evaluation_result}

        **🎯 Comparative Analysis**
        {'\n'.join(improvement_suggestions)}

        **Suggested Adjustments:**
        {'\n'.join(adjustment_suggestions) if adjustment_suggestions else "All key aspects meet or exceed the target. No major adjustments needed."}

        ### **Required Response Format**
        You must structure your response using the following format:

        ---
        ## **Detailed Optimization Plan**
        ### **1. Remunerative (Profit-Driven Appeal)**
        **Target Score:** `{target_values[0]}`  
        **Current Score:** `{evaluation_result.get("Remunerative", 0)}`  
        **Assessment:** _(Indicate whether it meets or falls short of the target)_  
        **Recommended Improvements:** _(If needed, provide specific improvement actions)_  

        ### **2. Informative (Conveying Essential Product Information)**
        **Target Score:** `{target_values[1]}`  
        **Current Score:** `{evaluation_result.get("Informative", 0)}`  
        **Assessment:** _(Indicate whether it meets or falls short of the target)_  
        **Recommended Improvements:** _(If needed, provide specific improvement actions)_  

        ### **3. Relational (Emotional and Social Connection)**
        **Target Score:** `{target_values[2]}`  
        **Current Score:** `{evaluation_result.get("Relational", 0)}`  
        **Assessment:** _(Indicate whether it meets or falls short of the target)_  
        **Recommended Improvements:** _(If needed, provide specific improvement actions)_  

        ### **4. Entertainment (Engagement and Attention-Grabbing Appeal)**
        **Target Score:** `{target_values[3]}`  
        **Current Score:** `{evaluation_result.get("Entertainment", 0)}`  
        **Assessment:** _(Indicate whether it meets or falls short of the target)_  
        **Recommended Improvements:** _(If needed, provide specific improvement actions)_  

        ---
        ### **Summary**
        Provide a **summary paragraph** summarizing the key improvement areas based on the above analysis. The summary should be **concise and action-oriented**, highlighting the most important recommendations that will **enhance the advertisement’s effectiveness**. Avoid bullet points—write a structured paragraph.
        ---

        Ensure the response **strictly follows** this format.
        """

        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}

        response = requests.post(GEMINI_URL, headers=headers, json=data)
        response_json = response.json()

        if "candidates" in response_json:
            recommendation_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
            logger.info(f"Generated Recommendation: {recommendation_text}")
            return recommendation_text.strip()

        return "Error generating recommendation."

    except Exception as e:
        logger.error(f"Error generating recommendation: {e}")
        return "Error generating recommendation."
