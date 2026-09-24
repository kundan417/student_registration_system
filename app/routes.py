from flask import Blueprint, render_template, request, redirect, url_for,flash
from app.forms import StudentRegistrationForm
from app.models import Student,db

main = Blueprint("main",__name__)

@main.route("/",methods=["GET","POST"])
def home():
    form = StudentRegistrationForm()
    if form.validate_on_submit(): # if request.method == "POST" and form.validate()

        student = Student(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            course=form.course.data,
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for("main.students")) # PRG -> POST -> Redirect -> GET
        
    return render_template("register.html",form=form)

@main.route("/students")
def students():
    all_students = Student.query.all()

    return render_template("students.html", students=all_students)

@main.route("/edit/<int:student_id>",methods=["GET","POST"])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    form = StudentRegistrationForm(obt=student)

    if form.validate_on_submit():
        student.name = form.name.data
        student.email = form.email.data
        student.age = form.age.data
        student.course = form.course.data

        db.session.commit()

        flash(
            "Student updated successfully",
            "success"
        )

        return redirect(url_for("main.students"))

    return render_template("edit_student.html",form=form)

@main.route("/delete/<int:student_id>")
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)

    db.session.delete(student)
    db.session.commit()

    flash(
        "Student deleted successfully",
        "success"
    )

    return redirect(url_for('main.students'))

