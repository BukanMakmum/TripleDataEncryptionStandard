import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
import webbrowser # Fungsi untuk mengarahkan ke alamat email saat teks hak cipta diklik
import os
import re

# Initial Permutation (IP) table
# Tabel IP untuk mengawali algoritma DES
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation (FP) table
# Tabel FP untuk mengakhiri algoritma DES
FP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

# Tabel Kompresi Kunci PC-1
# Tabel PC-1 untuk menghasilkan kunci sub
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Tabel Kompresi Kunci PC-2
# Tabel PC-2 untuk menghasilkan subkunci
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# Expansion Box (EBox) table
# Tabel EBox untuk mengembang bit dari setengah bagian kanan
EBox = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11,
        12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
        22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# S-Box tables
# Tabel S-Box digunakan untuk substitusi bit-bit
SBox = [
    # S1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    # S2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    # S3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    # S4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    # S5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    # S6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    # S7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    # S8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]

# P-Box permutation
PBox = [16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25]

# Tabel pergeseran bit untuk subkunci
ShiftBits = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Fungsi untuk mengonversi desimal ke biner
def decimal_to_binary(decimal, width):
    binary = bin(decimal)[2:]
    return binary.zfill(width)

# Fungsi untuk mengonversi heksadesimal ke biner
def hex_to_binary(hex_string, width):
    decimal = int(hex_string, 16)
    return decimal_to_binary(decimal, width)

# Fungsi untuk melakukan permutasi dengan tabel yang diberikan
def permute(data, table):
    return ''.join(data[i - 1] for i in table)

# Fungsi untuk melakukan pergeseran bit (left shift) pada data
def left_shift(data, shift_amount):
    return data[shift_amount:] + data[:shift_amount]

# Fungsi untuk melakukan XOR antara dua string biner dengan panjang yang sama
def xor(bin_str1, bin_str2):
    return ''.join('1' if a != b else '0' for a, b in zip(bin_str1, bin_str2))

# Fungsi untuk menghasilkan subkunci menggunakan tabel PC-1 dan tabel pergeseran bit
def generate_subkeys(key):
    global PC1, PC2, ShiftBits

    key_bin = bin(int(key, 16))[2:].zfill(64)

    # Lakukan "parity bit drop" sesuai dengan deskripsi yang Anda berikan
    key_parity_dropped = ''.join(key_bin[i] for i in range(64) if (i + 1) % 8 != 0)

    # Lakukan permutasi sesuai dengan tabel PC1 yang telah didefinisikan
    key_permuted = permute(key_bin, PC1)

    left_key, right_key = key_permuted[:28], key_permuted[28:]
    subkeys = []

    for round_num, shift_amount in enumerate(ShiftBits, start=1):
        left_key = left_shift(left_key, shift_amount)
        right_key = left_shift(right_key, shift_amount)

        subkey = permute(left_key + right_key, PC2)
        subkeys.append(subkey)

    return subkeys

def encrypt_3des(data, subkeys1, subkeys2, subkeys3):
    data_bin = hex_to_binary(data, 64)
    data_permuted = permute(data_bin, IP)
    
    left_half = data_permuted[:32]
    right_half = data_permuted[32:]

    for i in range(16):
        subkey1 = subkeys1[i]
        subkey2 = subkeys2[i]
        subkey3 = subkeys3[i]

        # Perubahan kunci yang digunakan di setiap putaran
        if i % 2 == 0:
            subkey = subkey1
        else:
            subkey = subkey2 if i % 4 == 1 else subkey3

        right_expanded = permute(right_half, EBox)
        
        right_xor = xor(right_expanded, subkey)
        sbox_output = ""
        
        for j in range(8):
            sbox_input = right_xor[j * 6: (j + 1) * 6]
            row = int(sbox_input[0] + sbox_input[5], 2)
            col = int(sbox_input[1:5], 2)
            sbox_value = SBox[j][row * 16 + col]
            sbox_output += format(sbox_value, '04b')
        
        right_permuted = permute(sbox_output, PBox)
        
        right_xor = xor(left_half, right_permuted)
        left_half = right_half
        right_half = right_xor

    combined = right_half + left_half
    ciphertext = permute(combined, FP)
    
    return ciphertext

def decrypt_3des(data, subkeys1, subkeys2, subkeys3):
    data_bin = hex_to_binary(data, 64)
    data_permuted = permute(data_bin, IP)
    
    left_half = data_permuted[:32]
    right_half = data_permuted[32:]

    for i in range(15, -1, -1):
        subkey1 = subkeys1[i]
        subkey2 = subkeys2[i]
        subkey3 = subkeys3[i]

        # Perubahan kunci yang digunakan di setiap putaran
        if i % 2 == 0:
            subkey = subkey1
        else:
            subkey = subkey2 if i % 4 == 1 else subkey3

        right_expanded = permute(right_half, EBox)
        
        right_xor = xor(right_expanded, subkey)
        sbox_output = ""
        
        for j in range(8):
            sbox_input = right_xor[j * 6: (j + 1) * 6]
            row = int(sbox_input[0] + sbox_input[5], 2)
            col = int(sbox_input[1:5], 2)
            sbox_value = SBox[j][row * 16 + col]
            sbox_output += format(sbox_value, '04b')
        
        right_permuted = permute(sbox_output, PBox)
        
        right_xor = xor(left_half, right_permuted)
        left_half = right_half
        right_half = right_xor

    combined = right_half + left_half
    plaintext = permute(combined, FP)
    
    return plaintext

# Fungsi untuk menghasilkan subkunci untuk 3DES dengan tiga kunci
def generate_3des_subkeys(key1, key2, key3):
    subkeys1 = generate_subkeys(key1)
    subkeys2 = generate_subkeys(key2)
    subkeys3 = generate_subkeys(key3)
    return subkeys1, subkeys2, subkeys3

# Fungsi validasi input
def validate_input(entry_widget, label_text, length=None):
    # Mengambil teks dari entry widget
    input_text = entry_widget.get()

    if not input_text:
        # Jika input kosong, tampilkan notifikasi
        tk.messagebox.showwarning("Input Error", f"{label_text} tidak boleh kosong.")
        return False

    # Mengubah huruf kecil menjadi huruf besar
    input_text = input_text.upper()

    # Cek apakah input hanya mengandung karakter heksadesimal
    if not input_text.isalnum() or not all(c in "0123456789ABCDEF" for c in input_text):
        tk.messagebox.showwarning("Input Error", f"{label_text} harus berupa karakter heksadesimal.")
        return False

    # Jika panjang input tidak sesuai
    if length is not None and len(input_text) != length:
        tk.messagebox.showwarning("Input Error", f"{label_text} harus memiliki panjang {length} karakter heksadesimal.")
        return False

    return True

# Fungsi enkripsi dan dekripsi
def encrypt_3des_text():
    # Validasi input sebelum melakukan enkripsi
    if not (validate_input(data_entry, "Data", 16) and
            validate_input(key1_entry, "Key 1", 16) and
            validate_input(key2_entry, "Key 2", 16) and
            validate_input(key3_entry, "Key 3", 16)):
        return

    # Lanjutkan dengan enkripsi jika input valid
    data = data_entry.get()
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    key3 = key3_entry.get()

    subkeys1, subkeys2, subkeys3 = generate_3des_subkeys(key1, key2, key3)
    ciphertext = encrypt_3des(data, subkeys1, subkeys2, subkeys3)
    result_text.delete(1.0, tk.END)
    
    # Menambahkan hasil enkripsi dalam format biner dengan spasi tiap 8 digit dan baris baru tiap 32 digit
    encrypted_binary = "Encrypted (Binary):\n"
    for i in range(0, len(ciphertext), 32):
        encrypted_binary += ' '.join(ciphertext[i:i+8] for i in range(i, i+32, 8)) + "\n"

    # Menambahkan hasil dalam format heksadesimal
    hex_result = "\nEncrypted (Hex):\n" + format(int(ciphertext, 2), '016X')

    # Menghapus teks yang ada dalam result_text
    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)

    # Menyisipkan teks baru ke dalam result_text
    result_text.insert(tk.END, encrypted_binary.strip() + "\n" + hex_result)

    # Mengatur tag untuk mengatur teks di tengah
    result_text.tag_add("center", "1.0", "end")
    result_text.tag_configure("center", justify="center")

    # Mengunci result_text
    result_text.config(state='disabled')

