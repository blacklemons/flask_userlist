![image-20210527112557137](https://user-images.githubusercontent.com/25717861/119756391-729f6d00-bede-11eb-94ba-7ce05968d862.png)
![image-20210527112717645](https://user-images.githubusercontent.com/25717861/119756443-8519a680-bede-11eb-8b9f-cd46ec2e7791.png)
## virtualenv 명령을 통해서 가상환경을 만든다.
virtualenv 설치
```powershell
pip install virtualenv
```
virtualenv 명령을 통해서 userlists 프로젝트 생성
```
virtualenv userlists
```
activate.bat 명령어를 통해 가상환경으로 들어간다.
```
Scripts\activate
```
##### flask 라이브러리 설치
```powershell
pip install flask 
```
파이썬 라이브러리 관리는 requirements.txt 를 통해서 관리한다.
requirements.txt  에 설치한 라이브러리를 쓴다.
```powershell
pip freeze > requirements.txt
```
requirements.txt 를 참조해서 라이브러리 설치하는 방법
```
pip install -r requirement.txt
```
서버를 http://localhost:5000 으로 서버를 띄우기 위해 app.py파일을 생성후 다음과 같이 추가한다.
```python
from flask import Flask
app = Flask(__name__)
app.debug = True
@app.route('/', methods=['GET' , 'POST'])
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run(port=5000)
```
![image-20210527144050912](https://user-images.githubusercontent.com/25717861/119772114-a5a32a00-bef9-11eb-9b0f-3f48f7e2c980.png)
위와 같은 결과를 확인할 수 있다.
#### render_template 를 활용해서 html파일을 랜더링한다.
index.html을 랜더링 하기 위해 
app.py를 다음과 같이 수정한다.
```python
from flask import Flask , render_template
app = Flask(__name__)
app.debug = True
@app.route('/', methods=['GET' , 'POST'])
def hello_world():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(port=5000)
```
templates/index.html 를 생성후 다음과 같은 코드를 추가한다.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```
### 레이아웃 파일 내에서 html 콘텐츠를 모두 입력 할 수 있습니다. layout.html 파일에는 특수 구문 {% block body %} 
###  {% endblock %}이 있습니다.
#### •   이 구문은 html 파일에서 파이썬 스크립트를 사용하는 데 도움이됩니다. {% block body %}를 시작 태그라고하고 {% endblock %}를 종료 태그라고합니다. 파이썬 스크립트는이 블록들 사이에 있습니다.
#### • layout.html 파일을 여러 페이지로 확장 할 수 있습니다. 
#### 공통으로 들어가는 코드는 layout.html에 넣은 후 다른 파일에서 상속받는데
layout.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gangnam Flask App</title>
</head>
<body>
   {% block body %}
   {% endblock %}
</body>
</html>
```
home.html을 다음과 같이 수정한다.
```html
{% extends 'layout.html' %} 
{% block body %} 
Hello world!!! 
{% endblock %}
```
네비게이션 메뉴을 만들기 위해서
includes/_navbar.html 파일 생성 후 다음과 같이 코드를 추가
```html
<nav class="navbar navbar-expand-lg navbar-light bg-warning">
    <a class="navbar-brand" href="/">Welcome my flask_web</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/about">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/articles">Articles</a>
        </li>
      </ul>
    </div>
  </nav>
```
네비게이션 메뉴가 모든 페이지에 보여지게 하기 위해서 layout.html에 include 한다.
layout.html 을 다음과 같이 수정한다.
```html
<html> 
<head> 
<title>Vasanth Flask App</title> 
<!-- CSS only -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
</head> 
<body> 
    {% include 'includes/_navbar.html'%}
    {% block body %}{% endblock %} 
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-Piv4xVNRyMGpqkS2by6br4gNJ7DXjqk09RmUpJ8jgGtD7zP9yug3goQfGII0yAns" crossorigin="anonymous"></script>
</body>
 </html> 
```
다음과 같은 페이지를 확인 할 수 있다.
![image-20210527165130348](https://user-images.githubusercontent.com/25717861/119787104-cf654c80-bf0b-11eb-8ecf-26e60987c2db.png)
url : http://localhost:5000/about 
method : GET
내용 : about.html 문서
app.py파일에 다음과 같은 코드를 추가한다.
```python
@app.route('/articles', methods=['GET' , 'POST'])
def articles():
    return render_template("articles.html"
```
templates/articles.html 생성후 다음과 같이 코드 추가
```html
{% extends 'layout.html' %} 
    {% block body %} 
    <div class="jumbotron">
        <h1 class="display-4">ARTICLES</h1>
        <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
        <hr class="my-4">
        <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
        <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
      </div>
    {% endblock %} 
```