import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("450x420")
root.resizable(False, False)  # Agar jendela tidak bisa diperbesar
root.config(bg="#333333")

# Entry untuk tampilan angka
display = tk.Entry(root, font=("Arial", 20), bd=6, relief="sunken",
                   justify="right", bg="#ffffff")
display.pack(padx=10, pady=15, fill="both")

# Fungsi untuk memasukkan angka/simbol
def click_button(value):
    current = display.get()
    if current == "Erorr":
        display.delete(0, tk.END)
    display.insert(tk.END, value)

# Fungsi menghitung hasil
def calculate():
    try:
        expression = display.get().replace("^", "**")
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Tidak Bisa Dibagi Nol")

# Fungsi hapus semua (clear)
def clear():
    display.delete(0, tk.END)

# Fungsi hapus satu karakter (backspace)
def backspace():
    current = display.get()
    display.delete(len(current)-1, tk.END)

# Frame untuk tombol
button_frame = tk.Frame(root, bg="#333333")
button_frame.pack(pady=10)

# Daftar tombol kalkulator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("^", 4, 2), ("+", 4, 3),
    ("AC", 5, 0), ("⌫", 5, 1), ("=", 5, 2)]

# Membuat tombol secara otomatis
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(button_frame, text=text, width=20, height=2,
                        bg="#2ECC71", fg="white", font=("Arial", 12),
                        command=calculate)
        btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5)
    elif text == "AC":
        btn = tk.Button(button_frame, text=text, width=10, height=2,
                        bg="#E74C3C", fg="white", font=("Arial", 12),
                        command=clear)
        btn.grid(row=row, column=col, padx=5, pady=5)
    elif text == "⌫":
        btn = tk.Button(button_frame, text=text, width=10, height=2,
                        bg="#F39C12", fg="white", font=("Arial", 12),
                        command=backspace)
        btn.grid(row=row, column=col, padx=5, pady=5)
    else:
        btn = tk.Button(button_frame, text=text, width=10, height=2,
                        bg="#555555", fg="white", font=("Arial", 12),
                        command=lambda value=text: click_button(value))
        btn.grid(row=row, column=col, padx=5, pady=5)

# Menjalankan program
root.mainloop()