# Fungsi dekripsi
def decrypt_3des_text():
    # Validasi input sebelum melakukan dekripsi
    if not (validate_input(data_entry, "Data", 16) and
            validate_input(key1_entry, "Key 1", 16) and
            validate_input(key2_entry, "Key 2", 16) and
            validate_input(key3_entry, "Key 3", 16)):
        return

    # Lanjutkan dengan dekripsi jika input valid
    data = data_entry.get()
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    key3 = key3_entry.get()

    subkeys1, subkeys2, subkeys3 = generate_3des_subkeys(key1, key2, key3)
    plaintext = decrypt_3des(data, subkeys1, subkeys2, subkeys3)
    result_text.delete(1.0, tk.END)        
    
    # Menambahkan hasil decrypted dalam format biner dengan spasi tiap 8 digit dan baris baru tiap 32 digit
    decrypted_binary = "Decrypted (Binary):\n"
    for i in range(0, len(plaintext), 32):
        decrypted_binary += ' '.join(plaintext[i:i+8] for i in range(i, i+32, 8)) + "\n"

    # Menambahkan hasil dalam format heksadesimal
    hex_result = "\nDecrypted (Hex):\n" + format(int(plaintext, 2), '016X')

    # Menghapus teks yang ada dalam result_text
    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)

    # Menyisipkan teks baru ke dalam result_text
    result_text.insert(tk.END, decrypted_binary.strip() + "\n" + hex_result)

    # Mengatur tag untuk mengatur teks di tengah
    result_text.tag_add("center", "1.0", "end")
    result_text.tag_configure("center", justify="center")

    # Mengunci result_text
    result_text.config(state='disabled')

