import tkinter as tk
from client.gui_app import Frame, menu_bar

def main():
    root = tk.Tk()
    root.title('Movies')
    root.iconbitmap('img/logo.ico')
    root.resizable(1, 1)

    menu_bar(root)

    app = Frame(root = root)

    app.mainloop()    

if __name__ == '__main__':
    main()