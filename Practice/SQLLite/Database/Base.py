import sqlite3


# Simple sqllite database
class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def create(self, sql):
        self.cursor.execute(sql)
        print('Table has created')

    def execute(self, sql):
        self.cursor.execute(sql)
        print('Data has changed')

    def select(self, sql):
        self.cursor = self.cursor.execute(sql)
        print(self.cursor.fetchone())

    def drop(self, sql):
        self.cursor = self.cursor.execute(sql)
        print('Table has deleted')
#
#
if __name__ == '__main__':


    with DataBase('test.db') as db:
        db.create('CREATE TABLE COMPANY'
                    ' (ID INT PRIMARY KEY NOT NULL,'
                    ' NAME TEXT NOT NULL,'
                    ' AGE INT NOT NULL,'
                    ' ADDRESS CHAR(50),'
                    ' SALARY REAL);')
        db.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
        "VALUES (1, 'Paul', 32, 'California', 20000.00)")
        db.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
        "VALUES (2, 'Allen', 25, 'Texas', 15000.00)")
        db.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
        "VALUES (3, 'Teddy', 23, 'Norway', 20000.00)")
        db.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
        "VALUES (4, 'Mark', 25, 'Richmond', 65000.00)")
        db.select('SELECT id, name, address, salary from '
                    'COMPANY WHERE id = 1')
        db.drop('DROP TABLE COMPANY')



