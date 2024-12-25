from tkinter import Tk, Label, Button, filedialog, Text, messagebox
from stegano import lsb

def hide_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg")])
    if not file_path:
        return

    message = text_input.get("1.0", "end-1c")
    if not message:
        messagebox.showerror("Error", "No message to hide!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if not save_path:
        return

    try:
        secret = lsb.hide(file_path, message)
        secret.save(save_path)
        messagebox.showinfo("Success", "Message hidden successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def reveal_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg")])
    if not file_path:
        return

    try:
        message = lsb.reveal(file_path)
        if message:
            messagebox.showinfo("Hidden Message", f"Message: {message}")
        else:
            messagebox.showinfo("No Message", "No hidden message found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = Tk()
root.title("Steganography")

Label(root, text="Enter Message:").pack(pady=10)
text_input = Text(root, height=5, width=40)
text_input.pack(pady=5)

Button(root, text="Hide Message in Image", command=hide_message).pack(pady=5)
Button(root, text="Reveal Message from Image", command=reveal_message).pack(pady=5)

root.mainloop()