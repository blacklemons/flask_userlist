from flask import Flask , render_template
from data import Articles

app = Flask(__name__)
app.debug = True
Articles = Articles()

@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template('Home.html', name = "정호성")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

if __name__== '__main__':
    app.run(port = 5000)