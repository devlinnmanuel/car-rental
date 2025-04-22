# from flask import Flask, render_template, request, redirect, url_for, session
# from database import SQL



# app = Flask(__name__)

# adminsD = {}
# membersD = {}
# adminL = []
# memberL = []
# cars_modelD = {}
# carsD = {}
# rentalsD = {}


# @app.route('/')
# def home():
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         role = request.form['role']  # Terima role dari JavaScript

#         if role == "admin":
#             dataD = adminsD
#         else:
#             dataD = membersD        

#         for id_user, datas in dataD.items():
#             if datas[1] == username and datas[2] == password:
#                 session['username'] = username
#                 session['role'] = role

#                 return redirect(url_for(f'{role}_homepage'))

#         return "Invalid credentials. <a href='/login'>Try again</a>"

#     return render_template('login_page.html')


# @app.route('/user_homepage', methods=['GET', 'POST'])
# def user_homepage():
#     if 'username' not in session or session['role'] != 'member':
#         return redirect(url_for('login'))
#     return render_template('user_homepage.html')


# @app.route('/admin_homepage', methods=['GET', 'POST'])
# def admin_homepage():
#     if 'username' not in session or session['role'] != 'admin':
#         return redirect(url_for('login'))
#     return render_template('admin_homepage.html')


# @app.route('/logout', methods=['GET', 'POST'])
# def logout():
#     session.pop('username', None)
#     session.pop('role', None)
#     return redirect(url_for('login'))


# if __name__ == "__main__":

#     db = SQL()
#     if db.connection:
#         users = db.get_all_users()
#         cars = db.get_all_cars()
#         cars_model = db.get_all_car_models()
#         rentals = db.get_all_rentals()

#         for user in users:
#             # {'ID_user': 1, 'name_user': 'Budi Santoso', 'email_user': 'budi@gmail.com', 'password_user': 'budi123', 'username_user': 'budi_s', 'role_user': 'member'}
#             role = user['role_user']
#             if role == "admin":
#                 adminsD['ID_user'] = [user['name_user'], user['username_user'], user['password_user'], user['email_user']]
#                 adminL.append(user['username_user'])
#             elif role == "member":
#                 membersD['ID_user'] = [user['name_user'], user['username_user'], user['password_user'], user['email_user']]
#                 memberL.append(user['username_user'])

#         for c_model in cars_model:
#             # {'ID_model': 1, 'brand_car': 'Toyota', 'year_manufactured': 2020, 'model_car': 'Avanza', 'price_car': Decimal('250000.00')}
#             cars_modelD['ID_model'] = [c_model['brand_car'], c_model['year_manufactured'], c_model['model_car'], c_model['price_car']]

#         for car in cars:
#             # {'ID_car': 1, 'model_id': 1, 'license_plate': 'B 1234 ABC', 'availability': 'available'}
#             carsD['ID_car'] = [car['model_id'], car['license_plate'], car['availability']]
        
#         for rental in rentals:
#             # {'ID_rental': 1, 'user_id': 1, 'car_id': 1, 'rental_date': datetime.date(2024, 3, 1), 'return_date': datetime.date(2024, 3, 5), 'approval_status': 'approved'}
#             rentalsD['ID_rental'] = [rental['user_id'], rental['car_id'], rental['rental_date'], rental['return_date'], rental['approval_status']]

#     else:
#         print("Gagal terhubung ke database.")

#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from database import SQL


# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# db = SQL()


# @app.route('/')
# def home():
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         users = db.get_all_users()
#         for user in users:
#             if user['username_user'] == username and user['password_user'] == password:
#                 session['user_id'] = user['ID_user']
#                 session['username'] = user['username_user']
#                 session['role'] = user['role_user']

#                 print(session['user_id'])
#                 print(session['username'])
#                 print(session['role'])
                
#                 if user['role_user'] == 'admin':
#                     return redirect(url_for('admin_homepage'))
#                 else:
#                     return redirect(url_for('user_homepage'))
        
#         # flash("Invalid username or password", "error")
#     return render_template('login_page.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         email = request.form['email']
#         username = request.form['username']
#         password = request.form['password']
        
#         db.create_user(fullname, email, password, username)
#         flash("Registration successful! Please log in.", "success")
#         return redirect(url_for('login'))
    
#     return render_template('register.html')

# @app.route('/user_homepage', methods=['POST'])
# def user_homepage():
#     # if 'user_id' not in session:
#     #     return redirect(url_for('login'))
    
#     cars = db.get_all_car_models()
#     return render_template('user_homepage.html', cars=cars)

# @app.route('/admin_homepage', methods=['POST'])
# def admin_homepage():
#     if 'user_id' not in session or session.get('role') != 'admin':
#         return redirect(url_for('login'))
    
#     rentals = db.get_all_rentals()
#     return render_template('admin_homepage.html', rentals=rentals)

# @app.route('/rent_car', methods=['POST'])
# def rent_car():
#     if 'user_id' not in session:
#         return redirect(url_for('login'))
    
#     car_id = request.form['car_id']
#     rental_date = request.form['rental_date']
#     return_date = request.form['return_date']
    
#     db.create_rental(session['user_id'], car_id, rental_date, return_date)
#     flash("Car rental request submitted! Waiting for approval.", "success")
#     return redirect(url_for('user_homepage'))

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     if db.connection:
#         app.run(debug=True)
#     else:
#         print("Gagal terhubung ke database.")


