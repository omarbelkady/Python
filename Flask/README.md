## Flask

- Framework that provides me with libraries to build lightweight web apps

#### Installation using pip

```python
pip install flask
```

#### Run Method in flask has 4 parameters

1. host: specify the host you want to run your Flask app on (default: 127.0.0.1 i.e. Localhost)

2. port: specify the port number where you wish to run your Flask app on (default: 5000)

3. debug: boolean value telling Flask whether you want debugging information to be provided to you(default: false)

4. options: information which you want to be forwarded to the server


#### Routing In Flask

```python
from flask import Flask
app = Flask(__name__)

@app.route("/home")
def home():
    return("This is the home page on my WS")

@app.route("/about")
def about():
    return("This is the about page on my WS")

@app.route("/services")
def services():
    return("This is the services page on my WS")

@app.route("/contact")
def about():
    return("This is the contact us page on my WS")


if(__name__=="__main__"):
    app.run(debug=True)
```