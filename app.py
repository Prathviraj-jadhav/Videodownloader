from flask import Flask, render_template, request, session  
from pytube import YouTube


app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
       session['link'] = request.form.get('url') 
    
    try :
      url = YouTube(session['link'])
      url.check_availability
    except :
        return render_template('error.html')
        return render_template('download.html')
    return render_template('home.html')   


@app.route("/download", methods = ["GET", "POST"])
def download():
     pass
     
    
     if __name__ == '__main__':
      app.run(debug= True)
