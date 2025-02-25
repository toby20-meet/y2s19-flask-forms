from databases import *
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add',methods = ['GET','POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('add.html')
	if request.method == 'POST':
		print("Received POST request!")
		name = request.form['student_name']
		year = request.form['student_year']
		add_student(name,year,)
		return render_template('add.html')

@app.route('/delete/<int:student_id>',methods = ['POST'])
def what_do_i_call_this(student_id):
	delete_student_id(student_id)
	return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)
