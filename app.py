from flask import Flask , render_template
from data import Articles

app = Flask(__name__)
app.debug = True
Articles = Articles()

@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<id>')
def article(id):
    if len(Articles)>=int(id):
        Article = Articles[int(id)-1]
        return render_template('article.html', article = Article)
    else :
        return render_template('article.html', article = "No DATA")

@app.route('/add_article')
def add_article():
    return render_template('add_article.html', articles = Articles)



if __name__== '__main__':
    app.run(port = 5000)