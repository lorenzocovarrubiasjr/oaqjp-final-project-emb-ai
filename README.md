# Watson Emotion Detector

A Flask web application that analyzes text input and detects emotions using Watson's emotion detection API.

## Overview

This application provides a web interface for emotion detection, analyzing text input and returning scores for five different emotions: anger, disgust, fear, joy, and sadness. The system also identifies the dominant emotion from the analysis.

## Features

- **Web Interface**: Simple HTML interface for text input and emotion analysis
- **REST API Endpoint**: Direct API access for programmatic use
- **Real-time Analysis**: Instant emotion detection results
- **Multi-emotion Detection**: Analyzes five core emotions simultaneously
- **Dominant Emotion Identification**: Highlights the strongest detected emotion

## Requirements

- Python 3.x
- Flask
- EmotionDetection module (custom module for Watson API integration)

## Installation

1. Clone or download the project files
2. Install required dependencies:
   ```bash
   pip install flask
   ```
3. Ensure the `EmotionDetection` module is in the same directory or Python path
4. Create an `index.html` template in a `templates/` folder

## Usage

### Starting the Server

Run the application:
```bash
python server.py
```

The server will start on `http://localhost:5000`

### Web Interface

1. Navigate to `http://localhost:5000` in your browser
2. Enter text in the provided interface
3. Submit to receive emotion analysis results

### API Endpoint

Make GET requests to the emotion detection endpoint:

```
GET /emotionDetector?textToAnalyze=YOUR_TEXT_HERE
```

**Example:**
```
http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20so%20happy%20today
```

**Response Format:**
```
For the given statement, the system response is 'anger': 0.1, 'disgust': 0.05, 'fear': 0.02, 'joy': 0.85 and 'sadness': 0.03. The dominant emotion is joy.
```

## API Response Details

The emotion detector returns scores for five emotions:
- **anger**: Intensity of anger detected (0.0 - 1.0)
- **disgust**: Intensity of disgust detected (0.0 - 1.0)
- **fear**: Intensity of fear detected (0.0 - 1.0)
- **joy**: Intensity of joy detected (0.0 - 1.0)
- **sadness**: Intensity of sadness detected (0.0 - 1.0)
- **dominant_emotion**: The emotion with the highest score

## Error Handling

The application handles two main error scenarios:

1. **Empty Input**: Returns "Input text missing! Please try again!"
2. **Invalid Text**: Returns "Invalid text! Please try again!" when the emotion detection API cannot process the input

## File Structure

```
project/
├── server.py              # Main Flask application
├── EmotionDetection.py    # Emotion detection module
└── templates/
    └── index.html         # Web interface template
```

## Configuration

- **Host**: `0.0.0.0` (accessible from any network interface)
- **Port**: `5000`
- **Debug Mode**: Disabled (production ready)

## Dependencies

- **Flask**: Web framework for the application
- **EmotionDetection**: Custom module that interfaces with Watson's emotion detection API

## Notes

- The application expects the `EmotionDetection` module to have an `emotion_detector()` function
- The emotion detector should return a dictionary with emotion scores and a dominant emotion field
- Ensure proper error handling in the `EmotionDetection` module for robust operation

## License

This project is designed for educational and demonstration purposes.