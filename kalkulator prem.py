import tkinter as tk

# Fungsi untuk menambahkan angka atau simbol
def click_button(value):
    current = display.get()
    if current == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, value)

# Fungsi menghitung hasil
def calculate():
    try:
        expression = display.get().replace("^", "**")
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Fungsi clear
def clear():
    display.delete(0, tk.END)
    display.insert(0, "0")

# Fungsi backspace
def backspace():
    current = display.get()
    if len(current) > 1:
        display.delete(len(current)-1, tk.END)
    else:
        display.delete(0, tk.END)
        display.insert(0, "0")

# Fungsi efek hover (masuk dan keluar tombol)
def on_hover(e):
    e.widget['bg'] = hover_color

def on_leave(e):
    e.widget['bg'] = e.widget.default_bg

# --- GUI ---
window = tk.Tk()
window.title("Kalkulator Elegan")
window.configure(bg="#1b1b1d")
window.resizable(False, False)

# Warna elegan
bg_color = "#1b1b1d"       # Latar belakang hitam elegan
button_color = "#2d2d30"  # Tombol gelap
hover_color = "#3e3e42"   # Hover efek lebih terang
accent_color = "#00a896"  # Hijau kebiruan elegan (untuk tombol '=')

# Display
display = tk.Entry(window, width=18, font=("Arial", 24), bd=5, relief="sunken",
                   justify="right", bg="#f0f0f0")
display.grid(row=0, column=0, columnspan=4, pady=10)
display.insert(0, "0")

# Tombol
buttons = [
    ("AC", clear), ("⌫", backspace), ("^", lambda: click_button("^")), ("/", lambda: click_button("/")),
    ("7", lambda: click_button("7")), ("8", lambda: click_button("8")), ("9", lambda: click_button("9")), ("*", lambda: click_button("*")),
    ("4", lambda: click_button("4")), ("5", lambda: click_button("5")), ("6", lambda: click_button("6")), ("-", lambda: click_button("-")),
    ("1", lambda: click_button("1")), ("2", lambda: click_button("2")), ("3", lambda: click_button("3")), ("+", lambda: click_button("+")),
    ("0", lambda: click_button("0")), (".", lambda: click_button(".")), ("=", calculate)
]

# Tempatkan tombol
row = 1
col = 0
for btn_text, btn_cmd in buttons:
    if btn_text == "=":
        btn = tk.Button(window, text=btn_text, width=19, height=2,
                        command=btn_cmd, bg=accent_color, fg="white", activebackground=accent_color)
        btn.grid(row=row, column=2, columnspan=10, pady=6)
    else:
        btn = tk.Button(window, text=btn_text, width=8, height=2,
                        command=btn_cmd, bg=button_color, fg="white", activebackground=button_color)
        btn.grid(row=row, column=col, pady=5)

    # Simpan warna asli dan tambahkan efek hover
    btn.default_bg = btn['bg']
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)

    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
