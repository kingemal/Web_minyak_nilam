#fungsi halaman Lokasi
def lokasi():
    st.title("Lokasi Minyak Nilam")
    Id_Nilam = st.text_input("Id Nilam")
    Lokasi = st.text_input("Masukkan Lokasi")
    if st.button("Tambah Lokasi"):
        add_lokasi(Id_Nilam, Lokasi)
        st.success("Pelacakan berhasil ditambahkan.")

# Fungsi untuk menambahkan jejak traceability Lokasi ke database
def add_traceability(Id_Nilam, Lokasi):
    try:
        with sqlite3.connect('data_nilam.db', timeout=10) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Lokasi (Id_Nilam, Lokasi) VALUES (?, ?)',
                           (Id_Nilam, Lokasi))
            conn.commit()
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")

# Fungsi untuk menambahkan Pengepul_1 ke database
def add_lokasi(id_Nilam, Lokasi):
    try:
        with sqlite3.connect('data_nilam.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Table_Lokasi (id_Nilam, Lokasi) VALUES (?, ?)', 
                           (id_Nilam, Lokasi))
            conn.commit()
    except sqlite3.Error as e:
        st.error(f"Kesalahan database: {e}")

# Fungsi untuk mendapatkan semua petani dari database
def get_all_petani():
    return query_db('SELECT Id_Petani, Nama, Asal, Alamat FROM Table_Petani')

# Fungsi untuk mendapatkan semua produksi dari database
def get_all_produksi():
    return query_db('SELECT Id_Produksi, Luas_lahan, Jumlah_daun, Jumlah_Minyak, Tanggal_Produksi FROM Table_Produksi')

# Fungsi untuk mendapatkan semua lokasi dari database
def get_all_lokasi():
    return query_db('SELECT Id_Nilam, Lokasi FROM Table_Lokasi')

# Fungsi untuk mendapatkan semua pengepul_1 dari database
def get_all_pengepul_1():
    return query_db('SELECT Id_Petani, Id_Pengepul_1, Id_produksi, Nama, Id_Nilam, Jumlah_Pasokan FROM Table_Pengepul_1')

# Fungsi untuk mendapatkan semua pengepul_2 dari database
def get_all_pengepul_2():
    return query_db('SELECT Id_Petani, Id_Pengepul_2, Id_produksi, Nama, Id_Nilam, Jumlah_Pasokan FROM Table_Pengepul_2')