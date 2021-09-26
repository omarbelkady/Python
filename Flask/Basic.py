# Basic Flask App


from flask import Flask

app = Flask(__name__)

# I use the app.route decorator telling Flask this is the home page
@app.route("/")
def homePage():
    return "This is the home page y'all"

if(__name__=="__main__"):
    app.run(debug=True)
    