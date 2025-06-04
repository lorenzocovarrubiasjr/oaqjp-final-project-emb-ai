"""
This is the server.py module. Designed for emotionDetection.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Watson Emotion Detector")

@app.route("/emotionDetector")
def get_emotion_detection():
    """
    Emotion Detection functionality
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze == "":
        return "Input text missing! Please try again!"

    emotion_analysis = emotion_detector(text_to_analyze)

    if emotion_analysis['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement,
    the system response is 'anger': {emotion_analysis['anger']}, 
    'disgust': {emotion_analysis['disgust']}, 
    'fear': {emotion_analysis['fear']}, 
    'joy': {emotion_analysis['joy']} 
    and 'sadness': {emotion_analysis['sadness']}. 
    The dominant emotion is {emotion_analysis['dominant_emotion']}."""


@app.route("/")
def render_index_page():
    """
    Emotion Detection page rendering
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
