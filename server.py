'''
importing modules 
'''
from flask import Flask, request, render_template
from emotion_detector import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    '''
    default landing page route
    '''
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    '''
    sentiment analysis route
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_result

if __name__ == '__main__':
    app.run(debug=True, port=5000)
