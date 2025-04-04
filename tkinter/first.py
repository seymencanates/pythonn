import tkinter as tk
from tkinter import ttk, messagebox

def open_read_page():
    messagebox.showinfo("Sayfa", "Veri Okuma Sayfası Açıldı")

def open_write_page():
    messagebox.showinfo("Sayfa", "Veri Yazma Sayfası Açıldı")

def open_update_page():
    messagebox.showinfo("Sayfa", "Veri Güncelleme Sayfası Açıldı")

def open_delete_page():
    messagebox.showinfo("Sayfa", "Veri Silme Sayfası Açıldı")

def create_main_window():
    root = tk.Tk()
    root.title("Veri Yönetim Sistemi")
    root.geometry("800x500")
    
    # Menü çubuğu oluşturma
    menubar = tk.Menu(root)
    
    # Veri İşlemleri Menüsü
    data_menu = tk.Menu(menubar, tearoff=0)
    data_menu.add_command(label="Veri Okuma", command=open_read_page)
    data_menu.add_command(label="Veri Yazma", command=open_write_page)
    data_menu.add_command(label="Veri Güncelleme", command=open_update_page)
    data_menu.add_command(label="Veri Silme", command=open_delete_page)
    data_menu.add_separator()
    data_menu.add_command(label="Çıkış", command=root.quit)
    
    menubar.add_cascade(label="İşlemler", menu=data_menu)
    root.config(menu=menubar)
    
    # Ana Frame
    frame = ttk.Frame(root, padding=10)
    frame.pack(expand=True, fill="both")
    
    label = ttk.Label(frame, text="Veri Yönetim Sistemi", font=("Arial", 16))
    label.pack(pady=20)
    
    # Treeview Tablosu
    columns = ("ID", "Ad", "Soyad", "Yaş")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")
    
    tree.pack(expand=True, fill="both", pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_main_window()
