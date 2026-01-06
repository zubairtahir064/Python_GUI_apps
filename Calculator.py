import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Calculator")
root.resizable(False, False)

# ================= FUNCTIONS =================

def add_to_entry(value):
    entry.insert("end", value)

def clear_entry():
    entry.delete(0, "end")

def calculate():
    try:
        result = eval(entry.get())
        clear_entry()
        entry.insert(0, result)
    except:
        clear_entry()
        entry.insert(0, "Error")

def plus_minus():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(0, -value)
    except:
        pass

def percent():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(0, value / 100)
    except:
        pass

# ================= ENTRY =================

entry = ctk.CTkEntry(root, width=350, height=100, font=("Arial", 30), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# ================= BUTTON HELPER =================

def create_btn(text, row, col, cmd, w=70, span=1, color="#3e3e42", tcolor="white"):
    btn = ctk.CTkButton(
        root,
        text=text,
        width=w,
        height=70,
        fg_color=color,
        text_color=tcolor,
        font=("Comic Sans MS", 20, "bold"),
        corner_radius=15,
        command=cmd
    )
    btn.grid(row=row, column=col, columnspan=span, padx=5, pady=5)

# ================= BUTTONS =================

create_btn("CE", 1, 0, clear_entry, color="skyblue", tcolor="black")
create_btn("+/-", 1, 1, plus_minus, color="skyblue", tcolor="black")
create_btn("%", 1, 2, percent, color="skyblue", tcolor="black")
create_btn("/", 1, 3, lambda: add_to_entry("/"), color="skyblue", tcolor="black")

create_btn("7", 2, 0, lambda: add_to_entry("7"))
create_btn("8", 2, 1, lambda: add_to_entry("8"))
create_btn("9", 2, 2, lambda: add_to_entry("9"))
create_btn("*", 2, 3, lambda: add_to_entry("*"), color="skyblue", tcolor="black")

create_btn("4", 3, 0, lambda: add_to_entry("4"))
create_btn("5", 3, 1, lambda: add_to_entry("5"))
create_btn("6", 3, 2, lambda: add_to_entry("6"))
create_btn("-", 3, 3, lambda: add_to_entry("-"), color="skyblue", tcolor="black")

create_btn("1", 4, 0, lambda: add_to_entry("1"))
create_btn("2", 4, 1, lambda: add_to_entry("2"))
create_btn("3", 4, 2, lambda: add_to_entry("3"))
create_btn("+", 4, 3, lambda: add_to_entry("+"), color="skyblue", tcolor="black")

create_btn("0", 5, 0, lambda: add_to_entry("0"), w=150, span=2)
create_btn(".", 5, 2, lambda: add_to_entry("."))
create_btn("=", 5, 3, calculate, color="skyblue", tcolor="black")

root.mainloop()
