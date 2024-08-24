from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Hello World from Azure App Service!'

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
