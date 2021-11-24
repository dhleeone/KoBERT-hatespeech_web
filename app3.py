#	https://goldengate1.run.goorm.io/home
from flask import Flask, render_template, request, url_for, make_response
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
  result1 = "{0} {1}".format(s_m, g_m)
  result2 = p_m
  cnt=len(g_m)
  render= render_template('index2.html', result1 = result1, result2=result2, cnt=cnt)
  response.append(render)
  response.append({'result': 'SUCCESS'})

  return json.dumps(response)


if __name__ == "__main__":
    app.run(host = '0.0.0.0')
