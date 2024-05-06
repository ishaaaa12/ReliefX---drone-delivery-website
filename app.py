from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def Home():
    return render_template("Home.html")
@app.route('/Services')
def Services():
    return render_template("Services.html")
@app.route('/About')
def About():
    return render_template("About.html")
@app.route('/Medicines')
def medicine():
    return render_template("medicine.html")
@app.route('/Groceries')
def grocery():
    return render_template("grocery.html")
@app.route('/Login')
def login():
    return render_template("login.html")
@app.route('/Register')
def register():
    return render_template("register.html")
@app.route('/Support')
def support():
    return render_template("support.html")
@app.route('/Contact')
def contact():
    return render_template("contact.html")

if __name__=="main":
    app.run(debug=True,port=5000)
