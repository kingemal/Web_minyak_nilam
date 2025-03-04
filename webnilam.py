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
    Nama = st.text_input("Masukkan Nama")
    Desa = st.text_input("Masukkan Desa")
    Kecamatan = st.text_input("Masukkan Kecamatan")
    Kabupaten = st.text_input("Masukkan Kabupaten")
    Tanggal_penyulingan = st.date_input("Tangggal Penyulingan")
    Tanggal_penjualan = st.date_input("Tanggal Penjualan")
    Jumlah_Penjualan_Minyak = st.text_input("Masukkan jumlah penjualan minyak")
    if st.button("Tambah Profil Petani"):
        add_petani(Id_Petani, Nama, Desa, Kecamatan, Kabupaten, Tanggal_penyulingan, Tanggal_penjualan, Jenis_Penyulingan, Jumlah_Penjualan_Minyak)
        st.success("Pelacakan berhasil ditambahkan.")

# Fungsi untuk menambahkan Petani ke database
def add_petani(Id_Petani, Nama, Desa, Kecamatan, Kabupaten, Tanggal_penyulingan, Tanggal_penjualan, Jenis_Penyulingan, Jumlah_Penjualan_Minyak):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Petani (Id_Petani, Nama, Desa, Kecamatan, Kabupaten, Tanggal_penyulingan, Tanggal_penjualan, Jenis_Penyulingan, Jumlah_Penjualan_Minyak) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                            (Id_Petani, Nama, Desa, Kecamatan, Kabupaten,  Tanggal_penyulingan, Tanggal_penjualan, Jenis_Penyulingan, Jumlah_Penjualan_Minyak))
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
def penyuling():
    st.title("Produksi/Penyulingan Nilam")
    Id_Penyulingan = st.text_input("Id Produksi/Penyulingan")
    Jenis_Penyulingan = st.text_input("Masukkan Jenis Penyulingan")
    Jumlah_minyak = st.text_input("Masukkan jumlah Minyak")
    Kadar_PA = st.text_input("Masukkan Kadar_PA")
    Lokasi = st.text_input("Masukkan Lokasi")
    Tanggal_Penyulingan = st.date_input("Tanggal Penyulingan")
    Tanggal_Penjualan = st.date_input("Tanggal Penjualan")
    if st.button("Tambah Penyulingan"):
        add_penyulingan(Id_Penyulingan, Jenis_Penyulingan, Jumlah_minyak, Kadar_PA, Lokasi, Tanggal_Penyulingan, Tanggal_Penjualan)
        st.success("Pelacakan berhasil ditambahkan.")

# Fungsi untuk menambahkan Produksi ke database
def add_penyulingan(Id_Penyulingan, Jenis_Penyulingan, Jumlah_Minyak, Kadar_PA, Lokasi, Tanggal_Penyulingan, Tanggal_Penjualan):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Penyulingan (Id_Penyulingan, Jenis_Penyulingan, Jumlah_Minyak, Kadar_PA, Lokasi, Tanggal_Penyulingan, Tanggal_Penjualan) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                           (Id_Penyulingan, Jenis_Penyulingan, Jumlah_Minyak, Kadar_PA, Lokasi, Tanggal_Penyulingan, Tanggal_Penjualan))
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

# Fungsi untuk menambahkan jejak traceability Petani ke database
def add_traceability(Id_Petani, Nama, Asal, Alamat, Hasil_Panen):
    try:
        with sqlite3.connect('data_nilam.db', timeout=10) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Petani ( Id_Petani, Nama, Asal, Alamat, Hasil_Panen) VALUES (?, ?, ?, ?, ?, ? )',
                            ( Id_Petani, Nama, Asal, Alamat, Hasil_Panen))
            conn.commit()
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")

def get_ids_from_db(query):
    conn = sqlite3.connect('data_nilam.db', timeout=10)  # Menambahkan timeout
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    conn.close()
    return [item[0] for item in data]
    
# Fungsi untuk menambahkan jejak traceability Produksi ke database
def add_traceability(Id_Produksi, Luas_lahan, Jumlah_minyak, Tanggal_Produksi, Tanggal_penjualan):
    try:
        with sqlite3.connect('data_nilam.db', timeout=10) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Produksi (Id_Produksi, Luas_lahan, Jumlah_minyak, Tanggal_Produksi, Tanggal_penjualan) VALUES (?, ?, ?, ?, ?)',
                            (Id_Produksi, Luas_lahan, Jumlah_minyak, Tanggal_Produksi, Tanggal_penjualan))
            conn.commit()
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")

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
    }
    return columns_dict.get(table_name, ["Id"])

