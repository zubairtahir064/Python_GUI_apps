# ========================= IMPORTS =========================
import customtkinter as ctk
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ========================= APP SETUP =========================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("1200x700")
root.title("Advanced Hospital Management System")

# ========================= VARIABLES =========================
fields = [
    "nameoftablet","ref","dose","nooftablets","lot","issuedate",
    "expdate","storage","nhsnumber","patientname","dob","address"
]

vars = {f: ctk.StringVar() for f in fields}

# ========================= DATABASE =========================
def create_db():
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS hospital (
        nameoftablet TEXT, ref TEXT PRIMARY KEY, dose TEXT,
        nooftablets TEXT, lot TEXT, issuedate TEXT,
        expdate TEXT, storage TEXT, nhsnumber TEXT,
        patientname TEXT, dob TEXT, address TEXT
    )
    """)
    conn.commit()
    conn.close()

create_db()

# ========================= FUNCTIONS =========================
def add_data():
    try:
        conn = sqlite3.connect("hospital.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO hospital VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    tuple(v.get() for v in vars.values()))
        conn.commit()
        conn.close()
        fetch_data()
        reset_data()
        messagebox.showinfo("Success","Record Added")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def fetch_data():
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hospital")
    rows = cur.fetchall()
    table.delete(*table.get_children())
    for r in rows:
        table.insert("", "end", values=r)
    conn.close()


def reset_data():
    for v in vars.values():
        v.set("")


def delete_data():
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM hospital WHERE ref=?", (vars["ref"].get(),))
    conn.commit()
    conn.close()
    fetch_data()


def update_data():
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("""
    UPDATE hospital SET nameoftablet=?, dose=?, nooftablets=?, lot=?, issuedate=?,
    expdate=?, storage=?, nhsnumber=?, patientname=?, dob=?, address=?
    WHERE ref=?
    """, (
        vars["nameoftablet"].get(), vars["dose"].get(), vars["nooftablets"].get(),
        vars["lot"].get(), vars["issuedate"].get(), vars["expdate"].get(),
        vars["storage"].get(), vars["nhsnumber"].get(), vars["patientname"].get(),
        vars["dob"].get(), vars["address"].get(), vars["ref"].get()
    ))
    conn.commit()
    conn.close()
    fetch_data()

# ========================= SEARCH =========================
def search_data():
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hospital WHERE patientname LIKE ?", ('%' + search_var.get() + '%',))
    rows = cur.fetchall()
    table.delete(*table.get_children())
    for r in rows:
        table.insert("", "end", values=r)
    conn.close()

# ========================= PDF =========================
def generate_pdf():
    doc = SimpleDocTemplate("prescription.pdf")
    styles = getSampleStyleSheet()
    content = []
    for k,v in vars.items():
        content.append(Paragraph(f"{k}: {v.get()}", styles['Normal']))
    doc.build(content)
    messagebox.showinfo("PDF","Prescription Saved")

# ========================= ANALYTICS =========================
def show_analytics():
    conn = sqlite3.connect("hospital.db")
    df = pd.read_sql_query("SELECT * FROM hospital", conn)
    conn.close()

    if df.empty:
        messagebox.showinfo("Analytics","No Data Available")
        return

    total = len(df)
    unique_patients = df['patientname'].nunique()

    messagebox.showinfo("Analytics",
                        f"Total Records: {total}\nUnique Patients: {unique_patients}")

# ========================= UI =========================
frame = ctk.CTkFrame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Form
for i,f in enumerate(fields):
    ctk.CTkLabel(frame, text=f).grid(row=i, column=0, sticky="w")
    ctk.CTkEntry(frame, textvariable=vars[f], width=200).grid(row=i, column=1)

# Buttons
btn_frame = ctk.CTkFrame(frame)
btn_frame.grid(row=0, column=2, rowspan=10, padx=20)

ctk.CTkButton(btn_frame, text="Add", command=add_data).pack(pady=5)
ctk.CTkButton(btn_frame, text="Update", command=update_data).pack(pady=5)
ctk.CTkButton(btn_frame, text="Delete", command=delete_data).pack(pady=5)
ctk.CTkButton(btn_frame, text="Reset", command=reset_data).pack(pady=5)
ctk.CTkButton(btn_frame, text="PDF", command=generate_pdf).pack(pady=5)
ctk.CTkButton(btn_frame, text="Analytics", command=show_analytics).pack(pady=5)

# Search
search_var = ctk.StringVar()
ctk.CTkEntry(frame, textvariable=search_var).grid(row=12, column=0)
ctk.CTkButton(frame, text="Search", command=search_data).grid(row=12, column=1)

# Table
table = ttk.Treeview(root, columns=fields, show='headings')
for f in fields:
    table.heading(f, text=f)
    table.column(f, width=100)

table.pack(fill="both", expand=True)

# Click event
def get_cursor(event):
    item = table.focus()
    values = table.item(item, 'values')
    for i,f in enumerate(fields):
        vars[f].set(values[i])

table.bind("<ButtonRelease-1>", get_cursor)

fetch_data()

root.mainloop()