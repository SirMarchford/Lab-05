import tkinter as tk
import requests
from PIL import Image, ImageTk

def fetch_fox():
    response = requests.get("https://randomfox.ca/floof/")
    data = response.json()
    image_url = data['image']

    image_response = requests.get(image_url)
    img_data = image_response.content

    with open("fox_image.jpg", "wb") as img_file:
        img_file.write(img_data)

    image = Image.open("fox_image.jpg")
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo
    label.place(x=0, y=0)

root = tk.Tk()
root.title("Random Fox Image Generator")
root.geometry('800x600')

label = tk.Label(root)
label.pack()

fetch_button = tk.Button(root, text="Fetch Fox", command=fetch_fox)
fetch_button.pack()

root.mainloop()
