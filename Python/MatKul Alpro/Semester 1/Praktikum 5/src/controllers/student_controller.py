import pandas
from flask import render_template

class StudentController:

    
    def __init__(self):
      
      pass

    @staticmethod
    def renderView():
        data = pandas.read_csv("././assets/students.csv")
       
        
        print('info : ',  data.info())
        print('dessc : ', data.describe())
        print('Data : ', data)
        data['Status'] = data['Grade'].apply(lambda x: 'Lulus' if x >= 80 else 'Tidak Lulus')
        data.to_csv('students_processed.csv',sep='|', index=False)
        gradeTotal = 0
        students = data.to_dict(orient='records')
        for student in students:
          gradeTotal += student['Grade']
        avg = gradeTotal/len(students)
        print("rata rata",avg)
        return render_template("index.html",students=students, avg = avg)