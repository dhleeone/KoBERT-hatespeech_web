#	https://goldengate1.run.goorm.io/home
from flask import Flask, render_template, request, url_for
from PIL import Image
import model
import slangword
import purify

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result_message():
  text = request.form['user_mes']
  g_m = model.mespredict(text)
  s_m = slangword.slang(text)
  p_m = purify.purifier(text)
    
  result1 = s_m
  result2 = g_m
  result3 = p_m
    
  cnt=len(g_m)
  return render_template('index2.html', result1 = result1, result2=result2, result3=result3, cnt=cnt)


if __name__ == "__main__":
    app.run(host = '0.0.0.0')
