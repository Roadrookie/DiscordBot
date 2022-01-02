import sqlite3
import datetime
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_row(conn, row):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO deaths (name,deaths,updated)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, row)
    conn.commit()



def update_row(conn, name):
    try: 
        name = name.capitalize()

        sql = ''' UPDATE deaths SET deaths = ?, updated = ? WHERE name = ?'''

        cur = conn.cursor()
        deaths = get_deaths(conn, name)
        deaths += 1

        row = (deaths, datetime.datetime.now(), name)
        
        cur.execute(sql, row)
        conn.commit()
        
        return f'{name}\'s death count was updated to {deaths} in the DB'
        #return cur.lastrowid

    except:
        return "An error occurred"


def get_deaths(conn, name):

    sql = ''' SELECT deaths FROM deaths WHERE name = ?'''

    name = (name,)

    cur = conn.cursor()
    cur.execute(sql, name)
    conn.commit()

    rows = cur.fetchall()
    
    deaths = rows[0][0]

    return deaths

def scoreboard(conn):
    data = []

    sql = ''' SELECT * FROM deaths '''

    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        data.append(f'Player: {row[1]} | Deaths: {row[2]} | Last Death Reported: {row[3]}')

    return data


#def main():
#    database = "6ft_over.db"
#
#    #sql_create_table = """ CREATE TABLE IF NOT EXISTS deaths (
#    #                                    id integer PRIMARY KEY,
#   #                                    deaths int,
#    #                                    COD text,   
#    #                                    updated timestamp                                    
#    #                                ); """

    # create a database connection
    #conn = create_connection(database)

    #raw_name = 'frantz'
    #name = raw_name.capitalize()

    # create tables
    #if conn is not None:
        #data = ('Jake', 0, datetime.datetime.now())

        #create_row(conn, data)
        #print('Row was inserted')



        #data = (1, datetime.datetime.now(), 'Hector')

        #update_row(conn, data)
        #print('Updated the row')

    #    update_row(conn, name)


    #else:
    #    print("Error! cannot create the database connection.")

#main()