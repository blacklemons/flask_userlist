import re
from flask import Flask , render_template , redirect, request
from data import Articles
from passlib.hash import sha256_crypt
import pymysql


db = pymysql.connect(
            host='localhost', 
            user='root', 
            password='1234',
            db='gangnam',
            charset='utf8mb4')

cur = db.cursor()

app = Flask(__name__)
app.debug = True

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password = sha256_crypt.encrypt(password)

        sql = f"SELECT email FROM users WHERE email = '{email}'"

        cur.execute(sql)

        db.commit()
        user_email = cur.fetchone()
        if user_email==None:
            query = f"INSERT INTO users (name , email , username, password) VALUES ('{name}', '{email}', '{username}' , '{password}');"
            
            cur.execute(query)
            db.commit()
            return render_template('login.html')
        else:
            return redirect('/register')
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return "SUCCESS"
    else:
        return render_template('login.html')




@app.route('/', methods=['GET' , 'POST'])
def hello_world():
    return render_template('home.html' , name="김태경")

@app.route('/about', methods=['GET' , 'POST'])
def about():
    return render_template("about.html")

@app.route('/articles', methods=['GET' , 'POST'])
def articles():
    # articles = Articles()
    query = 'SELECT * FROM topic;'

    cur.execute(query)

    db.commit()

    articles = cur.fetchall()

    # print(data[0][2])
    return render_template("articles.html" , articles = articles )

@app.route('/article/<id>', methods=['GET' , 'POST'])
def article(id):
    # articles = Articles()
    query = f'SELECT * FROM topic WHERE id = {id};'

    cur.execute(query)

    db.commit()

    article = cur.fetchall()
    print(article)

    if article == None:
        return redirect('articles')
    else:
        return render_template("article.html" , article = article[0] )

    # print(len(articles))
    # if len(articles)>=int(id):
    #     article = articles[int(id)-1]
    #     return render_template('article.html', article = article)
    # else:
    #     return render_template('article.html', article = "NO DATA")

@app.route('/add_article', methods=['GET','POST'])
def add_article():
    if request.method =='POST':
        
        title = request.form["title"]
        description = request.form["description"]
        author = request.form["author"]

        print(title, description, author)

        query = "INSERT INTO `topic`(`title`,`description`, `author`) VALUES ( %s, %s, %s)"
        input_data = [title, description, author]
        # print(request.form['desc'])

        cur.execute(query, input_data)
        db.commit()
        print(cur.rowcount)
        return redirect("/articles")
    else:
        return render_template("add_article.html")


@app.route('/article/<id>/delete')
def delete_article(id):
    query = f"DELETE FROM `gangnam`.`topic` WHERE `id` = {id}"

    cur.execute(query)

    db.commit()

    return redirect('/articles')

@app.route('/article/<id>/edit', methods=['GET','POST'])
def edit_article(id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author = request.form['author']
        query = f'UPDATE `gangnam`.`topic` SET `title` = "{title}" ,`description` = "{description}", `author` = "{author}" WHERE id = "{id}"'
        cur.execute(query)
        db.commit()
        return redirect(f'/article/{id}')

    else:
        query = f'SELECT * FROM topic WHERE id = {id}'
        cur.execute(query)
        db.commit()
        article = cur.fetchone()
        return render_template("edit_article.html", article = article)

if __name__ == '__main__':
    app.run(port=5000)