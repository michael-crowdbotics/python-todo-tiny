import sqlite3 as sqlite


class Database:
    def __init__(self):
        self.db = None

    def connect_to_db(self):
        try:
            self.db = sqlite.connect("todo.db")
            c = self.db.cursor()
            c.execute(
                "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task VARCHAR(255) NOT NULL, date VARCHAR(50) NOT NULL)"
            )
            print("Database connected and table ensured.")
        except sqlite.DatabaseError as e:
            print("Error: Database not found")
            print(e)

    def read_db(self):
        """Read data from database."""
        c = self.db.cursor()
        c.execute("SELECT task, date FROM tasks")
        rows = c.fetchall()
        print(f"Read from database: {rows}")
        return rows

    def insert_db(self, values):
        """Insert new task into database."""
        c = self.db.cursor()
        c.execute("INSERT INTO tasks (task, date) VALUES (?, ?)", values)
        self.db.commit()
        print(f"Inserted into database: {values}")

    def delete_db(self, value):
        """Delete task from database."""
        c = self.db.cursor()
        c.execute("DELETE FROM tasks WHERE task=?", value)
        self.db.commit()
        print(f"Deleted from database: {value}")

    def update_db(self, value):
        """Update task in database."""
        c = self.db.cursor()
        c.execute("UPDATE tasks SET task=? WHERE task=?", value)
        self.db.commit()
        print(f"Updated in database: {value}")

    def close_db(self):
        """Close connection to database."""
        if self.db:
            self.db.close()
            print("Database connection closed.")
