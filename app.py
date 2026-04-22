from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    name = "Priyanka"
    skills = ["Python", "Java", "SQL"]
    return render_template("index.html", name=name, skills=skills)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        print("Name:", username)
        print("Email:", email)
        print("Message:", message)

        return "Form Submitted Successfully!👍"
    
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)