import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def message_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message)

def binary_to_message(binary_string):
    message = ''
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        message += chr(int(byte, 2))
    return message

def hide_message(image_path, message):
    img = Image.open(image_path)
    binary_message = message_to_binary(message)
    
    if len(binary_message) > img.width * img.height * 3:
        raise ValueError("Le message est trop long pour être caché dans l'image.")
    
    binary_message_length = format(len(binary_message), '032b')  # 32-bit header for message length
    binary_message = binary_message_length + binary_message + '1111111111111110'  # Add length header and end marker
    
    data_index = 0
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            if data_index < len(binary_message):
                r = r & ~1 | int(binary_message[data_index])
                data_index += 1
            if data_index < len(binary_message):
                g = g & ~1 | int(binary_message[data_index])
                data_index += 1
            if data_index < len(binary_message):
                b = b & ~1 | int(binary_message[data_index])
                data_index += 1
            img.putpixel((x, y), (r, g, b))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    output_path = os.path.splitext(image_path)[0] + "_stegano.png"
    img.save(output_path)
    print(f"Message caché avec succès dans {output_path}")
    return output_path

def reveal_message(image_path):
    img = Image.open(image_path)
    binary_message = ''
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)
    
    # Extract the length of the hidden message
    if len(binary_message) >= 32:
        binary_message_length = int(binary_message[:32], 2)
        actual_message_binary = binary_message[32:32 + binary_message_length]
        if binary_message[32 + binary_message_length:32 + binary_message_length + 16] == '1111111111111110':
            return binary_to_message(actual_message_binary)
    
    return ''

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    entry_image_path.delete(0, tk.END)
    entry_image_path.insert(0, file_path)

def hide_message_gui():
    image_path = entry_image_path.get()
    message = text_message.get("1.0", tk.END).strip()
    try:
        output_path = hide_message(image_path, message)
        messagebox.showinfo("Succès", f"Message caché avec succès dans {output_path}")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def reveal_message_gui():
    image_path = entry_image_path.get()
    try:
        message = reveal_message(image_path)
        text_message.delete("1.0", tk.END)
        text_message.insert(tk.END, message)
        if not message:
            messagebox.showinfo("Résultat", "Aucun message trouvé dans l'image.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Interface graphique
root = tk.Tk()
root.title("Mini Project")

# Set dark theme colors
bg_color = "#2e2e2e"
fg_color = "#ffffff"
entry_bg_color = "#3e3e3e"
entry_fg_color = "#ffffff"
button_bg_color = "#4e4e4e"
button_fg_color = "#ffffff"

root.configure(bg=bg_color)

frame = tk.Frame(root, bg=bg_color)
frame.pack(padx=10, pady=10)

label_image_path = tk.Label(frame, text="Chemin de l'image :", font=("Helvetica", 12), bg=bg_color, fg=fg_color)
label_image_path.grid(row=0, column=0, sticky="e")

entry_image_path = tk.Entry(frame, width=50, font=("Helvetica", 12), bg=entry_bg_color, fg=entry_fg_color)
entry_image_path.grid(row=0, column=1, padx=5)

button_browse = tk.Button(frame, text="Parcourir", command=browse_image, font=("Helvetica", 12), bg=button_bg_color, fg=button_fg_color)
button_browse.grid(row=0, column=2)

label_message = tk.Label(frame, text="Message :", font=("Helvetica", 12), bg=bg_color, fg=fg_color)
label_message.grid(row=1, column=0, sticky="ne")

text_message = tk.Text(frame, width=50, height=10, font=("Helvetica", 12), bg=entry_bg_color, fg=entry_fg_color)
text_message.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

button_hide = tk.Button(frame, text="Cacher le message", command=hide_message_gui, font=("Helvetica", 12), bg=button_bg_color, fg=button_fg_color)
button_hide.grid(row=2, column=1, pady=5)

button_reveal = tk.Button(frame, text="Révéler le message", command=reveal_message_gui, font=("Helvetica", 12), bg=button_bg_color, fg=button_fg_color)
button_reveal.grid(row=2, column=2, pady=5)

root.mainloop()
