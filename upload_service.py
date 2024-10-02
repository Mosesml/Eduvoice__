from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz  # PyMuPDF
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Ensure NLTK resources are available
nltk.download('punkt')

app = Flask(__name__)
CORS(app)

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):
        pdf_document = fitz.open(stream=file.read(), filetype='pdf')
        text = ''
        for page in pdf_document:
            text += page.get_text()

        return jsonify({'text': text})
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.route('/generate_notes', methods=['POST'])
def generate_notes():
    data = request.get_json()
    text = data.get('text', '')

    # Summarize the text using Sumy
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 10)  # Summarize to 10 sentences

    summary_text = " ".join([str(sentence) for sentence in summary])

    # Use SpaCy to extract key phrases
    doc = nlp(text)
    key_phrases = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) > 1]

    notes = f"Summary:\n{summary_text}\n\nKey Phrases:\n" + "\n".join(key_phrases)
    return jsonify({'notes': notes})

if __name__ == '__main__':
    app.run(debug=True, port=5005)  # Running on port 5005
