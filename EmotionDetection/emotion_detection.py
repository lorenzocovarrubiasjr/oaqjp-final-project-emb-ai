import requests
import json

BERT_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

def emotion_detector(text_to_analyze):
    try:
        response = requests.post(BERT_URL, 
            headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
            json = {"raw_document": { "text": text_to_analyze }}
        )
        response.raise_for_status()

        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }

        formatted_resp = json.loads(response.text)
     
        emotion_scores = {
            "anger": formatted_resp["emotionPredictions"][0]["emotion"]["anger"],
            "disgust": formatted_resp["emotionPredictions"][0]["emotion"]["disgust"],
            "fear": formatted_resp["emotionPredictions"][0]["emotion"]["fear"],
            "joy": formatted_resp["emotionPredictions"][0]["emotion"]["joy"],
            "sadness": formatted_resp["emotionPredictions"][0]["emotion"]["sadness"]
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores["dominant_emotion"] = dominant_emotion
        return emotion_scores
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}

        