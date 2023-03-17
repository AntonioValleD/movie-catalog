import tkinter as tk
from tkinter import ttk, messagebox
from model.control_db import Movie, create_table, delete_table, save, edit, delete, list

def menu_bar(root):
    menu_bar = tk.Menu(root)
    root.config(menu = menu_bar, width = 300, height = 300)
    
    home_menu = tk.Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(label = 'Home', menu = home_menu)
    home_menu.add_command(label = 'Create table in DB', command = create_table)
    home_menu.add_command(label = 'Delete table from DB', command = delete_table)
    home_menu.add_command(label = 'Exit', command = root.destroy)

    menu_bar.add_cascade(label = 'Queries')

    menu_bar.add_cascade(label = 'Settings')

    menu_bar.add_cascade(label = 'Help')


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 600, height = 600)
        self.root = root
        self.pack()

        self.movie_fields()
        self.disable_fields()
        self.movie_table()

        self.id_movie = None

    def movie_fields(self):
        # Labels
        self.label_name = tk.Label(self, text = 'Name')
        self.label_name.config(font = ('Arial', 12, 'bold'))
        self.label_name.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.label_duration = tk.Label(self, text = 'Duration')
        self.label_duration.config(font = ('Arial', 12, 'bold'))
        self.label_duration.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.label_genre = tk.Label(self, text = 'Genre')
        self.label_genre.config(font = ('Arial', 12, 'bold'))
        self.label_genre.grid(row = 2, column = 0, padx = 10, pady = 10)


        # Entrys
        self.var_name = tk.StringVar()
        self.entry_name = tk.Entry(self, textvariable = self.var_name)
        self.entry_name.config(font = ('Arial', 11), width = 50)
        self.entry_name.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.var_duration = tk.StringVar()
        self.entry_duration = tk.Entry(self, textvariable = self.var_duration)
        self.entry_duration.config(font = ('Arial', 11), width = 50)
        self.entry_duration.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.var_genre = tk.StringVar()
        self.entry_genre = tk.Entry(self, textvariable = self.var_genre)
        self.entry_genre.config(font = ('Arial', 11), width = 50)
        self.entry_genre.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2)


        # Buttons
        self.button_new = tk.Button(self, text = 'New', command = self.enable_fields)
        self.button_new.config(font = ('Arial', 12, 'bold'), width = 15, fg = 'white',
                                    activebackground = 'light green')
        self.button_new.grid(row = 3, column = 0, padx = 10, pady = 10)

        self.button_save = tk.Button(self, text = 'Save', command = self.save_fields)
        self.button_save.config(font = ('Arial', 12, 'bold'), width = 15, fg = 'white',
                                    activebackground = 'light blue')
        self.button_save.grid(row = 3, column = 1, padx = 10, pady = 10)

        self.button_cancel = tk.Button(self, text = 'Cancel', command = self.disable_fields)
        self.button_cancel.config(font = ('Arial', 12, 'bold'), width = 15, fg = 'white',
                                    activebackground = '#F1948A')
        self.button_cancel.grid(row = 3, column = 2, padx = 10, pady = 10)

        self.button_edit = tk.Button(self, text = 'Edit', command = self.edit_data)
        self.button_edit.config(font = ('Arial', 12, 'bold'), width = 15, fg = 'white', bg = 'blue',
                                    activebackground = 'light blue', cursor = 'hand2')
        self.button_edit.grid(row = 5, column = 0, padx = 10, pady = 10)

        self.button_delete = tk.Button(self, text = 'Delete', command = self.delete_data)
        self.button_delete.config(font = ('Arial', 12, 'bold'), width = 15, fg = 'white', bg = 'red',
                                    activebackground = '#F1948A', cursor = 'hand2')
        self.button_delete.grid(row = 5, column = 1, padx = 10, pady = 10)


    def enable_fields(self):
        self.entry_name.config(state = 'normal')
        self.entry_duration.config(state = 'normal')
        self.entry_genre.config(state = 'normal')

        self.var_name.set('')
        self.var_duration.set('')
        self.var_genre.set('')

        self.button_new.config(state = 'disabled', bg = 'light green', cursor = '')
        self.button_save.config(state = 'normal', bg = 'blue', cursor = 'hand2')
        self.button_cancel.config(state = 'normal', bg = 'red', cursor = 'hand2')

    
    def disable_fields(self):
        self.id_movie = None
        self.entry_name.config(state = 'disabled')
        self.entry_duration.config(state = 'disabled')
        self.entry_genre.config(state = 'disabled')

        self.var_name.set('')
        self.var_duration.set('')
        self.var_genre.set('')

        self.button_new.config(state = 'normal', bg = 'green', cursor = 'hand2')
        self.button_save.config(state = 'disabled', bg = 'light blue', cursor = '')
        self.button_cancel.config(state = 'disabled', bg = '#F98884', cursor = '')


    def save_fields(self):
        movie = Movie(
            self.var_name.get(),
            self.var_duration.get(),
            self.var_genre.get()
        )

        if self.id_movie == None:
            save(movie)
        else:
            edit(movie, self.id_movie)

        self.movie_table()
        self.disable_fields()


    def edit_data(self):
        try:
            self.id_movie = self.table.item(self.table.selection())['text']
            self.movie_name = self.table.item(self.table.selection())['values'][0]
            self.movie_duration = self.table.item(self.table.selection())['values'][1]
            self.movie_genre = self.table.item(self.table.selection())['values'][2]

            self.enable_fields()

            self.entry_name.insert(0, self.movie_name)
            self.entry_duration.insert(0, self.movie_duration)
            self.entry_genre.insert(0, self.movie_genre)
        except:
            title = 'Edit'
            message = 'Information can not be edited\nNo register has been selected'
            messagebox.showerror(title, message)


    def delete_data(self):
        try:
            self.id_movie = self.table.item(self.table.selection())['text']
            delete(self.id_movie)
            self.movie_table()
            self.id_movie = None
        except:
            title = 'Delete'
            message = 'Information can not be deleted\nNo register has been selected'
            messagebox.showerror(title, message)


    def movie_table(self):
        self.movie_list = list()
        self.movie_list.reverse()

        # Table
        self.table = ttk.Treeview(self, column = ('Name', 'Duration', 'Genre'))
        self.table.grid(row = 4, column = 0, padx = 5, pady = 5, columnspan = 4, sticky = 'nse')

        # Scrollbar
        self.scroll = ttk.Scrollbar(self, orient = 'vertical', command = self.table.yview)
        self.scroll.grid(row = 4, column = 4, sticky = 'nse')
        self.table.configure(yscrollcommand = self.scroll.set)
        
        # Fields
        self.table.heading('#0', text = 'ID')
        self.table.heading('#1', text = 'Name')
        self.table.heading('#2', text = 'Duration')
        self.table.heading('#3', text = 'Genre')

        # Insert information in table
        for p in self.movie_list:
            self.table.insert('', 0, text = p[0], values = (p[1], p[2], p[3]))