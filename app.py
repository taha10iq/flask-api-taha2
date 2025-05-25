from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from PIL import Image
import io

app = Flask(__name__)
genai.configure(api_key="AIzaSyCw8Civc1Sk7OvPxfhLdXSUUCBbgxxi2FY")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('message')
    image_file = request.files.get('image')

    try:
        if image_file:
            img = Image.open(image_file.stream)
            response = model.generate_content([user_input, img] if user_input else [img])
        else:
            response = model.generate_content(user_input)

        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        return jsonify({"reply": f"❌ خطأ: {str(e)}"})

if __name__ == '__main__':
    app.run(host='192.168.0.133', port=2500, debug=True)
