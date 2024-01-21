import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = '5220411112_kevina_maydiva_heriansaputri'

def connect_db():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor, table_name, columns):
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cursor.execute(query)

def main():
    conn, cursor = connect_db()


    create_table(cursor, "film_kevina", """
        Id INT AUTO_INCREMENT PRIMARY KEY,
        judul VARCHAR(222) NOT NULL,
        tahun VARCHAR(222) NOT NULL
    """)
    print("Table film_kevina created successfully")


    create_table(cursor, "studio_kevina", """
        Id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(222) NOT NULL,
        kapasitas VARCHAR(222) NOT NULL
    """)
    print("Table studio_kevina created successfully")

    create_table(cursor, "tiket_kevina", """
        Id INT AUTO_INCREMENT PRIMARY KEY,
        studio_id INT NOT NULL,
        film_id INT NOT NULL,
        tanggal DATE NOT NULL,
        jam_tayang VARCHAR(222) NOT NULL,
        jam_selesai VARCHAR(222) NOT NULL,
        harga VARCHAR(222) NOT NULL,
        FOREIGN KEY (studio_id) REFERENCES studio_kevina (Id),
        FOREIGN KEY (film_id) REFERENCES film_kevina (Id)
    """)
    print("Table tiket_kevina created successfully")


    create_table(cursor, "tr_penjualan_kevina", """
        Id INT AUTO_INCREMENT PRIMARY KEY,
        tiket_id INT NOT NULL,
        jumlah VARCHAR(222) NOT NULL,
        bayar VARCHAR(222) NOT NULL,
        kembalian VARCHAR(222) NOT NULL,
        tanggal DATE NOT NULL,
        FOREIGN KEY (tiket_id) REFERENCES tiket_kevina (Id)
    """)
    print("Table tr_penjualan_kevina created successfully")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()