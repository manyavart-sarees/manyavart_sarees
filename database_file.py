import sqlite3
def connect_to_database():
 # connect=sqlite3.connect()
 # # cursor=connect.cursor("C:\Users\HP\Pictures\Saved Pictures\prerana\prerana_photos\B612")
  connect = sqlite3.connect("G\\Database1.db")
  cursor = connect.cursor()

  cursor.execute("CREATE TABLE IF NOT EXISTS USER_DETAILS(First_Name TEXT,last_Name TEXT,Email TEXT,Gender TEXT,Password TEXT)")

  return cursor, connect

def insert_to_user_details(Fname,Lname,Email,gender,password):
    cursor,connect=connect_to_database()
    if gender==0:
       gender="male"
    else:
        gender="female"
    cursor.execute(
         "INSERT INTO User_Details(First_Name,last_Name,Email,Gender,password) VALUES('"+str(Fname)+"','"+ str(Lname)+"','"+str(Email)+"','"+str(gender)+"','"+str(password)+"')")

    connect.commit()


def fetch_user_details(USERNAME,PASSWORD):
            cursor,connect=connect_to_database()
            cursor.execute(
                "SELECT * from User_Details WHERE First_Name='"+str(USERNAME) +"'AND Password ='"+PASSWORD+"'")

            connect.commit()
            if cursor.fetchone() is not None:
                s1 = 1
            else:
                s1 = 0
            return s1

