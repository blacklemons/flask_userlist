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