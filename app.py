from flask import Flask, render_template, request, url_for

app = Flask(__name__)
            

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods = ["GET"])
def greet():
    if request.method == "GET":
        name = request.args.get("name", "world")
        return render_template("greet.html", name = name)
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template('test.html')

# @app.route("/view", methods = ["GET"])
# def view():
#     

#     print(requested_file)
#     

#     content = "This is the content of the file"
    
#     return render_template("view.html", content = content)


@app.route("/view_file", methods = ["GET"])
def view_file():
    requested_file = request.args.get("file_name")
    try:
        with open(f"{requested_file}.txt", "r") as file:
            content = file.read()
    except:
        content = "No such File"
    return render_template("view_file.html", content = content)