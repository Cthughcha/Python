import os
import shutil

# --- Konfigurasi ---
# Ganti dengan path folder yang ingin diatur
folder_sumber = "/home/sansan/Downloads"  # Contoh

# Mendefinisikan kategori file dan folder tujuannya
kategori_file = {
    "gambar": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "dokumen": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "video": [".mp4", ".mov", ".avi", ".mkv"],
    "audio": [".mp3", ".wav", ".aac"],
    "arsip": [".zip", ".rar", ".7z"],
    "program": [".exe", ".msi"],
    "lainnya": [] # Kategori untuk file yang tidak terdefinisi
}

# --- Fungsi untuk mengatur file ---
def atur_file_otomatis():
    print(f"Memulai proses pengaturan file di {folder_sumber}...")
    
    # Membuat folder tujuan jika belum ada
    for folder in kategori_file.keys():
        path_folder = os.path.join(folder_sumber, folder.capitalize())
        if not os.path.exists(path_folder):
            os.makedirs(path_folder)
            print(f"Folder '{folder.capitalize()}' dibuat.")

    # Memproses setiap file di folder sumber
    for filename in os.listdir(folder_sumber):
        if os.path.isdir(os.path.join(folder_sumber, filename)):
            continue  # Abaikan folder

        ext = os.path.splitext(filename)[1].lower()
        tujuan_folder = "Lainnya"
        
        # Mencari kategori yang cocok
        for kategori, ekstensi_list in kategori_file.items():
            if ext in ekstensi_list:
                tujuan_folder = kategori.capitalize()
                break
        
        # Memindahkan file
        path_file_asal = os.path.join(folder_sumber, filename)
        path_file_tujuan = os.path.join(folder_sumber, tujuan_folder, filename)
        
        # Mencegah file dengan nama yang sama
        if os.path.exists(path_file_tujuan):
            print(f"Peringatan: File '{filename}' sudah ada di tujuan. Dilewati.")
        else:
            shutil.move(path_file_asal, path_file_tujuan)
            print(f"'{filename}' dipindahkan ke '{tujuan_folder}'.")

    print("Proses selesai. 🎉")

# Menjalankan fungsi
atur_file_otomatis()