from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import SQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

app = Flask(__name__)
app.secret_key = "your_secret_key"
db = SQL()

adminsD = {}
membersD = {}
adminL = []
memberL = []
cars_modelD = {}
carsD = {}
rentalsD = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')  # Ambil role dari form

        # print("\n=== Data yang diterima dari form ===")
        # print(f"Username: {username}")
        # print(f"Password: {password}")
        # print(f"Role: {role}")
        # print("===================================\n")

        if role == "admin":
            dataD = adminsD
        else:
            dataD = membersD        

        # print(f"Dict: {dataD}")

        for id_user, datas in dataD.items():
            # print(f"user: {datas}")
            if datas[1] == username and datas[2] == password:
                session['username'] = username
                session['role'] = role
                session['user_id'] = id_user

                # print(f"isi session: {session}")

                if role == 'admin':
                    # print(f"masuk ke admin homepage:")
                    return redirect(url_for('admin_homepage'))
                else:
                    # print(f"masuk ke user homepage:")
                    return redirect(url_for('user_homepage'))
        
        flash("Invalid username or password", "error")
    return render_template('login_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not fullname or not email or not username or not password:
            flash("All fields are required", "error")
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        db.create_user(fullname, email, hashed_password, username)
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/user_homepage', methods=['GET', 'POST'])
def user_homepage():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    id_user = session['user_id']
    
    cars_model = db.get_all_car_models()    
    cars = db.get_all_cars()
    rentals = db.get_all_rentals()

    member_cars = []
    
    for rental in rentals:
        if rental['user_id'] == id_user:  # Filter hanya untuk user_id tertentu
            car_id = rental['car_id']
            car = next((c for c in cars if c['ID_car'] == car_id), None)
            
            if car:
                model_id = car['model_id']
                car_model = next((m for m in cars_model if m['ID_model'] == model_id), None)
                
                if car_model:
                    rental_info = {
                        'rental_id': rental['ID_rental'],
                        'rental_date': rental['rental_date'].strftime("%d/%m/%Y"),
                        'return_date': rental['return_date'].strftime("%d/%m/%Y"),
                        'approval_status': rental['approval_status'],
                        'car_info': {
                            'license_plate': car['license_plate'],
                            'availability': car['availability'],
                            'brand': car_model['brand_car'],
                            'model': car_model['model_car'],
                            'year': car_model['year_manufactured'],
                            'price': str(car_model['price_car']), 
                            'image': car_model['image_car']
                        }
                    }
                    
                    member_cars.append(rental_info)

        print(f"{member_cars}")

    return render_template('user_homepage.html', cars=member_cars)

@app.route('/admin_homepage', methods=['GET', 'POST'])
def admin_homepage():
    if 'user_id' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    rentals = db.get_all_rentals()
    return render_template('admin_homepage.html', rentals=rentals)

@app.route('/rent_car', methods=['POST'])
def rent_car():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    car_id = request.form.get('car_id')
    rental_date = request.form.get('rental_date')
    return_date = request.form.get('return_date')
    
    if not car_id or not rental_date or not return_date:
        flash("All fields are required", "error")
        return redirect(url_for('user_homepage'))
    
    db.create_rental(session['user_id'], car_id, rental_date, return_date)
    flash("Car rental request submitted! Waiting for approval.", "success")
    return redirect(url_for('user_homepage'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    if db.connection:
        users = db.get_all_users()
        cars = db.get_all_cars()
        cars_model = db.get_all_car_models()
        rentals = db.get_all_rentals()

        for user in users:
            # {'ID_user': 1, 'name_user': 'Budi Santoso', 'email_user': 'budi@gmail.com', 'password_user': 'budi123', 'username_user': 'budi_s', 'role_user': 'member'}
            role = user['role_user']
            if role == "admin":
                adminsD[user['ID_user']] = [user['name_user'], user['username_user'], user['password_user'], user['email_user']]
                adminL.append(user['username_user'])
            elif role == "member":
                membersD[user['ID_user']] = [user['name_user'], user['username_user'], user['password_user'], user['email_user']]
                memberL.append(user['username_user'])

        for c_model in cars_model:
            # {'ID_model': 1, 'brand_car': 'Toyota', 'year_manufactured': 2020, 'model_car': 'Avanza', 'price_car': Decimal('250000.00')}
            cars_modelD[c_model['ID_model']] = [c_model['brand_car'], c_model['year_manufactured'], c_model['model_car'], c_model['price_car'], c_model['image_car']]

        for car in cars:
            # {'ID_car': 1, 'model_id': 1, 'license_plate': 'B 1234 ABC', 'availability': 'available'}
            carsD[car['ID_car']] = [car['model_id'], car['license_plate'], car['availability']]
        
        for rental in rentals:
            # {'ID_rental': 1, 'user_id': 1, 'car_id': 1, 'rental_date': datetime.date(2024, 3, 1), 'return_date': datetime.date(2024, 3, 5), 'approval_status': 'approved'}
            rentalsD[rental['ID_rental']] = [rental['user_id'], rental['car_id'], rental['rental_date'], rental['return_date'], rental['approval_status']]

        app.run(debug=True)
    else:
        print("Gagal terhubung ke database.")