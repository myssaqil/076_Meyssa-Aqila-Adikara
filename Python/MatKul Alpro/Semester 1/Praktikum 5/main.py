from flask import Flask
from src.controllers import student_controller

app = Flask(__name__, template_folder='views')

studentCtrl = student_controller.StudentController

@app.route("/student")
def index():
    
    return studentCtrl.renderView()

if __name__ == "__main__":
    app.run(debug=True)



