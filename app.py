from flask import Flask, request, jsonify, render_template
import openai
import base64

app = Flask(__name__)

openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    video_data = data['video'].split(',')[1]
    video_bytes = base64.b64decode(video_data)

    # Gửi video đến OpenAI API để phân tích và nhận gợi ý làm đẹp
    response = openai.Video.create(
        file=video_bytes,
        purpose='beauty_suggestions'
    )

    suggestions = response['data']['suggestions']
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)