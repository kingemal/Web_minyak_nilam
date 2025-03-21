import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageOps
import sqlite3
from datetime import datetime
import io
import os
import pydeck as pdk
from io import BytesIO
from PIL import Image
import segno 

# Fungsi untuk halaman Home
def home():
    st.title("Selamat Datang di Management System Nilam")
    
    # Contoh gambar dari Google
    st.image("https://media.istockphoto.com/id/1168224419/id/foto/hidup-semarak-hijau-pogostemon-cablin-patchouli-tanaman-daun-basah-dari-hujan.jpg?s=2048x2048&w=is&k=20&c=nwRSXMai7sXjumRmCiFb0ckTsIpx5sFFiLNnf29PHJo=", use_column_width=True)
    
    # Deskripsi perusahaan
    st.markdown("""
        <div style="text-align: center;">
            <p>Nilam merupakan tumbuhan penghasil minyak atsiri yang digunakan sebagai bahan tambahan dalam pembuatan industri seperti parfum, kosmetik, sabun dan lainnya.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Informasi kontak
    st.markdown("""
        <div style="text-align: center;">
            <h3>Kontak Kami</h3>
            <p>Hubungi kami melalui media sosial atau email:</p>
            <div style="display: flex; justify-content: center; align-items: center;">
                <div style="margin: 10px;">
                    <a href="ISI LINK IG" target="_blank" style="text-decoration: none; color: inherit;">
                        <i class="fa fa-instagram" style="font-size: 24px;"></i>
                        <p>@Nilam Aceh</p>
                    </a>
                </div>
                <div style="margin: 10px;">
                    <a href="" target="_blank" style="text-decoration: none; color: inherit;">
                        <i class="fa fa-facebook" style="font-size: 24px;"></i>
                        <p>Nilam Aceh</p>
                    </a>
                </div>
                <div style="margin: 10px;">
                    <a href="mailto:info@Nilamaceh.com" style="text-decoration: none; color: inherit;">
                        <i class="fa fa-envelope" style="font-size: 24px;"></i>
                        <p>nilamaceh@gmail.com</p>
                    </a>
                </div>
                <div style="margin: 10px;">
                    <i class="fa fa-phone" style="font-size: 24px;"></i>
                    <p>(tambah)</p>
                </div>
            </div>
            <p><strong>Alamat:</strong> </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .big-font {
            font-size:50px !important;
        }
        </style>
    """, unsafe_allow_html=True)

# Fungsi Untuk Halaman Profil Petani
def petani():
    st.title("Profil Petani")
    Id_Petani = st.text_input("Masukkan Id Petani")
    Jenis_Penyulingan = st.text_input("Masukkan Jenis Penyulingan")
    Nama_Petani= st.text_input("Masukkan Nama")
    Desa = st.text_input("Masukkan Desa")
    Kecamatan = st.text_input("Masukkan Kecamatan")
    Kabupaten = st.text_input("Masukkan Kabupaten")
    Tanggal_penyulingan = st.date_input("Tangggal Penyulingan")
    Tanggal_penjualan = st.date_input("Tanggal Penjualan")
    Jumlah_Penjualan_Minyak = st.text_input("Masukkan jumlah penjualan minyak")
    if st.button("Tambah Profil Petani"):
        add_petani(Id_Petani, Nama_Petani, Desa, Kecamatan, Kabupaten, Tanggal_penyulingan, Tanggal_penjualan, Jenis_Penyulingan, Jumlah_Penjualan_Minyak)
        st.success("Pelacakan berhasil ditambahkan.")

# Fungsi untuk menambahkan Petani ke database
def add_petani(Id_Petani, Nama_Petani, Desa, Kecamatan, Kabupaten, Tanggal_penyulingan, Tanggal_penjualan, Jenis_Penyulingan, Jumlah_Penjualan_Minyak):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Petani (Id_Petani, Nama_Petani, Desa, Kecamatan, Kabupaten, Tanggal_penyulingan, Tanggal_penjualan, Jenis_Penyulingan, Jumlah_Penjualan_Minyak) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                            (Id_Petani, Nama_Petani, Desa, Kecamatan, Kabupaten,  Tanggal_penyulingan, Tanggal_penjualan, Jenis_Penyulingan, Jumlah_Penjualan_Minyak))
            conn.commit()                
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")

# Fungsi untuk mendapatkan ID Produksi dari database
def get_ids_from_db(query):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return [row[0] for row in results]
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")
        return []

def get_ids_from_db(query):
    conn = sqlite3.connect('data_nilam.db', timeout=10)  # Menambahkan timeout
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    conn.close()
    return [item[0] for item in data]

# Fungsi Halaman Untuk Produksi
def penyulingan():
    st.title("Produksi/Penyulingan Nilam")
    Id_Penyulingan = st.text_input("Id Produksi/Penyulingan")
    Id_Minyak_Nilam = st.text_input("Masukkan Id Minyak Nilam")
    Jenis_Penyulingan = st.text_input("Masukkan Jenis Penyulingan")
    Jumlah_Minyak = st.text_input("Masukkan jumlah Minyak")
    Kadar_PA = st.text_input("Masukkan Kadar_PA")
    Lokasi = st.text_input("Masukkan Lokasi")
    Tanggal_Penyulingan = st.date_input("Tanggal Penyulingan")
    Tanggal_Penjualan = st.date_input("Tanggal Penjualan")
    if st.button("Tambah Penyulingan"):
        add_penyulingan(Id_Penyulingan, Id_Minyak_Nilam, Jenis_Penyulingan, Jumlah_Minyak, Kadar_PA, Lokasi, Tanggal_Penyulingan, Tanggal_Penjualan)
        st.success("Pelacakan berhasil ditambahkan.")

# Fungsi untuk menambahkan penyulingan ke database
def add_penyulingan(Id_Penyulingan, Id_Minyak_Nilam, Jenis_Penyulingan, Jumlah_Minyak, Kadar_PA, Lokasi, Tanggal_Penyulingan, Tanggal_Penjualan):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Penyulingan (Id_Penyulingan, Id_Minyak_Nilam, Jenis_Penyulingan, Jumlah_Minyak, Kadar_PA, Lokasi, Tanggal_Penyulingan, Tanggal_Penjualan) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                           (Id_Penyulingan, Id_Minyak_Nilam, Jenis_Penyulingan, Jumlah_Minyak, Kadar_PA, Lokasi, Tanggal_Penyulingan, Tanggal_Penjualan))
            conn.commit()
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")

# Fungsi untuk mendapatkan ID Produksi dari database
def get_ids_from_db(query):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return [row[0] for row in results]
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")
        return []

def get_ids_from_db(query):
    conn = sqlite3.connect('data_nilam.db', timeout=10)  # Menambahkan timeout
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    conn.close()
    return [item[0] for item in data]

def get_ids_from_db(query):
    conn = sqlite3.connect('data_nilam.db', timeout=10)  # Menambahkan timeout
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    conn.close()
    return [item[0] for item in data]

def pengepul_1():
    st.title("Pengepul Nilam 1")
    Id_Petani_list = get_ids_from_db("SELECT Id_Petani FROM Table_Petani")
    Id_Petani = st.selectbox("Id_Petani", Id_Petani_list)
    Id_Pengepul_1= st.text_input("Id Pengepul 1")
    Id_Penyulingan = st.text_input("Masukkan Id Penyulingan")
    Tanggal_Pembelian = st.date_input("Tanggal Pembelian")
    Jp_Minyak_Dibeli = st.text_input("Masukkan Jumlah Minyak Yang dibeli ")
    Jumlah_Pembelian = st.text_input("Jumlah Pembelian")
    Kadar_PA_Pembelian = st.text_input("Masukkan Kadar PA Pembelian(%)")
    Tanggal_Penjualan = st.date_input("Tanggal Penjualan")
    Kadar_PA_Penjualan = st.text_input("Masukkan Kadar PA Penjualan(%)")
    Jumlah_Penjualan = st.text_input("Masukkan Jumlah Penjualan")
    if st.button("Tambah Pengepul 1"):
        add_pengepul_1(Id_Petani, Id_Pengepul_1, Id_Penyulingan, Tanggal_Pembelian, Jp_Minyak_Dibeli, Jumlah_Pembelian, Kadar_PA_Pembelian, Tanggal_Penjualan, Kadar_PA_Penjualan, Jumlah_Penjualan)
        st.success("Pelacakan berhasil ditambahkan.")

def pengepul_2():
    st.title("Pengepul Nilam 2")
    Id_Petani_list = get_ids_from_db("SELECT Id_Petani FROM Table_Petani")
    Id_Pengepul_1_list = get_ids_from_db("SELECT Id_Pengepul_1 FROM Table_Pengepul_1")
    Kadar_PA_list = get_ids_from_db("SELECT Kadar_PA FROM Table_Penyulingan")
    Id_Petani = st.selectbox("Id_Petani", Id_Petani_list)
    Id_Pengepul_1 = st.selectbox("Id_Pengepul_1", Id_Pengepul_1_list)
    Kadar_PA_Pembelian = st.selectbox("Id_Kadar_PA(%)", Kadar_PA_list)
    Id_Pengepul_2 = st.text_input("Masukkan Id Pengepul 2")
    Id_Penyulingan = st.text_input("Masukkan Id Penyulingan")
    Jenis_Penyulingan = st.text_input("Masukkan Jenis Penyulingan")
    Tanggal_Pembelian = st.date_input("Masukkan Tanggal Pembelian")
    Jumlah_Pembelian = st.text_input("Masukkan Jumlah Pembelian")
    Tanggal_Penjualan = st.date_input("Masukkan Tanggal Penjualan")
    Jumlah_Penjualan = st.text_input("Masukkan Jumlah Penjualan")
    Kadar_PA_Penjualan = st.text_input("Masukkan Kadar PA Penjualan")
    if st.button("Tambah Pengepul 2"):
        add_pengepul_2(Id_Petani, Id_Pengepul_1, Id_Pengepul_2, Id_Penyulingan, Jenis_Penyulingan, Tanggal_Pembelian, Kadar_PA_Pembelian, Jumlah_Pembelian, Jumlah_Penjualan, Tanggal_Penjualan, Kadar_PA_Penjualan)
        st.success("Pelacakan berhasil ditambahkan.")

# Fungsi Halaman Membuat Detail Qr code Produk Minyak Nilam
def minyaknilam():
    st.title("Detail Qrcode Minyak Nilam")
    Id_Minyak_Nilam_list = get_ids_from_db ("SELECT Id_Minyak_Nilam FROM Table_Penyulingan")
    Id_Minyak_Nilam = st.selectbox("Id_Minyak_Nilam", Id_Minyak_Nilam_list)
    Nama_Petani_Penyuling = st.text_input("Masukkan Nama Petani atau Penyuling")
    Jenis_Penyulingan = st.text_input("Masukkan Jenis Penyulingan")
    Jumlah_minyak = st.text_input("Masukkan jumlah Minyak")
    Lokasi = st.text_input("Masukkan Lokasi")
    Nama_Pengepul_12 = st.text_input("Masukkan Nama Pengepul 1/2")
    Tanggal_Penjualan_ke_Pengepul_12 = st.date_input("Tanggal_Penjualan_ke_Pengepul_1/2")
    if st.button("Tambah detail Qrcode"):
        add_minyaknilam(Id_Minyak_Nilam, Nama_Petani_Penyuling, Jenis_Penyulingan, Jumlah_minyak, Lokasi, Nama_Pengepul_12, Tanggal_Penjualan_ke_Pengepul_12)
        st.success("Pelacakan berhasil ditambahkan.")

# Fungsi untuk menambahkan Pengepul_1 ke database
def add_pengepul_1(Id_Petani, Id_Pengepul_1, Id_Produksi, Tanggal_Pembelian, Jp_Minyak_Dibeli, Jumlah_Pembelian, Kadar_PA_Pembelian, Tanggal_Penjualan, Kadar_PA_Penjualan, Jumlah_Penjualan):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Pengepul_1 (Id_Petani, Id_Pengepul_1, Id_Produksi, Tanggal_Pembelian, Jp_Minyak_Dibeli, Jumlah_Pembelian, Kadar_PA_Pembelian, Tanggal_Penjualan, Kadar_PA_Penjualan, Jumlah_Penjualan) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                           (Id_Petani, Id_Pengepul_1, Id_Produksi, Tanggal_Pembelian, Jp_Minyak_Dibeli, Jumlah_Pembelian, Kadar_PA_Pembelian, Tanggal_Penjualan, Kadar_PA_Penjualan, Jumlah_Penjualan))
            conn.commit()
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")

# Fungsi untuk menambahkan Pengepul 2 ke database
def add_pengepul_2(Id_Petani, Id_Pengepul_1, Id_Pengepul_2, Id_Penyulingan, Jenis_Penyulingan, Tanggal_Pembelian, Kadar_PA_Pembelian, Jumlah_Pembelian, Jumlah_Penjualan, Tanggal_Penjualan, Kadar_PA_Penjualan):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Pengepul_2 (Id_Petani, Id_Pengepul_1, Id_Pengepul_2, Id_Penyulingan, Jenis_Penyulingan, Tanggal_Pembelian, Kadar_PA_Pembelian) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                           (Id_Petani, Id_Pengepul_1, Id_Pengepul_2, Id_Penyulingan, Jenis_Penyulingan, Kadar_PA_Pembelian, Tanggal_Pembelian, Jumlah_Pembelian, Jumlah_Penjualan, Tanggal_Penjualan, Kadar_PA_Penjualan))
            conn.commit()
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")

# Fungsi untuk menambahkan detail minyak nilam ke database
def add_minyaknilam(Id_Minyak_Nilam, Nama_Petani_Penyuling, Jenis_Penyulingan, Jumlah_minyak, Lokasi, Nama_Pengepul_12, Tanggal_Penjualan_ke_Pengepul_12):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Minyak_Nilam (Id_Minyak_Nilam, Nama_Petani_Penyuling, Jenis_Penyulingan, Jumlah_minyak, Lokasi, Nama_Pengepul_12, Tanggal_Penjualan_ke_Pengepul_12) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                           (Id_Minyak_Nilam, Nama_Petani_Penyuling, Jenis_Penyulingan, Jumlah_minyak, Lokasi, Nama_Pengepul_12, Tanggal_Penjualan_ke_Pengepul_12))
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")

def get_ids_from_db(query):
    conn = sqlite3.connect('data_nilam.db', timeout=10)  # Menambahkan timeout
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    conn.close()
    return [item[0] for item in data]
    
# Fungsi untuk mendapatkan informasi lain dari database berdasarkan query
def get_name_from_db(query):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0] if result else None
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")
        return None

# Fungsi umum untuk menjalankan query dan mendapatkan hasilnya
def query_db(query):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")
        return []
    
# Fungsi untuk mendapatkan kolom berdasarkan nama tabel
def columns_for_table(table_name):
    columns_dict = {
        'Table_Petani': ["Id_Petani"],
        'Table_Penyulingan': ["Id_Penyulingan"],
        'Table_Pengepul_1': ["Id_Pengepul_1"],
        'Table_Pengepul_2': ["Id_Pengepul_2"],    
        'Table_Minyak_Nilam': ["Id_Minyak_Nilam"],    
    }
    return columns_dict.get(table_name, ["Id"])

# Fungsi untuk mengambil data penyulingan berdasarkan Id_Penyuling
def get_product_info(Id_Penyulingan):
    conn = sqlite3.connect('data_nilam.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Table_Penyulingan WHERE Id_Penyulingan=?", (Id_Penyulingan,))
    data = cursor.fetchone()

    conn.close()
    return data

# Fungsi untuk mengambil data Minyak Nilam berdasarkan Id_Minyak_Nilam
def get_product_from_db(Id_Minyak_Nilam):
    conn = sqlite3.connect('data_nilam.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Table_Minyak_Nilam WHERE Id_Minyak_Nilam=?", (Id_Minyak_Nilam,))
    data = cursor.fetchone()

    conn.close()
    return data

# Path untuk menyimpan QR code yang dihasilkan
generated_qrcodes_path = "qr_codes"

# Fungsi untuk halaman Generate QR Code
def generate():
    st.title("QR Code Generator")
     
    # Input penyulingan dari pengguna
    Id_Penyulingan_list = get_ids_from_db("SELECT Id_Penyulingan FROM Table_Penyulingan")
    Id_Penyulingan = st.selectbox("Id_Penyulingan", Id_Penyulingan_list)
    
    if Id_Penyulingan:
        # Mendapatkan tanggal produksi berdasarkan Id_Penyulingan yang dipilih
        Tanggal_Penjualan = get_name_from_db(f"SELECT Tanggal_Penjualan FROM Table_Penyulingan WHERE Id_Penyulingan = '{Id_Penyulingan}'")
        
        if Tanggal_Penjualan:
            st.write(f"Tanggal_Penjualan_ke_Pengepul_12: {Tanggal_Penjualan}") 
            
            if st.button("Generate QR Code"):
                # Generate QR code data
                link = "https://webminyaknilam.streamlit.app//?"
                data = f"{link}Id_Penyulingan={Id_Penyulingan}"
                qr_image = segno.make(data)

                # Menyimpan gambar QR code sementara
                if not os.path.exists(generated_qrcodes_path):
                    os.makedirs(generated_qrcodes_path)
                    
                qr_file_path = os.path.join(generated_qrcodes_path, f"qr_code_{Tanggal_Penjualan}.png")
                qr_image.save(qr_file_path)

                # Menampilkan QR code di Streamlit
                st.image(qr_file_path, caption=" Hasil Qr Code Untuk Id Penyulingan", use_column_width=False)
                
                # Menampilkan informasi terkait (gabungan Id Produksi dan link)
                st.write(f"{link}Id_Penyulingan={Id_Penyulingan}")
        
                # Tombol untuk menyimpan QR code
                with open(qr_file_path, "rb") as file:
                    st.download_button(
                        label="Download QR Code",
                        data=file,
                        file_name=f"qr_code_{Id_Penyulingan}.png",
                        mime="image/png"
                    )
        else:
            st.error("Tanggal Penjualan ke Pengepul 1 atau 2 tidak ditemukan. Pastikan Id Mianyak Nlam valid.")

# Fungsi untuk halaman Penelusuran
def penelusuran(Id_Penyulingan=None):
    conn = sqlite3.connect('data_nilam.db')
    cursor = conn.cursor()

# Membuat tabel Table_Penyulingan dengan struktur yang diperbarui
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Table_Penyulingan (
            Id_Penyulingan TEXT PRIMARY KEY,
            Id_Minyak_Nilam TEXT PRIMARY KEY,
            Jenis_Penyulingan TEXT,
            Jumlah_Minyak TEXT,
            Kadar_PA TEXT,
            Lokasi TEXT,
            Tanggal_Penyulingan TEXT,
            Tanggal_Penjualan TEXT
                            )
    ''')

    # Membuat tabel produk untuk detail produk
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Table_Minyak_Nilam (
            Id_Minyak_Nilam TEXT PRIMARY KEY,
            Nama_Petani_atau_Penyuling TEXT,
            Jenis_Penyulingan TEXT,
            Jumlah_Minyak TEXT,
            Lokasi TEXT,
            Nama_Pengepul_12 TEXT,
            Tanggal_Penjualan_ke_Pengepul TEXT,
            Gambar BLOB 
                            )
    ''')

    conn.commit()
    conn.close()
    if Id_Penyulingan:
        product_info = get_product_info(Id_Penyulingan) 

        if product_info:
            st.write(f"**Tanggal Penyulingan:** {product_info[7]}")
            
            # Menampilkan detail produk dari Id_Minyak_Nilam
            id_minyak_nilam_to_view = product_info[1]
            if id_minyak_nilam_to_view:
                product_info_detail = get_product_from_db(id_minyak_nilam_to_view)
                if product_info_detail:
                    st.write(f"**Nama Petani atau Penyuling:** {product_info_detail[1]}")
                    st.write(f"**Jenis Penyulingan:** {product_info_detail[2]}")
                    st.write(f"**Jumlah_Minyak:** {product_info_detail[3]}")
                    st.write(f"**Lokasi:** {product_info_detail[4]}")
                    st.write(f"**Nama Pengepul 1 atau 2:** {product_info_detail[6]}")
                    st.write(f"**Tanggal Penjualan ke pengepul 1 atau 2:** {product_info_detail[5]}")

                    # Menampilkan gambar jika ada
                    if product_info_detail[8]:
                        image_db = Image.open(io.BytesIO(product_info_detail[8]))
                        st.image(image_db, caption='Gambar dari Database SQLite', use_column_width=True)
                    else:
                        st.info("Tidak ada gambar untuk produk ini.")
                else:
                    st.error("Data penyulingan tidak ditemukan!")
            else:
                st.warning("ID Produk tidak ditemukan.")
            
             # Menampilkan peta lokasi petani
            st.header("Alamat Petani Nilam Aceh")

            # Koordinat lokasi Pemasok
            lokasi = [723.7565169210094, 95.58097307482704]  # Lokasi aceh jaya

            # Kunci API Mapbox (Ganti dengan kunci API Anda sendiri)
            pdk.settings.api_key = "YOUR_MAPBOX_API_KEY"

            # Buat layer peta untuk lokasi pasar dengan marker besar
            marker_layer = pdk.Layer(
                "ScatterplotLayer",
                data=[{"position": lokasi, "name": "Krueng Sabee"}],
                get_position="position",
                get_fill_color=[255, 0, 0],  # Merah untuk marker
                get_radius=10000,  # Radius besar untuk visibilitas
                pickable=True,
                auto_highlight=True
            )

            # Buat layer teks untuk label
            text_layer = pdk.Layer(
                "TextLayer",
                data=[{"position": lokasi, "name": "Krueng Sabee"}],
                get_position="position",
                get_text="name",
                get_size=16,
                get_color=[0, 0, 0],  # Warna teks hitam
                get_text_anchor="middle",
                get_alignment_baseline="center",
            )

            # Set peta dan tampilan dengan gaya peta dari Mapbox
            peta = pdk.Deck(
                layers=[marker_layer, text_layer],
                initial_view_state=pdk.ViewState(
                    latitude=lokasi[0],
                    longitude=lokasi[1],
                    zoom=17,  # Zoom sesuai dengan link Google Maps
                    pitch=0,
                ),
                map_style="mapbox://styles/mapbox/outdoors-v12"  # Gaya peta global
            )

            # Tampilkan peta di Streamlit
            st.pydeck_chart(peta)
                # Link ke halaman utama perusahaan
            st.markdown("[Kunjungi Home web minyak nilam](#ISI LINK)")

        else:
            st.error('Data produksi tidak ditemukan!')
    else:
        st.error('ID Produksi tidak ditemukan.')

def signup():
    st.write("Sign Up Page")
    username = st.text_input("New Username")
    email = st.text_input("Email")
    password = st.text_input("New Password", type="password")
    role = st.selectbox("Role", ["Administrasi", "Retailer", "Distribusi"])
    
    if st.button("Sign Up"):
        conn = sqlite3.connect('data_nilam.db')
        c = conn.cursor()
        
        if role == "Petani":
            table_name = 'petani_users'
        elif role == "Penyulingan":
            table_name = 'penyulingan_users'
        elif role == "Pengepul 1":
            table_name = 'pengepul1_users'
        elif role == "Pengepul 2":
            table_name = 'pengepul2_users'
        
        c.execute(f'INSERT INTO {table_name} (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()
        st.success("User created successfully")

# Fungsi untuk log out
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.sidebar.success("Anda telah berhasil keluar. Menuju ke halaman Home...")
    st.session_state.page = "Home"  # Set halaman tujuan setelah logout

def login():
    st.title("Login Page")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Login as", ["Petani", "Penyulingan", "Pengepul 1", "Pengepul 2"])
    
    if st.button("Login"):
        conn = sqlite3.connect('data_nilam.db')
        c = conn.cursor()
        
        if role == "Petani":
            table_name = 'petani_users'
        elif role == "Penyulingan":
            table_name = 'penyulingan_users'
        elif role == "Pengepul 1":
            table_name = 'pengepul1_users'
        elif role == "Pengepul 2":
            table_name = 'pengepul2_users'
        
        # Assuming hashed_password is directly used; in a real application, it should be hashed
        hashed_password = password
        c.execute(f'SELECT * FROM {table_name} WHERE email = ? AND password = ?', (email, hashed_password))
        user = c.fetchone()
        conn.close()
        
        if user:
            st.session_state.logged_in = True
            st.session_state.role = role.lower()  # store role in lowercase to match with menu conditions
            st.rerun() #  Refresh the page to show the correct menu
        else:
            st.error("Invalid credentials")
    
def main():
    # Initialize session state if not already set
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.role = ""

    st.sidebar.title("Navigasi")
    
    # Periksa query params ketika aplikasi dijalankan
    query_params= st.query_params.to_dict()
    Id_Penyulingan = query_params.get('Id_Penyulingan', [None][0])

    # Jika Id_Produksi diberikan di URL, langsung ke halaman Penelusuran
    if  Id_Penyulingan:
         penelusuran(Id_Penyulingan)
         return  # Exit the main function to prevent further processing
    
    if st.session_state.logged_in:
        if st.session_state.role == "petani":
            menu = ["Home", "Petani", "Log Out"]
        elif st.session_state.role  == "penyulingan":
            menu = ["Home", "Penyulingan", "Log Out"]
        elif st.session_state.role  == "pengepul 1":
            menu = ["Home", "Pengepul 1", "Log Out"]
        elif st.session_state.role  == "pengepul 2":
            menu = ["Home", "Penelusuran", "Petani", "Generate QR code", "Penyulingan", "Pengepul 1", "Pengepul 2", "Minyak Nilam", "SignUp", "Log Out"]
    else:
        menu = ["Home", "Login"]
    
    choice = st.sidebar.selectbox("Navigasi", menu)

    if choice == "Home":
        home()
    elif choice == "Login":
        login()
    elif choice == "SignUp" and st.session_state.logged_in:
        signup()
    elif choice == "Penelusuran":
        penelusuran()
    elif choice == "Generate QR code" and st.session_state.logged_in:
        generate()
    elif choice == "Petani" and st.session_state.logged_in:
        petani()
    elif choice == "Penyulingan" and st.session_state.logged_in:
        penyulingan()
    elif choice == "Pengepul 1" and st.session_state.logged_in:
        pengepul_1()
    elif choice == "Pengepul 2" and st.session_state.logged_in:
        pengepul_2()
    elif choice == "Minyak Nilam" and st.session_state.logged_in:
        minyaknilam()
    elif choice == "Log Out" and st.session_state.logged_in:
        logout()
        home()  # Redirect to Home page after logout
    else:
        st.sidebar.warning("Silakan login terlebih dahulu untuk mengakses halaman ini.")
        
if __name__ == '__main__':
    main()
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)