def reset_fields():
    data_entry.delete(0, tk.END)
    key1_entry.delete(0, tk.END)
    key2_entry.delete(0, tk.END)
    key3_entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

def open_email(event):
    webbrowser.open("mailto:imamsayuti.usk@gmail.com")

# Fungsi untuk keluar dari aplikasi
def exit_app():
    window.quit()

def show_about_info():
    # Gunakan teks judul jendela dan versi aplikasi untuk mengatur teks keterangan
    window_title = window.title()
    email = "imamsyt22@mhs.usk.ac.id"  # Ganti dengan alamat email Anda
    about_info = f"{window_title}\nVersi {app_version}\n\nDikembangkan oleh [Bukan Makmum]\nEmail: {email}"
    result = messagebox.showinfo("About", about_info, icon=messagebox.INFO)
    if result:
        open_github()

def open_github(): 
    webbrowser.open("https://github.com/BukanMakmum/TripleDataEncryptionStandard.git")  # Ganti dengan URL repositori GitHub Anda
    
# Judul aplikasi dan versi
app_title = "Triple Data Encryption Standard"
app_version = "Education 1.0.beta"

window = tk.Tk()
window.title(f"{app_title}")

# Mendapatkan ukuran layar
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Mengatur ukuran jendela
window_width = 540
window_height = 410
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Mencegah pengguna untuk mengubah ukuran jendela
window.resizable(False, False)

# Dapatkan direktori tempat script ini berada
current_directory = os.path.dirname(__file__) if os.path.dirname(__file__) else '.'

# Gabungkan direktori saat ini dengan nama file ikon favicon
favicon_path = os.path.join(current_directory, "favicon.ico")

# Atur favicon
window.iconbitmap(default=favicon_path)

# Warna latar belakang dan font
background_color = "#6495ED"
font_style = ("Helvetica", 11)

frame = tk.Frame(window, bg=background_color, padx=20, pady=20)
frame.pack(expand=True, fill="both", side="top")

# Membuat objek menu utama
menubar = tk.Menu(window)
window.config(menu=menubar)

# Membuat menu "File" tanpa garis putus-putus
file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)

