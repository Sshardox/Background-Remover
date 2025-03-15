import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image
import os

def process_image():
    input_path = entry_input.get()
    output_path = entry_output.get()
    if not input_path or not output_path:
        messagebox.showwarning("Warning", "Please select an input image and an output path.")
        return
    try:
        input_image = Image.open(input_path)
        output = remove(input_image)
        output.save(output_path)
        messagebox.showinfo("Success", "Background removed successfully!")
        output_image = Image.open(output_path)
        output_image.show()
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {input_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_input():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if file_path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, file_path)

def select_output():
    file_path = filedialog.asksaveasfilename(
        title="Save the image without background",
        defaultextension=".png",
        filetypes=[("PNG file", "*.png")]
    )
    if file_path:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, file_path)

root = tk.Tk()
root.title("Background Remover")
root.geometry("400x300")

tk.Label(root, text="Input Image:").pack(pady=5)
entry_input = tk.Entry(root, width=40)
entry_input.pack(pady=5)
tk.Button(root, text="Select", command=select_input).pack(pady=5)

tk.Label(root, text="Save as:").pack(pady=5)
entry_output = tk.Entry(root, width=40)
entry_output.pack(pady=5)
tk.Button(root, text="Select", command=select_output).pack(pady=5)

tk.Button(root, text="Remove Background", command=process_image).pack(pady=20)

root.mainloop()