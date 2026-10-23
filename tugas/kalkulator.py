
import tkinter as tk

# Membuat jendela kalkulator
root = tk.Tk()
root.title("Kalkulator")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#E8EEF5")

# Variabel untuk menyimpan perhitungan
angka_pertama = None
operator = None

# Layar kalkulator
layar = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=5,
    relief="ridge"
)
layar.grid(
    row=0, column=0,
    columnspan=4,
    padx=10, pady=15,
    sticky="nsew",
    ipady=10
)

# Fungsi tombol angka
def tekan_angka(angka):
    layar.insert(tk.END, angka)

# Fungsi tombol hapus semua
def hapus():
    global angka_pertama, operator
    layar.delete(0, tk.END)
    angka_pertama = None
    operator = None

# Fungsi tombol hapus satu karakter
def hapus_satu():
    isi = layar.get()
    layar.delete(0, tk.END)
    layar.insert(0, isi[:-1])

# Fungsi tombol desimal
def tekan_desimal():
    isi = layar.get()
    if "." not in isi:
        if isi == "":
            layar.insert(0, "0.")
        else:
            layar.insert(tk.END, ".")

# Fungsi operator (+, -, *, /)
def pilih_operator(op):
    global angka_pertama, operator

    isi = layar.get()

    if isi == "":
        return

    try:
        angka_pertama = float(isi)
        operator = op

        # Kosongkan layar untuk angka kedua
        layar.delete(0, tk.END)

    except ValueError:
        pass

# Fungsi tombol sama dengan
def hitung():
    global angka_pertama, operator

    if angka_pertama is None or operator is None:
        return

    isi = layar.get()

    if isi == "":
        return

    try:
        angka_kedua = float(isi)

        if operator == "+":
            hasil = angka_pertama + angka_kedua
        elif operator == "-":
            hasil = angka_pertama - angka_kedua
        elif operator == "*":
            hasil = angka_pertama * angka_kedua
        elif operator == "/":
            if angka_kedua == 0:
                layar.delete(0, tk.END)
                layar.insert(0, "Tidak bisa dibagi 0")
                angka_pertama = None
                operator = None
                return
            hasil = angka_pertama / angka_kedua
        else:
            return

        if hasil == int(hasil):
            hasil = int(hasil)

        layar.delete(0, tk.END)
        layar.insert(0, str(hasil))

        angka_pertama = None
        operator = None

    except ValueError:
        pass

        # Rapikan hasil desimal
        if hasil == int(hasil):
            hasil = int(hasil)

        layar.delete(0, tk.END)
        layar.insert(0, str(hasil))

        # Simpan hasil agar bisa dihitung kembali
        angka_pertama = hasil
        operator = None

    except ValueError:
        layar.delete(0, tk.END)
        layar.insert(0, "Input tidak valid")
        angka_pertama = None
        operator = None

# Daftar tombol kalkulator
tombol = [
    ("C", 1, 0, hapus),
    ("⌫", 1, 1, hapus_satu),
    ("÷", 1, 2, lambda: pilih_operator("/")),
    ("×", 1, 3, lambda: pilih_operator("*")),

    ("7", 2, 0, lambda: tekan_angka("7")),
    ("8", 2, 1, lambda: tekan_angka("8")),
    ("9", 2, 2, lambda: tekan_angka("9")),
    ("−", 2, 3, lambda: pilih_operator("-")),

    ("4", 3, 0, lambda: tekan_angka("4")),
    ("5", 3, 1, lambda: tekan_angka("5")),
    ("6", 3, 2, lambda: tekan_angka("6")),
    ("+", 3, 3, lambda: pilih_operator("+")),

    ("1", 4, 0, lambda: tekan_angka("1")),
    ("2", 4, 1, lambda: tekan_angka("2")),
    ("3", 4, 2, lambda: tekan_angka("3")),
    ("=", 4, 3, hitung),

    ("0", 5, 0, lambda: tekan_angka("0")),
    (".", 5, 1, tekan_desimal),
]

# Membuat tombol dan mengatur tampilannya
for teks, baris, kolom, fungsi in tombol:
    warna = "#FFFFFF"

    if teks in ["C", "⌫"]:
        warna = "#C7D8EE"
    elif teks in ["÷", "×", "−", "+", "="]:
        warna = "#80A9DF"

    btn = tk.Button(
        root,
        text=teks,
        font=("Arial", 16, "bold"),
        bg=warna,
        activebackground="#B3C9E5",
        command=fungsi
    )

    btn.grid(
        row=baris,
        column=kolom,
        padx=5,
        pady=5,
        sticky="nsew",
        ipadx=5,
        ipady=10
    )

# Mengatur ukuran kolom dan baris
for kolom in range(4):
    root.grid_columnconfigure(kolom, weight=1, uniform="kolom")

for baris in range(1, 6):
    root.grid_rowconfigure(baris, weight=1, uniform="baris")

# Menjalankan aplikasi
root.mainloop()
