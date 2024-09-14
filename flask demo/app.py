from flask import Flask ,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home(): 
    return render_template('index.html')
@app.route('/confirm',methods=['POST','GET'])
def register():
    if request.method=='POST':
        f=request.form.get('fname')
        l=request.form.get('lname')
        return render_template('confirm.html',fname=f,lname=l)

@app.route('/users/<fname>')
def users(fname):
    return "<h3>Welcome {}</h3>".format(fname)
if __name__ =="__main__":
    app.run(debug=True)
