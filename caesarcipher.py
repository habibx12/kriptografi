import tkinter as tk
from tkinter import ttk

# enkripsi
def encrypt():
    try:
        shift = int(entry_shift_encrypt.get())
        plaintext = entry_plaintext.get()
        ciphertext = ""

        for char in plaintext:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                ciphertext += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                ciphertext += char

        result_encrypt.set(ciphertext)
    except ValueError:
        result_encrypt.set("Kunci harus berupa angka!")

# dekripsi
def decrypt():
    try:
        shift = int(entry_shift_decrypt.get())
        ciphertext = entry_ciphertext.get()
        plaintext = ""

        for char in ciphertext:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                plaintext += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            else:
                plaintext += char

        result_decrypt.set(plaintext)
    except ValueError:
        result_decrypt.set("Kunci harus berupa angka!")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# membuat window utama
root = tk.Tk()
root.title("Aplikasi Caesar Cipher")
root.geometry("600x350")
root.update_idletasks()
center_window(root)

# variabel hasil enkripsi dan dekripsi
result_encrypt = tk.StringVar()
result_decrypt = tk.StringVar()

# membuat tab
tab_control = ttk.Notebook(root)
tab_encrypt = ttk.Frame(tab_control)
tab_decrypt = ttk.Frame(tab_control)

tab_control.add(tab_encrypt, text="Enkripsi")
tab_control.add(tab_decrypt, text="Dekripsi")
tab_control.pack(expand=1, fill="both")

# tab enkripsi
label_plaintext = tk.Label(tab_encrypt, text="Masukkan Plaintext:", font=("Arial", 10))
label_plaintext.pack(pady=5)
entry_plaintext = tk.Entry(tab_encrypt, width=50)
entry_plaintext.pack(pady=5)
label_shift_encrypt = tk.Label(tab_encrypt, text="Masukkan Kunci Pergeseran:", font=("Arial", 10))
label_shift_encrypt.pack(pady=5)
entry_shift_encrypt = tk.Entry(tab_encrypt, width=10)
entry_shift_encrypt.pack(pady=5)
button_encrypt = tk.Button(tab_encrypt, text="Enkripsi", command=encrypt)
button_encrypt.pack(pady=10)
label_ciphertext_result = tk.Label(tab_encrypt, text="Hasil Ciphertext:", font=("Arial", 10))
label_ciphertext_result.pack(pady=5)
entry_result_encrypt = tk.Entry(tab_encrypt, textvariable=result_encrypt, width=50, state="readonly")
entry_result_encrypt.pack(pady=5)

# tab dekripsi
label_ciphertext = tk.Label(tab_decrypt, text="Masukkan Ciphertext:", font=("Arial", 10))
label_ciphertext.pack(pady=5)
entry_ciphertext = tk.Entry(tab_decrypt, width=50)
entry_ciphertext.pack(pady=5)
label_shift_decrypt = tk.Label(tab_decrypt, text="Masukkan Kunci Pergeseran:", font=("Arial", 10))
label_shift_decrypt.pack(pady=5)
entry_shift_decrypt = tk.Entry(tab_decrypt, width=10)
entry_shift_decrypt.pack(pady=5)
button_decrypt = tk.Button(tab_decrypt, text="Dekripsi", command=decrypt)
button_decrypt.pack(pady=10)
label_plaintext_result = tk.Label(tab_decrypt, text="Hasil Plaintext:", font=("Arial", 10))
label_plaintext_result.pack(pady=5)
entry_result_decrypt = tk.Entry(tab_decrypt, textvariable=result_decrypt, width=50, state="readonly")
entry_result_decrypt.pack(pady=5)

# menjalankan loop utama
root.mainloop()