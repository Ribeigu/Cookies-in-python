from flask import Flask, make_response, request, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    saved_name=request.cookies.get("saved_name")
    return render_template("index.html", saved_name=saved_name) #this will render the html template with the value present on saved name

@app.route("/save_name", methods=["POST"])
def save_name():
    name=request.form['name']

    response= make_response(f"We will now remembrer your name, {name}!")
    response.set_cookie("saved_name", name)

    return response  #response is the first line created on the function

@app.route("/delete_cookie")
def delete_cookie():
    response = make_response("We will no longer remember your name!")
    response.set_cookie("saved_name", "", expires=0)

    return response  #response is the first line created on the function

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=9999)