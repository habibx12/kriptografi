import tkinter as tk
from tkinter import messagebox

# Simulasi sederhana dari Enigma Cipher
class EnigmaCipher:
    def __init__(self):
        self.rotor = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.offset = 0

    def set_offset(self, offset):
        self.offset = offset % len(self.rotor)

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        encrypted = ""
        for char in plaintext:
            if char in self.rotor:
                index = (self.rotor.index(char) + self.offset) % len(self.rotor)
                encrypted += self.rotor[index]
            else:
                encrypted += char  # Non-alphabetic characters are not encrypted
        return encrypted

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        decrypted = ""
        for char in ciphertext:
            if char in self.rotor:
                index = (self.rotor.index(char) - self.offset) % len(self.rotor)
                decrypted += self.rotor[index]
            else:
                decrypted += char  # Non-alphabetic characters are not decrypted
        return decrypted

# GUI Implementation
def main():
    def encrypt_text():
        try:
            offset = int(offset_entry.get())
            plaintext = input_text.get("1.0", tk.END).strip()
            enigma.set_offset(offset)
            ciphertext = enigma.encrypt(plaintext)
            output_text.delete("1.0", tk.END)
            output_text.insert("1.0", ciphertext)
        except ValueError:
            messagebox.showerror("Error", "Offset harus berupa angka.")

    def decrypt_text():
        try:
            offset = int(offset_entry.get())
            ciphertext = input_text.get("1.0", tk.END).strip()
            enigma.set_offset(offset)
            plaintext = enigma.decrypt(ciphertext)
            output_text.delete("1.0", tk.END)
            output_text.insert("1.0", plaintext)
        except ValueError:
            messagebox.showerror("Error", "Offset harus berupa angka.")

    # Initialize Enigma Cipher
    enigma = EnigmaCipher()

    # Set up the main window
    root = tk.Tk()
    root.title("Enigma Cipher")

    # Input Text
    tk.Label(root, text="Input Text:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    input_text = tk.Text(root, height=5, width=40)
    input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    # Offset
    tk.Label(root, text="Offset:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    offset_entry = tk.Entry(root)
    offset_entry.grid(row=2, column=1, padx=10, pady=5)

    # Buttons
    encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
    encrypt_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
    decrypt_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

    # Output Text
    tk.Label(root, text="Output Text:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    output_text = tk.Text(root, height=5, width=40)
    output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()