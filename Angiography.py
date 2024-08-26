import tkinter as tk
from tkinter import Menu, Label, Toplevel, messagebox
from PIL import Image, ImageTk

class AngiographyCenterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Angiography Center Designer")
        self.geometry("900x700")

        # Menu Bar
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        # Adding Menus
        home_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Home", menu=home_menu)
        home_menu.add_command(label="Introduction", command=self.show_introduction)
        home_menu.add_command(label="Devices", command=self.show_devices)
        home_menu.add_command(label="Design Standards", command=self.show_standards)
        home_menu.add_separator()
        home_menu.add_command(label="Exit", command=self.quit)

        images_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Images", menu=images_menu)
        images_menu.add_command(label="View Images", command=self.show_images)

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        # Welcome Label
        welcome_label = Label(self, text="Welcome to the Angiography Center Designer", font=("Arial", 18))
        welcome_label.pack(pady=20)

        # Display the uploaded image
        self.display_image()

    def display_image(self):
        try:
            # Load and display the uploaded image
            img_path = ("SDG_CaseStudy_St_Johns_Angio_07.jpg")  # مسیر تصویر آپلود شده
            img = Image.open(img_path)
            img = img.resize((600, 400), Image.Resampling.LANCZOS)  # تغییر اندازه تصویر
            img = ImageTk.PhotoImage(img)

            img_label = Label(self, image=img)
            img_label.image = img  # نگه‌داشتن مرجع تصویر
            img_label.pack(pady=20)
        except Exception as e:
            messagebox.showerror("Image Error", f"Failed to load image: {e}")

    def show_introduction(self):
        messagebox.showinfo("Introduction", "This software helps you design and manage an Angiography Center.\nYou can explore rooms, devices, and design standards.")

    def show_devices(self):
        devices_window = Toplevel(self)
        devices_window.title("Devices in the Angiography Center")
        devices_window.geometry("400x300")
        
        devices_info = Label(devices_window, text="1. Angiography Machine\n2. Patient Monitoring System\n3. X-ray System\n4. Injector\n5. Imaging Workstation", font=("Arial", 14))
        devices_info.pack(pady=20)

    def show_standards(self):
        standards_window = Toplevel(self)
        standards_window.title("Design Standards for Angiography Centers")
        standards_window.geometry("500x400")

        standards_info = Label(standards_window, text="Standards for designing Angiography Centers:\n\n1. Room size: Minimum 50 square meters\n2. Radiation protection measures\n3. Proper ventilation and air filtering\n4. Power backup systems\n5. Patient and staff safety considerations", font=("Arial", 14))
        standards_info.pack(pady=20)

    def show_images(self):
        images_window = Toplevel(self)
        images_window.title("Images of the Angiography Center")
        images_window.geometry("800x600")

        # Display the same uploaded image
        try:
            img_path = ("SDG_CaseStudy_St_Johns_Angio_07.jpg")
            img = Image.open(img_path)
            img = img.resize((400, 300), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)

            img_label = Label(images_window, image=img)
            img_label.image = img  # نگه‌داشتن مرجع تصویر
            img_label.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Image Error", f"Failed to load image: {e}")

    def show_about(self):
        messagebox.showinfo("About", "Angiography Center Designer v1.0\nDeveloped by [Your Name]")

if __name__ == "__main__":
    app = AngiographyCenterApp()
    app.mainloop()
