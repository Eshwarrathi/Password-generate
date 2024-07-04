import tkinter as tk
from tkinter import*
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x650")
        self.root.title("Password Generator")

        self.bg_color = "#f4f4f4"

        self.create_password_generation_form()

    def create_password_generation_form(self):
        form_frame = tk.Frame(self.root, bg=self.bg_color,pady=2).pack(fill=X)

        title = tk.Label(form_frame, text="Password Generator", font=("time new roman", 16, "bold"), bg=self.bg_color, fg="#00308F",pady=2).pack(fill=X)

        self.username_var = tk.StringVar()
        self.length_var = tk.IntVar()
        self.result_var = tk.StringVar()

        lbl_username = tk.Label(form_frame, text="Enter User Name:", font=("time new roman", 15, "bold"), bg=self.bg_color, fg="#555")
        lbl_username.place(x=30,y=70)
        txt_username = tk.Entry(form_frame, textvariable=self.username_var, font=("time new roman", 15), bd=5, relief=tk.GROOVE)
        txt_username.place(x=270,y=70)

        lbl_length = tk.Label(form_frame, text="Enter Password Length:", font=("time new roman", 15, "bold"), bg=self.bg_color, fg="#555")
        lbl_length.place(x=10,y=120)
        txt_length = tk.Entry(form_frame, textvariable=self.length_var, font=("time new roman", 15,"bold"), bd=5, relief=tk.GROOVE)
        txt_length.place(x=270,y=120)

        lbl_result = tk.Label(form_frame, text="Generated Password:", font=("time new roman", 15, "bold"), bg=self.bg_color, fg="#555")
        lbl_result.place(x=10,y=170)
        txt_result = tk.Entry(form_frame, textvariable=self.result_var, font=("time new roman", 15, "bold"), bd=5, relief=tk.GROOVE, state='readonly')
        txt_result.place(x=270,y=170)


        button_frame = tk.Frame(form_frame, bg=self.bg_color)
        button_frame.place(x=200,y=230)
        
        btn_generate = tk.Button(button_frame, text="Generate Password", font=("Helvetica", 20, "bold"), bg="#074463", fg="white", bd=5, relief=tk.RAISED, command=self.generate_password).grid(row=0,column=0,padx=0,pady=5)

        btn_accept = tk.Button(button_frame, text="Accept", font=("Helvetica", 20, "bold"), fg="#00308F", relief=tk.RAISED, command=self.accept_password)
        btn_accept.grid(row=1, column=0, pady=5)

        btn_reset = tk.Button(button_frame, text="Reset", font=("Helvetica", 20, "bold"), fg="#00308F", relief=tk.RAISED, command=self.reset_form)
        btn_reset.grid(row=2, column=0, pady=5)

    def generate_password(self):
        try:
            length = self.length_var.get()
            if length < 1:
                raise ValueError("Password length must be at least 1")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            self.result_var.set(password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def accept_password(self):
        username = self.username_var.get()
        password = self.result_var.get()
        if username and password:
            messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror("Error", "Please generate a password first")

    def reset_form(self):
        self.username_var.set("")
        self.length_var.set(0)
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
