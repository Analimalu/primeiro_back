#importar as bibliotecas 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

#criar nossa janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False,height=False) 
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/icon.ico")

#=== carregar imagens 
Logo = PhotoImage(file="icons/sandu.png.png")


#=== Widgets ==========

LeftFrame = Frame(jan,width=200,height=300,bg="#c5ebd0", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan,width=395,height=300,bg="#91c3d7", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=Logo, bg="#c5ebd0")
LogoLabel.place(x=0,y=40)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="#91c3d7", fg="white")
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame,width=30)
UserEntry.place(x=150,y=110)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="#91c3d7", fg="white")
PassLabel.place(x=5,y=150)

PassEntry = ttk.Entry(RightFrame,width=30,show="•")
PassEntry.place(x=150,y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBase.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login info", message="Acesso confirmado. Bem-vindo!")
    except:
        messagebox.showinfo(title="Login info", message="Acesso negado. Verifique se está cadastrado no sistema!")

#botões 
LoginButton = ttk.Button (RightFrame, text= "Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    #Removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="#91c3d7", fg="white")
    NomeLabel.place(x=5,y=5)

    NomeEntry = ttk.Entry(RightFrame,width=39)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="#91c3d7", fg="white")
    EmailLabel.place(x=5,y=55)

    EmailEntry = ttk.Entry(RightFrame,width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Não deixe nenhum campo vazio. Preencha todos os campos")
        else:
            DataBase.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """,(Name, Email, User, Pass))
            DataBase.conn.commit()
            messagebox.showinfo(title="Register info", message="Conta criada com sucesso")

    Register = ttk.Button (RightFrame, text= "Register", width=30,command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        #Removend widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo de volta os widgets de login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button (RightFrame, text= "Back", width=20, command=BackToLogin)
    Back.place(x=125,y=260)

RegisterButton = ttk.Button (RightFrame, text= "Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()

