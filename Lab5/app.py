from flask import Flask, render_template, request, redirect, url_for
from database import SQL

app = Flask(__name__)
db = SQL()


@app.route('/')
def home():
    students_list = []
    # [{'id': 1, 'nim': '12345', 'nama': 'Budi', 'tgl_lahir': '2005-03-21'}, ...

    students_db = db.get_all_students()
    for student in students_db:
        students = {}
        students['id'] = student['id']
        students['nim'] = student['nim']
        students['nama'] = student['nama']
        students['tgl_lahir'] = student['tgl_lahir'].strftime('%Y-%m-%d')

        students_list.append(students)
    
    return render_template('index.html', students=students_list)


# create student:
@app.route('/add-student', methods=['POST'])
def add_student():
    nim = request.form.get('NIM')
    nama = request.form.get('NAMA')
    tgl_lahir = request.form.get('TGL-LAHIR')

    # kalau form ada yang kosong:
    if not nim or not nama or not tgl_lahir:
        print("Form tidak lengkap")
        return redirect(url_for('home'))

    available_nims = db.get_all_nim()
    for nims in available_nims:
        if nim == nims['nim']:
            print("NIM sudah dipakai.")
            return redirect(url_for('home'))

    db.create_student(nim, nama, tgl_lahir)
    print("student berhasil ditambah ke database.")
    return redirect(url_for('home'))


# update student
@app.route('/update-student/<int:student_id>/<string:nim>/<string:nama>/<string:tgl_lahir>')
def update_student(student_id, nim, nama, tgl_lahir):
    #proses update ke database:
    if not nim or not nama or not tgl_lahir:
        print("Form tidak lengkap")
        return redirect(url_for('home'))
    
    # print(student_id, nim, nama, tgl_lahir)

    db.update_student(student_id, nim, nama, tgl_lahir)
    print("Student berhasil diupdate!")
    return redirect(url_for('home'))


# delete student:
@app.route('/delete-student/<int:student_id>')
def delete_student(student_id):
    # proses delete dari database:
    db.delete_student(student_id)
    print("student telah dihapus!")

    return redirect(url_for('home'))


if __name__ == "__main__":
    if db.connection:
        app.run(debug=True)
    else:
        print("Gagal terhubung ke database.")