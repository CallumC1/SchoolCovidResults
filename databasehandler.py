# -----------------------------------------------------------------------------------------------------------------
# Transfering some code over regularly, if you edit anything in these files, just put a comment by it or say in discord
# -----------------------------------------------------------------------------------------------------------------
import sqlite3
from sqlite3 import Error
from datetime import datetime

time_get = datetime.now()
time_now_mins = time_get.strftime("%d-%m-%Y %H:%M")
time_now_date = time_get.strftime("%d-%m-%Y")

# SQLite queries
CREATE_TABLE_RESULTS = "CREATE TABLE IF NOT EXISTS studentResults (id INTEGER PRIMARY KEY, date TEXT, name TEXT, results TEXT);"
CREATE_TABLE_CLASSES = "CREATE TABLE IF NOT EXISTS classes (class TEXT, numStudents TEXT);"
ADD_RESULT = "INSERT INTO studentResults (date, name, results) VALUES (?, ?, ?);"
SEARCH_RESULTS = ";"
SEARCH_CLASSES = ";"
SEARCH_RESULTS_STUDENT = "SELECT ? FROM studentResults;"


# Attempts to connect to the SQLite database.
def create_connection():
    try:
        print(f"Successfully secured database connection at date: {time_now_mins}!")
        return sqlite3.connect("covidresults.db")
    except Error as e:
        print(f"(!) An error has occurred whilst connecting to the SQLite Database: {e}")


# Creates the covidresults.db SQLite files if it does not already exist
def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE_RESULTS)
        connection.execute(CREATE_TABLE_CLASSES)


# Adds a Students name, result and time added into the database.
def add_result(connection, name, results):
    with connection:
        connection.execute(ADD_RESULT, (time_now_date, name, results))


# Removes the formatting from the database.
def refine_results(rowVar):
    refinedrow = str(rowVar).replace(",", '').replace("(", '').replace(")", '').replace("'", '')
    if refinedrow[-1] == "N":
        print(refinedrow[:-1] + "Negative")
    elif refinedrow[-1] == "P":
        print(refinedrow[:-1] + "Positive")
    else:
        print("An error has occurred!... Skipping Data.")


# Get the results of every test.
def search_results_student_all(connection):
    with connection:
        print("ID |  DATE  | STUDENT NAME | RESULT")
        for row in connection.execute("SELECT * FROM studentResults"):
            refine_results(row)


# Search the database by a students full name
def search_results_student(connection, studentname):
    with connection:
        print("ID |  DATE  | STUDENT NAME | RESULT")
        for row in connection.execute("SELECT * FROM studentResults WHERE name=?", (studentname,)):
            refine_results(row)


def total_students_get(connection):  # GETS TOTAL STUDENT COUNT
    with connection:
        cur = connection.cursor()
        total_students = 0
        for row in cur.execute("SELECT numStudents FROM classes"):
            total_students += int(row[0])
        return print(f"Total Students = {total_students}")


def total_students_year_get(connection):
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM classes")
        classes_array = cur.fetchall()
        print(classes_array)  # DEBUG CODE
        compressed_years = set()
        # Compresses all tutor groups into their one year.
        for i in range(0, len(classes_array)):
            if (classes_array[i][0][1]).isnumeric():  # Checks for a second digit
                number = classes_array[i][0][0] + classes_array[i][0][1]  # Adds the 2 digits to get the double digit number
            else:
                number = classes_array[i][0][0]  # Single digit
            if number not in compressed_years:
                compressed_years.add(number)
                print(compressed_years)
        print(compressed_years)

# GOT ALL CLASSES YEARS INTO 1 NOW NEED TO GET NUM IN EACH YEAR ^u^


def get_classes(connection):
    with connection: 
        cur = connection.cursor()
        cur.execute("SELECT * FROM classes")
        classes_array = cur.fetchall()  # GETS THE CLASS INFORMATION IN FORM OF AN ARRAY
        print(classes_array)
        print(classes_array[1][1])
        total_students_get(connection)

# ISSUES
# Can not detect double diget numbers.
# E.g. 10, 11


# 5 Days a week, 5 Periods a day.
# 25 periods total to work with.
# Max of 20 students can be tested in 1 period.
# TOTAL STUDENTS / 25?
# TOTAL PERIODS NEEDED WITHOUT SPLITTING YEARS: 14
