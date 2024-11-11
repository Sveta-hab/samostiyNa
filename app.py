from flask import Flask, jsonify, render_template
import pandas as pd
import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)

app = Flask(__name__)

# Завантажуємо дані з CSV
data = pd.read_csv('clustered_universities.csv')

@app.route('/universities', methods=['GET'])
def universities():
    # Перетворюємо дані у формат JSON
    return jsonify(data.to_dict(orient='records'))

@app.route('/')
def index():
    # Повертаємо HTML-сторінку
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
