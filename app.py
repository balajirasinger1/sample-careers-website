from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
  return "Hello"

if __name__ == '__main__':
  print("inside if")
  app.run(host='0.0.0.0',debug=True)