import tkinter as tk
from tkinter import messagebox
import random

# ── colours ──────────────────────────────────────────
BG       = "#0f0f1a"
CARD     = "#1a1a2e"
ACCENT   = "#e94560"
ACCENT2  = "#0f3460"
TEXT     = "#eaeaea"
SUBTEXT  = "#a0a0b0"
GREEN    = "#00e676"
YELLOW   = "#ffd600"

root = tk.Tk()
root.title("🚀 Cool Dashboard")
root.geometry("500x600")
root.configure(bg=BG)
root.resizable(False, False)

# ── header ────────────────────────────────────────────
header = tk.Frame(root, bg=ACCENT2, pady=15)
header.pack(fill="x")

tk.Label(header, text="🚀 My Dashboard", font=("Helvetica", 22, "bold"),
         bg=ACCENT2, fg=TEXT).pack()
tk.Label(header, text="Welcome, Ahmad!", font=("Helvetica", 11),
         bg=ACCENT2, fg=SUBTEXT).pack()

# ── stat cards ────────────────────────────────────────
cards_frame = tk.Frame(root, bg=BG, pady=15)
cards_frame.pack(fill="x", padx=20)

def make_card(parent, emoji, title, value, color):
    card = tk.Frame(parent, bg=CARD, padx=15, pady=15,
                    relief="flat", bd=0)
    card.pack(side="left", expand=True, fill="both", padx=6)
    tk.Label(card, text=emoji, font=("Helvetica", 24),
             bg=CARD, fg=color).pack()
    tk.Label(card, text=value, font=("Helvetica", 20, "bold"),
             bg=CARD, fg=color).pack()
    tk.Label(card, text=title, font=("Helvetica", 9),
             bg=CARD, fg=SUBTEXT).pack()

make_card(cards_frame, "⚡", "Tasks",   "24",   ACCENT)
make_card(cards_frame, "✅", "Done",    "18",   GREEN)
make_card(cards_frame, "⏳", "Pending", "6",    YELLOW)

# ── random number generator ───────────────────────────
rng_frame = tk.Frame(root, bg=CARD, pady=20, padx=20)
rng_frame.pack(fill="x", padx=20, pady=10)

tk.Label(rng_frame, text="🎲 Random Number Generator",
         font=("Helvetica", 13, "bold"), bg=CARD, fg=TEXT).pack()

rng_label = tk.Label(rng_frame, text="???",
                     font=("Helvetica", 40, "bold"), bg=CARD, fg=ACCENT)
rng_label.pack(pady=8)

def generate():
    num = random.randint(1, 100)
    rng_label.config(text=str(num))
    color = GREEN if num > 50 else ACCENT
    rng_label.config(fg=color)

tk.Button(rng_frame, text="  Generate!  ", font=("Helvetica", 12, "bold"),
          bg=ACCENT, fg=TEXT, relief="flat", cursor="hand2",
          command=generate, pady=6).pack()

# ── to-do list ────────────────────────────────────────
todo_frame = tk.Frame(root, bg=CARD, pady=15, padx=20)
todo_frame.pack(fill="x", padx=20, pady=10)

tk.Label(todo_frame, text="📝 Quick To-Do",
         font=("Helvetica", 13, "bold"), bg=CARD, fg=TEXT).pack(anchor="w")

entry_row = tk.Frame(todo_frame, bg=CARD)
entry_row.pack(fill="x", pady=8)

entry = tk.Entry(entry_row, font=("Helvetica", 11), bg="#2a2a3e",
                 fg=TEXT, insertbackground=TEXT, relief="flat",
                 bd=8)
entry.pack(side="left", fill="x", expand=True)

listbox = tk.Listbox(todo_frame, font=("Helvetica", 11), bg="#2a2a3e",
                     fg=TEXT, selectbackground=ACCENT, relief="flat",
                     height=4, bd=0)
listbox.pack(fill="x", pady=4)

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert("end", f"  ☐  {task}")
        entry.delete(0, "end")
    else:
        messagebox.showwarning("Oops", "Please type a task first!")

def done_task():
    try:
        idx = listbox.curselection()[0]
        task = listbox.get(idx).replace("☐", "☑")
        listbox.delete(idx)
        listbox.insert(idx, task)
        listbox.itemconfig(idx, fg=GREEN)
    except IndexError:
        messagebox.showinfo("Hint", "Click a task first to mark it done!")

btn_row = tk.Frame(todo_frame, bg=CARD)
btn_row.pack(fill="x")

tk.Button(btn_row, text="➕ Add", font=("Helvetica", 10, "bold"),
          bg=ACCENT2, fg=TEXT, relief="flat", cursor="hand2",
          command=add_task, padx=10, pady=4).pack(side="left", padx=(0,6))

tk.Button(btn_row, text="✅ Done", font=("Helvetica", 10, "bold"),
          bg=GREEN, fg=BG, relief="flat", cursor="hand2",
          command=done_task, padx=10, pady=4).pack(side="left")

# ── footer ────────────────────────────────────────────
tk.Label(root, text="Built with Python & Tkinter  ♥",
         font=("Helvetica", 9), bg=BG, fg=SUBTEXT).pack(pady=12)

root.mainloop()