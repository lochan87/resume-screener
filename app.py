from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from resume_parser.parser import parse_resume

app = Flask(__name__, static_folder="frontend/static", template_folder="frontend/templates")
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    pdf_file = request.files['resume']
    parsed_data = parse_resume(pdf_file)

    return jsonify(parsed_data)

if __name__ == '__main__':
    app.run(debug=True)
