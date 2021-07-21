from flask import flask

app= Flask (__name__)

@app.route('/')
def home():
 return 'index.html'

if __name__ == ''
      app.run()
