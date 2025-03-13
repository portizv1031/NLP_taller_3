import os
from flask import Flask, request, render_template
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

# Carga el modelo una sola vez
model_name = "Helsinki-NLP/opus-mt-es-en"  # Traducir de español a inglés
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('text', '')

    if not text.strip():
        return render_template('index.html', error="Por favor ingresa un texto para traducir.")

    # Traducción
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

    return render_template('result.html', original_text=text, translated_text=translated_text)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  
    app.run(host='0.0.0.0', port=port)
