LA#29
import tkinter as tk

your_name = "Gelo Borcena"
your_section = "BSIT-2A"
root = tk.Tk()
root.title(f"OOP LA29 {your_name} {your_section}")
root.geometry("400x300")
root.configure(bg="blue")

name = tk.Label(font=100, text=(f"OOP LA29 {your_name} {your_section}"))
name.grid(row=0, column=0, padx=100, pady=120)

root.mainloop()
