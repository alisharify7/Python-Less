import alphabet
import passGenerate 
from flask import Flask,render_template, request , redirect


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        passwd = request.form.get('password')
        if not passwd:
            answer = 'Please Full The box'
            return render_template('index.html',password=answer)    
        
        ans = passGenerate.gnt(passwd)
        return render_template('index.html',password = ans)

if __name__ == '__main__':
    app.run(debug=True)            