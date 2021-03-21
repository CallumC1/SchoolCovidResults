import databasehandler
from datetime import datetime

# TEST AREA
connection = databasehandler.create_connection()
databasehandler.create_table(connection)
databasehandler.total_students_year_get(connection)

# TEST AREA

time_get = datetime.now()
time_now = time_get.strftime("%d-%m-%Y")


MENU_PROMPT = """
School Covid Reports
--------------------

1) Add new Result
2) Show All Students Results
3) Search for Students Results
4) Display all classes - TEMP
5) Exit Program

Your selection: """


def menu():
    connection = databasehandler.create_connection()
    databasehandler.create_table(connection)

    while (user_input := input(MENU_PROMPT)) != "5": # Continues to run the loop until user inputs "5"
        if user_input == "1":
            name = input("Enter students first and last name!\nYour Response: ").upper()
            result = input("Was their test Positive(P) or Negative(N)?\nYour Response: ").upper()
            while result != "P" and result != "N":
                result = input("Invalid Response!\nWas their test Positive(P) or Negative(N)?\nYour Response: ").upper()
            if result == "P":
                databasehandler.add_result(connection, name, result)
                result = "Positive"
                print(f"{result} result for {name} has been added into the database.")
            elif result == "N":
                databasehandler.add_result(connection, name, result)
                result = "Negative"
                print(f"{result} result for {name} has been added into the database.")

        elif user_input == "2":
            databasehandler.search_results_student_all(connection)

        elif user_input == "3":
            studentname = str(input("Which Student do you want to see the results for?\nStudents Full Name: ")).upper()
            databasehandler.search_results_student(connection, studentname)

        elif user_input == "4":
            print("Displaying all classes!")
            databasehandler.get_classes(connection)
        else:
            print("Invalid response! Try again!")


#menu()


# CLASS - NUM OF STUDENTS - TOTAL STUDENTS IN YEAR
# 7A - 25 |
# 7B - 23 | YEAR 7 | 67
# 7C - 19 |

# 8A - 29 |
# 8B - 22 | YEAR 8 | 81
# 8C - 30 |

# 9A - 12 | YEAR 9 | 39
# 9B - 27 |

# 10A - 28 |
# 10B - 31 | YEAR 10 | 84
# 10C - 25 |

# 11A - 20 |
# 11B - 25 | YEAR 11 | 75
# 11C - 30 |


# GET TOTAL STUDENTS FROM EACH YEAR