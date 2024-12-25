from tkinter import Tk, Label, Entry, Button, Text, END
from Crypto.Cipher import DES
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt():
    key = key_entry.get().encode('utf-8')
    if len(key) != 8:
        result_text.delete('1.0', END)
        result_text.insert(END, "Key harus 8 karakter!")
        return

    message = input_text.get("1.0", END).strip()
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = pad(message).encode('utf-8')
    encrypted_message = cipher.encrypt(padded_message)
    encoded_message = base64.b64encode(encrypted_message).decode('utf-8')

    result_text.delete('1.0', END)
    result_text.insert(END, encoded_message)

def decrypt():
    key = key_entry.get().encode('utf-8')
    if len(key) != 8:
        result_text.delete('1.0', END)
        result_text.insert(END, "Key harus 8 karakter!")
        return

    encrypted_message = input_text.get("1.0", END).strip()
    cipher = DES.new(key, DES.MODE_ECB)
    try:
        decoded_message = base64.b64decode(encrypted_message)
        decrypted_message = cipher.decrypt(decoded_message).decode('utf-8').strip()

        result_text.delete('1.0', END)
        result_text.insert(END, decrypted_message)
    except Exception as e:
        result_text.delete('1.0', END)
        result_text.insert(END, "Dekripsi gagal: " + str(e))

# GUI setup
app = Tk()
app.title("DES Encryption/Decryption")
app.geometry("500x400")

Label(app, text="Key (8 karakter):").pack(pady=5)
key_entry = Entry(app, width=30)
key_entry.pack(pady=5)

Label(app, text="Input Text:").pack(pady=5)
input_text = Text(app, height=5, width=50)
input_text.pack(pady=5)

Button(app, text="Encrypt", command=encrypt).pack(pady=5)
Button(app, text="Decrypt", command=decrypt).pack(pady=5)

Label(app, text="Result:").pack(pady=5)
result_text = Text(app, height=5, width=50)
result_text.pack(pady=5)

app.mainloop()