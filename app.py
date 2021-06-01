from flask import Flask , render_template , redirect, request, session
from data import Articles
from passlib.hash import sha256_crypt
import pymysql
from functools import wraps


db = pymysql.connect(
            host='localhost', 
            user='root', 
            password='1234',
            db='gangnam',
            charset='utf8mb4')

cur = db.cursor()

app = Flask(__name__)
app.debug = True

def is_loged_in(f):
    @wraps(f)
    def _wraps(*args,**kwargs):
        if 'is_loged' in session:
            print(session)
            return f(*args,**kwargs)
        else:
            return redirect('/login')
    return _wraps

def is_admined(e):
    @wraps(e)
    def _wraps(*args,**kwargs):
        if session['username'] == 'admin':
            print(session, "admin")
            return e(*args,**kwargs)
        else:
            print(session['username'], "NO")
            return redirect('/login')
    return _wraps    

@app.route('/admin/<id>/edit', methods=['GET','POST'])
@is_admined
@is_loged_in
def edit_user(id):
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        query = f'UPDATE `gangnam`.`users` SET `name` = "{name}" ,`username` = "{username}" WHERE id = "{id}"'
        cur.execute(query)
        db.commit()
        return redirect(f'/admin')
    else:
        query = f'SELECT * FROM users WHERE id = {id}'
        cur.execute(query)
        db.commit()
        user = cur.fetchone()
        return render_template("edit_users.html", user = user)

@app.route('/admin/<id>/delete')
@is_admined
@is_loged_in
def delete_user(id):
    query = f"DELETE FROM `gangnam`.`users` WHERE `id` = {id}"

    cur.execute(query)

    db.commit()

    return redirect('/admin')        

@app.route('/admin', methods=['GET','POST'])
@is_admined
@is_loged_in
def admin():
    query = 'SELECT *FROM users'
    cur.execute(query)
    db.commit()
    users = cur.fetchall()
    return render_template('/admin.html', users = users)

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
        query = f"SELECT * FROM users WHERE email = '{email}';"
        cur.execute(query)
        db.commit()
        user = cur.fetchone()
        # print(user)                 # 없으면 None 있으면 Tuple
        if user == None:
            return redirect('login')
        else:
            if sha256_crypt.verify(password, user[4]):
                session['is_loged']=True
                session['username']=user[3]
                session['email']=user[2]
                print(session)
                return redirect('/')
            else :
                return redirect('/login')
    else:
        return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')

@app.route('/', methods=['GET' , 'POST'])
def hello_world():
    return render_template('home.html' , name="김태경")

@app.route('/about', methods=['GET' , 'POST'])
@is_loged_in
def about():
    print(session['username'])
    return render_template("about.html")



@app.route('/articles', methods=['GET' , 'POST'])
@is_loged_in
def articles():
    query = 'SELECT * FROM topic;'

    cur.execute(query)

    db.commit()

    articles = cur.fetchall()

    return render_template("articles.html" , articles = articles )


@app.route('/article/<id>', methods=['GET' , 'POST'])
@is_loged_in
def article(id):
    query = f'SELECT * FROM topic WHERE id = {id};'

    cur.execute(query)

    db.commit()

    article = cur.fetchall()
    print(article)

    if article == None:
        return redirect('articles')
    else:
        return render_template("article.html" , article = article[0] )

@app.route('/add_article', methods=['GET','POST'])
def add_article():
    if request.method =='POST':
        
        title = request.form["title"]
        description = request.form["description"]
        author = request.form["author"]

        print(title, description, author)

        query = "INSERT INTO `topic`(`title`,`description`, `author`) VALUES ( %s, %s, %s)"
        input_data = [title, description, author]

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
    app.secret_key = 'gangnamStyle'
    app.run(port=5000)