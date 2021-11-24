#	https://goldengate1.run.goorm.io/home
from flask import Flask, render_template, request, url_for
from PIL import Image

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/popup')
def popup():
    return render_template('popup2.html')

@app.route('/result', methods=['POST', 'GET'])
def result_message():

  # img = Image.open('robot1.png')
  return render_template('index2.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0')