# Fungsi untuk mengambil data Penyulingan berdasarkan Id_Penyulingan
def get_product_info(Id_Penyulingan):
    conn = sqlite3.connect('data_nilam.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Table_Penyulingan WHERE Id_Penyulingan=?", (Id_Penyulingan,))
    data = cursor.fetchone()

    conn.close()
    return data

# Fungsi untuk mengambil data produk berdasarkan Id_Produk
def get_product_from_db(Id_Penyulingan):
    conn = sqlite3.connect('data_')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Table_Penyulingan WHERE Id_Penyulingan=?", (Id_Penyulingan,))
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
        # Mendapatkan tanggal produksi berdasarkan Id_Produksi yang dipilih
        Tanggal_Penyulingan = get_name_from_db(f"SELECT Tanggal_Penyulingan FROM Table_Penyulingan WHERE Id_Penyulingan = '{Id_Penyulingan}'")
        
        if Tanggal_Penyulingan:
            st.write(f"Tanggal_Penyulingan: {Tanggal_Penyulingan}") 
            
            if st.button("Generate QR Code"):
                # Generate QR code data
                link = "https://webminyaknilam.streamlit.app//?"
                data = f"{link}Id_Penyulingan={Id_Penyulingan}"
                qr_image = segno.make(data)

                # Menyimpan gambar QR code sementara
                if not os.path.exists(generated_qrcodes_path):
                    os.makedirs(generated_qrcodes_path)
                    
                qr_file_path = os.path.join(generated_qrcodes_path, f"qr_code_{Tanggal_Penyulingan}.png")
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
            st.error("Tanggal penyulingan tidak ditemukan. Pastikan Id Penyulingan valid.")

# Fungsi untuk halaman Penelusuran
def penelusuran(Id_Penyulingan=None):
    conn = sqlite3.connect('data_nilam.db')
    cursor = conn.cursor()

# Membuat tabel Table_Penyulingan dengan struktur yang diperbarui
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Table_Penyulingan (
            Id_Penyulingan TEXT PRIMARY KEY,
            Jenis_Penyulingan TEXT,
            Jumlah_Minyak TEXT,
            Kadar_PA TEXT,
            Lokasi INTEGER,
            Tanggal_Penyulingan INTEGER,
            Tanggal_Penjualan INTEGER
        )
    ''')

    # Membuat tabel produk untuk detail produk
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Table_Minyak_Nilam (
            Id_Produk TEXT PRIMARY KEY,
            Nama_Produk TEXT,
            Bau TEXT,
            Kadar Minyak TEXT,
            Gambar BLOB
                    )
    ''')

    conn.commit()
    conn.close()
    if Id_Penyulingan:
        product_info = get_product_info(Id_Penyulingan) 
        if product_info:
            st.write(f"**Tanggal Penyulingan:** {product_info[7]}")
            
            # Menampilkan detail produk dari Id_
            Id_Penyulingan_to_view = product_info[1]
            if Id_Penyulingan_to_view:
                product_info_detail = get_product_from_db(Id_Penyulingan_to_view)
                if product_info_detail:
                    st.write(f"**Nama Petani:** {product_info_detail[1]}")
                    st.write(f"*Asal Produk:** {product_info_detail[2]}")
                    st.write(f"**Kadar Minyak:** {product_info_detail[3]}")
                    
                    # Menampilkan gambar jika ada
                    if product_info_detail[4]:
                        image_db = Image.open(io.BytesIO(product_info_detail[4]))
                        st.image(image_db, caption='Gambar dari Database SQLite', use_column_width=True)
                    else:
                        st.info("Tidak ada gambar untuk produk ini.")
                else:
                    st.error("Data penyulingan tidak ditemukan!")
            else:
                st.warning("ID Produk tidak ditemukan.")
            
             # Menampilkan peta lokasi pemasok
            st.header("Alamat Pemasok Nilam Aceh")

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
            st.markdown("[Kunjungi Home Perusahaan](#ISI LINK PERUSAHAAN)")

        else:
            st.error('Data produksi tidak ditemukan!')
    else:
        st.error('ID Produksi tidak ditemukan.')

def main():
    st.sidebar.title("Navigasi")
    menu = ["Home", "Penelusuran", "Generate QR code", "Petani", "Penyuling", "Pengepul 1", "Pengepul 2"]
    page = st.sidebar.selectbox("MENU", menu) 
    st.sidebar.info("SELAMAT DATANG USER MINYAK NILAM")

    if page == "Home":
        home()
    elif page == "Penelusuran":
        penelusuran()
    elif page == "Generate QR code":
        generate()
    elif page == "Petani": 
        petani()
    elif page == "Penyuling":
        penyuling()
    elif page == "Pengepul 1":
        pengepul_1()
    elif page == "Pengepul 2": 
        pengepul_2()
    elif page== "Home":
        home()  # Redirect to Home page after logout
        
if __name__ == '__main__':
    main()
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
   



