from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def Show():
    if request.method=='POST':
        return 'Hey There!'

@app.route('/Login',methods=["POST","GET"])
def login():
        if request.method=='POST':
                uname=request.form["Uname"]
                Password=request.form["Password"]
                if uname=='Admin' and Password=='1234':
                        return 'Success'
                else:
                        return 'Failure'

if __name__ == "__main__":
    app.run()