# Menambahkan opsi "Debug Result" di menu "File" dan menonaktifkannya saat pertama kali dibuat
file_menu.add_command(label="Debug Result", command="", state=tk.DISABLED)

# Menambahkan opsi "Exit" di menu "File" tanpa garis pemisah
file_menu.add_command(label="Exit", command=exit_app)

# Menambahkan opsi "About" di menu utama
menubar.add_command(label="About", command=show_about_info)

# Judul aplikasi
app_title_label = tk.Label(frame, text=app_title, bg=background_color, font=("Helvetica", 14))
app_title_label.grid(row=0, column=1, columnspan=1, pady=(10, 0))

# Label versi dengan font yang lebih kecil
version_label = tk.Label(frame, text=f"Versi {app_version}", font=("Helvetica", 11), bg=background_color)
version_label.grid(row=1, column=1, columnspan=1, pady=(5, 20))

data_label = tk.Label(frame, text="Data (hex):", bg=background_color, font=font_style)
data_label.grid(row=2, column=0, sticky="w", padx=(20, 10))
data_entry = tk.Entry(frame, font=font_style, justify="right", width=30)
data_entry.grid(row=2, column=1, padx=(10, 20))

key1_label = tk.Label(frame, text="Key 1 (hex):", bg=background_color, font=font_style)
key1_label.grid(row=3, column=0, sticky="w", padx=(20, 10))
key1_entry = tk.Entry(frame, font=font_style, justify="right", width=30)
key1_entry.grid(row=3, column=1, padx=(10, 20))

key2_label = tk.Label(frame, text="Key 2 (hex):", bg=background_color, font=font_style)
key2_label.grid(row=4, column=0, sticky="w", padx=(20, 10))
key2_entry = tk.Entry(frame, font=font_style, justify="right", width=30)
key2_entry.grid(row=4, column=1, padx=(10, 20))

key3_label = tk.Label(frame, text="Key 3 (hex):", bg=background_color, font=font_style)
key3_label.grid(row=5, column=0, sticky="w", padx=(20, 10))
key3_entry = tk.Entry(frame, font=font_style, justify="right", width=30)
key3_entry.grid(row=5, column=1, padx=(10, 20))

reset_button = tk.Button(frame, text="Reset", bg="#B22222", fg="white", font=("Helvetica", 11), command=reset_fields, width=6, height=1)
reset_button.grid(row=6, column=0, pady=10, padx=(20, 20))

decrypt_button = tk.Button(frame, text="Decrypt", bg="#808080", fg="white", font=("Helvetica", 11), command=decrypt_3des_text, width=6, height=1)
decrypt_button.grid(row=6, column=1, pady=10, padx=(20, 20))

encrypt_button = tk.Button(frame, text="Encrypt", bg="#228B22", fg="white", font=("Helvetica", 11), command=encrypt_3des_text, width=6, height=1)
encrypt_button.grid(row=6, column=2, pady=10, padx=(20, 20))

result_label = tk.Label(frame, text="Result:", bg=background_color, font=font_style)
result_label.grid(row=7, column=1, sticky="nsew")
result_text = scrolledtext.ScrolledText(frame, height=6, width=17, font=font_style, state='disabled')
result_text.grid(row=8, column=0, columnspan=3, sticky="nsew", padx=(25, 20))

# #Dilarang hapus, sesama pengembang/pemrograman/mahasiswa/sarjana harus saling menghargai karya orang lain!
copyright_label = tk.Label(frame, text="© 2023 BukanMakmum.", foreground="#fbf7f6", cursor="hand2", bg=background_color, font=("Helvetica", 10))
copyright_label.grid(row=9, column=1, pady=(10, 20), sticky="nsew")
"""
Jika ingin berkontribusi silakan Clone Github berikut https://github.com/BukanMakmum/TripleDataEncryptionStandard.git
#User sangat menghargai kontribusi Anda, dengan menampilkan profil di halaman kontribusi. 

# Mengatur teks hak cipta menjadi rata tengah horizontal
#copyright_label.configure(anchor="center", justify="center")
"""
# Menghubungkan fungsi dengan klik pada teks hak cipta
copyright_label.bind("<Button-1>", open_email)

window.mainloop()