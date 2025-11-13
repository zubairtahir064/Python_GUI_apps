from tkinter import *
from tkinter import filedialog, ttk, messagebox
import requests
import os

class Downloader:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("555x344")
        self.window.title("Downloader Created by Zubair")

        # URL input
        self.url_label = Label(text="Enter URL:")
        self.url_label.pack()
        self.url_entry = Entry(width=60)
        self.url_entry.pack(pady=5)

        # File save path
        self.path_label = Label(text="Save file as:")
        self.path_label.pack()
        self.path_entry = Entry(width=60)
        self.path_entry.pack(pady=5)

        self.browse_button = Button(text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.download_button = Button(text="Download", command=self.download)
        self.download_button.pack(pady=10)

        self.progress_bar = ttk.Progressbar(
            self.window, orient="horizontal", maximum=100, length=400, mode="determinate"
        )
        self.progress_bar.pack(pady=10)

        self.window.mainloop()

    def browse_file(self):
        filename = filedialog.asksaveasfilename(defaultextension="", title="Save As")
        if filename:
            self.path_entry.delete(0, END)
            self.path_entry.insert(0, filename)

    def download(self):
        url = self.url_entry.get().strip()
        file_path = self.path_entry.get().strip()

        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return
        if not file_path:
            messagebox.showerror("Error", "Please choose where to save the file.")
            return

        try:
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get("content-length", 0))
            block_size = 1024
            self.progress_bar["value"] = 0

            with open(file_path, "wb") as f:
                downloaded = 0
                for data in response.iter_content(block_size):
                    f.write(data)
                    downloaded += len(data)
                    percent = (downloaded / total_size) * 100 if total_size else 0
                    self.progress_bar["value"] = percent
                    self.window.update_idletasks()

            messagebox.showinfo("Success", "Download completed successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Download failed:\n{e}")

Downloader()
