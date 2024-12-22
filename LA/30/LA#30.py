LA#30
import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter Widgets")
root.geometry("500x500")
root.configure(bg="orange")

frame = tk.Frame(root)
frame.pack(pady=20)


def display_text():
    print("My favorite anime is BLEACH!")

button = tk.Button(root, text="Run", command=display_text)
button.pack(pady=10)
root.mainloop()
