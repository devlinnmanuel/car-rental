import mysql.connector

class SQL:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="DevSQL265Man**",
                database="students"
            )
            print("Connection to database is successful")
            return self.connection

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query runs successfully")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()

    def fetch_data(self, query, data=None):
        cursor = self.connection.cursor(dictionary=True)
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        
        finally:
            cursor.close()

    # Bagian CRUD student:
    def create_student(self, nim, nama, tgl_lahir):
        query = """
        INSERT INTO student(nim, nama, tgl_lahir)
        VALUES
        (%s, %s, %s)
        """
        data = (nim, nama, tgl_lahir,)
        self.execute_query(query, data)

    def get_all_students(self):
        query = "SELECT * FROM student"
        return self.fetch_data(query)
    
    def get_all_nim(self):
        query = "SELECT nim FROM student"
        return self.fetch_data(query)

    def update_student(self, student_id, nim, nama, tgl_lahir):
        query = """
        UPDATE student
        SET nim = %s,
            nama = %s,
            tgl_lahir = %s
        WHERE id = %s
        """
        data = (nim, nama, tgl_lahir, student_id,)
        self.execute_query(query, data)

    def delete_student(self, student_id):
        query = "DELETE FROM student WHERE id = %s"
        data = (student_id,)
        self.execute_query(query, data)