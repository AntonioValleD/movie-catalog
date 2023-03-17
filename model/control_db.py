from .connection_db import ConnectionDB
from tkinter import messagebox

def create_table():
    connection = ConnectionDB()

    sql = '''
    CREATE TABLE movies(
        id_movie INTEGER,
        name VARCHAR(50),
        duration VARCHAR(20),
        genre VARCHAR(50),
        PRIMARY KEY(id_movie AUTOINCREMENT)
    )
    '''

    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        title = 'Create table'
        message = 'Table created successfully!'
        messagebox.showinfo(title, message)
    except:
        title = 'Create table'
        message = 'Table already exists'
        messagebox.showerror(title, message)


def delete_table():
    connection = ConnectionDB()

    sql = 'DROP TABLE movies'

    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        title = 'Delete table'
        message = 'Table deleted successfully!'
        messagebox.showinfo(title, message)
    except:
        title = 'Delete table'
        message = 'Table does not exist'
        messagebox.showerror(title, message)


class Movie:
    def __init__(self, name, duration, genre):
        self.id_movie = None
        self.name = name
        self.duration = duration
        self.genre = genre
    
    def __str__(self):
        return f'Movie[{self.name}, {self.duration}, {self.genre}]'


def save(movie):
    connection = ConnectionDB()

    sql = f"""INSERT INTO movies (name, duration, genre)
    VALUES('{movie.name}', '{movie.duration}', '{movie.genre}')"""

    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        title = 'Save'
        message = 'Information saved successfully!'
        messagebox.showinfo(title, message)
    except:
        title = 'Save'
        message = 'Information was not saved\nTable does not exist'
        messagebox.showerror(title, message)


def list():
    connection = ConnectionDB()

    movie_list = []
    sql = 'SELECT * FROM movies'

    try:
        connection.cursor.execute(sql)
        movie_list = connection.cursor.fetchall()
        connection.close_connection()
    except:
        title = 'Recover data'
        message = 'Data was not recovered\nTable does not exist'
        messagebox.showerror(title, message)

    return movie_list


def edit(movie, id_movie):
    connection = ConnectionDB()

    sql = f"""UPDATE movies
    SET name = '{movie.name}', duration = '{movie.duration}', genre = '{movie.genre}'
    WHERE id_movie = {id_movie} 
    """

    try:
        connection.cursor.execute(sql)
        connection.close_connection()
    except:
        title = 'Edit'
        message = 'Information can not be edited'
        messagebox.showerror(title, message)


def delete(id_movie):
    connection = ConnectionDB()

    sql = f'DELETE FROM movies WHERE id_movie = {id_movie}'

    try:
        connection.cursor.execute(sql)
        connection.close_connection()
    except:
        title = 'Delete'
        message = 'Information can not be Deleted'
        messagebox.showerror(title, message)