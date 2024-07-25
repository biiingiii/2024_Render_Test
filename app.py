from flask import Flask, render_template
app = Flask(__name__)
student_data = {
    1: {"name": "이예환", "score": {"국어": 90, "영어": 00, "수학": 100}},
    2: {"name": "이혜원", "score": {"국어": 75, "영어": 100, "수학": 75}}
}
@app.route('/')
def index():
    return render_template("index.html", 
            template_students = student_data)
@app.route("/student/<int:id>")
def student(id):
    return render_template("student.html", 
            template_name=student_data[id]["name"], 
            template_score=student_data[id]["score"])
if __name__ == '__main__':
    app.run(debug=True)
