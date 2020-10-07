import sqlite3

DB_PATH = 'quiz_collection.db'   # Update accordingly
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_quiz_to_list(quiz):
    try:
        conn = sqlite3.connect(DB_PATH)



        # Once a connection has been established, we use the cursor
        # Object to execute queries
        c = conn.cursor()

        # Keep the initla status as Not Started
        c.execute('insert into quizzes(quiz, status) values(?,?)',(quiz,NOTSTARTED))

        # We commit to save the change
        conn.commit()

        return {"quiz": quiz,"status":NOTSTARTED}
    except Exception as e:
        print('Error: ',e)
        return None

def get_all_quizzes():
    try:
        conn=sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from quizzes')
        rows= c.fetchall()
        return {"count": len(rows),
                "quizzes" : rows}
    except Exception as e:
        print('Error: ',e)
        return None

def get_quiz(quiz):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select status from quizzes where quiz='%s'" % quiz)
        status = c.fetchone()[0]
        return status
    except Exception as e:
        print('Error: ',e)
        return None