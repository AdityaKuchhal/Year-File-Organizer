import os
import shutil
import re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
import json

# File to store history
HISTORY_FILE = "history.json"

# Regex patterns for date formats (31-DEC-2024 and 24-12-31)
date_patterns = [
    (r'\d{2}-[A-Z]{3}-\d{4}', lambda match: match.group().split('-')[2]),  # Extract year from 31-DEC-2024
    (r'\d{2}-\d{2}-\d{2}', lambda match: handle_yy_mm_dd(match.group()))  # Extract year from 24-12-31
]


def handle_yy_mm_dd(date_str):
    """Handle yy-mm-dd format where the first two digits represent the year."""
    parts = date_str.split('-')
    yy = int(parts[0])  # Extract year from the first part of the date
    if yy < 100:  # Handle as a 21st-century year (2000 onwards)
        return f"20{yy:02d}"
    return str(yy)  # Return the year as-is for any valid full year


def extract_year_from_name(file_name):
    for pattern, year_extractor in date_patterns:
        match = re.search(pattern, file_name)
        if match:
            return year_extractor(match)
    return None


def save_history(folder_path):
    """Save the folder path to history."""
    history = load_history()
    if folder_path not in history:
        history.append(folder_path)
        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file)


def load_history():
    """Load the history of organized folders."""
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as file:
        return json.load(file)


def organize_files_by_year(target_folder, progress_callback=None):
    if not os.path.exists(target_folder):
        print(f"The folder '{target_folder}' does not exist.")
        return

    files = [file_name for file_name in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, file_name))]
    total_files = len(files)

    for index, file_name in enumerate(files):
        file_path = os.path.join(target_folder, file_name)

        # Extract year from file name
        year = extract_year_from_name(file_name)
        if year:
            # Create a folder for the year if it doesn't exist
            year_folder = os.path.join(target_folder, year)
            if not os.path.exists(year_folder):
                os.makedirs(year_folder)

            # Move the file into the corresponding year folder
            shutil.move(file_path, os.path.join(year_folder, file_name))
            print(f"Moved '{file_name}' to '{year_folder}'.")
        else:
            print(f"Skipped '{file_name}': No valid date found in the name.")

        # Update progress if callback is provided
        if progress_callback:
            progress_callback(index + 1, total_files)

    # Save folder to history
    save_history(target_folder)
    print("Files organized successfully.")


def browse_folder():
    folder_selected = filedialog.askdirectory(title="Select Folder to Organize")
    if folder_selected:
        try:
            def update_progress(current, total):
                progress_var.set((current / total) * 100)
                progress_bar.update()
                percentage_label.config(text=f"{int((current / total) * 100)}%")

            progress_var.set(0)
            progress_bar.update()
            percentage_label.config(text="0%")

            organize_files_by_year(folder_selected, update_progress)
            messagebox.showinfo("Success", "Files have been successfully organized by year!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


def show_history():
    """Display the history of organized folders."""
    history = load_history()
    if not history:
        messagebox.showinfo("History", "No history available.")
        return

    history_window = tk.Toplevel()
    history_window.title("History")
    history_window.geometry("400x300")

    tk.Label(history_window, text="Organized Folders History", font=("Helvetica", 14, "bold")).pack(pady=10)

    listbox = tk.Listbox(history_window, font=("Helvetica", 10))
    listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    for folder in history:
        listbox.insert(tk.END, folder)

    close_button = ttk.Button(history_window, text="Close", command=history_window.destroy)
    close_button.pack(pady=10)


def create_gui():
    root = tk.Tk()
    root.title("Organize Files by Year")
    root.geometry("500x400")
    root.resizable(False, False)

    # Set application icon
    icon_path = "icon.ico"  # Replace with the path to your .ico file
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
    else:
        print("Icon file not found. Using default icon.")

    # Apply ttk theme
    style = ttk.Style()
    style.theme_use("clam")

    # Header
    header = tk.Label(root, text="Organize Files by Year", font=("Helvetica", 16, "bold"))
    header.pack(pady=10)

    # Instructions
    instructions = tk.Label(root, text="Select a folder to organize files by year:", font=("Helvetica", 10))
    instructions.pack(pady=5)

    # Browse Button
    browse_button = ttk.Button(root, text="Browse Folder", command=browse_folder)
    browse_button.pack(pady=10)

    # History Button
    history_button = ttk.Button(root, text="View History", command=show_history)
    history_button.pack(pady=10)

    # Progress Bar
    global progress_var, progress_bar, percentage_label
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.pack(pady=10, fill=tk.X, padx=20)

    # Percentage Label
    percentage_label = tk.Label(root, text="0%", font=("Helvetica", 10))
    percentage_label.pack()

    # Exit Button
    exit_button = ttk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
