import tkinter as tk
from tkinter import messagebox
import json
import matplotlib.pyplot as plt

candidates = {}

def add_candidate():
    name = entry_candidate_name.get()
    if name:
        if name not in candidates:
            candidates[name] = 0
            listbox_candidates.insert(tk.END, name)
            entry_candidate_name.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"Candidate '{name}' already exists.")
    else:
        messagebox.showerror("Error", "Candidate name cannot be empty.")

def cast_vote():
    selected_candidate = listbox_candidates.get(tk.ACTIVE)
    if selected_candidate:
        candidates[selected_candidate] += 1
        messagebox.showinfo("Vote Cast", f"Vote cast for '{selected_candidate}'.")
    else:
        messagebox.showerror("Error", "No candidate selected.")

def display_results():
    results = "\n".join([f"{name}: {votes} votes" for name, votes in candidates.items()])
    messagebox.showinfo("Results", results)

def save_results():
    filename = entry_filename.get()
    if not filename:
        filename = "results.json"
    with open(filename, 'w') as file:
        json.dump(candidates, file)
    messagebox.showinfo("Save Results", f"Results saved to {filename}.")

def load_results():
    global candidates
    filename = entry_filename.get()
    if not filename:
        filename = "results.json"
    try:
        with open(filename, 'r') as file:
            candidates = json.load(file)
        listbox_candidates.delete(0, tk.END)
        for name in candidates:
            listbox_candidates.insert(tk.END, name)
        messagebox.showinfo("Load Results", f"Results loaded from {filename}.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"No file named {filename} found.")

def visualize_results():
    if candidates:
        names = list(candidates.keys())
        votes = list(candidates.values())
        plt.bar(names, votes, color='skyblue')
        plt.xlabel('Candidates')
        plt.ylabel('Votes')
        plt.title('Election Results')
        plt.show()
    else:
        messagebox.showerror("Error", "No candidates available to visualize.")

# Setting up the GUI
root = tk.Tk()
root.title("Voting System")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_candidate_name = tk.Label(frame, text="Candidate Name:")
label_candidate_name.grid(row=0, column=0, padx=5, pady=5)
entry_candidate_name = tk.Entry(frame)
entry_candidate_name.grid(row=0, column=1, padx=5, pady=5)
button_add_candidate = tk.Button(frame, text="Add Candidate", command=add_candidate)
button_add_candidate.grid(row=0, column=2, padx=5, pady=5)

listbox_candidates = tk.Listbox(frame)
listbox_candidates.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

button_cast_vote = tk.Button(frame, text="Cast Vote", command=cast_vote)
button_cast_vote.grid(row=2, column=0, padx=5, pady=5)
button_display_results = tk.Button(frame, text="Display Results", command=display_results)
button_display_results.grid(row=2, column=1, padx=5, pady=5)
button_visualize_results = tk.Button(frame, text="Visualize Results", command=visualize_results)
button_visualize_results.grid(row=2, column=2, padx=5, pady=5)

label_filename = tk.Label(frame, text="Filename:")
label_filename.grid(row=3, column=0, padx=5, pady=5)
entry_filename = tk.Entry(frame)
entry_filename.grid(row=3, column=1, padx=5, pady=5)
button_save_results = tk.Button(frame, text="Save Results", command=save_results)
button_save_results.grid(row=4, column=0, padx=5, pady=5)
button_load_results = tk.Button(frame, text="Load Results", command=load_results)
button_load_results.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
