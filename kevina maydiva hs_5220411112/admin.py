import mysql.connector
from datetime import datetime

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = '5220411112_kevina_maydiva_heriansaputri'

class Crud:
    @staticmethod
    def connect_db():
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def studio():
        conn, cursor = Crud.connect_db()
        studio = input("Masukkan Nama Studio: ")
        kapasitas = input("Masukkan kapasitas Studio: ")
        
        query_check = "SELECT * FROM studio_kevina WHERE nama = %s"
        cursor.execute(query_check, (studio,))
        result = cursor.fetchall()
    
        if result:
            print("Nama Telah Tersedia !!!")
        else:
            query = "INSERT INTO studio_kevina (nama, kapasitas) VALUES (%s, %s)"
            values = (studio, kapasitas)
            cursor.execute(query, values)
            conn.commit()
            print(f"Data telah ditambahkan ke studio_kevina")

        
    @staticmethod
    def hapus_studio():
        conn, cursor = Crud.connect_db()
        studio_nama = input("Masukkan Nama Studio yang ingin dihapus: ")
        query = "DELETE FROM studio_kevina WHERE nama = %s"
        cursor.execute(query, (studio_nama,))
        conn.commit()
        print(f"Studio dengan nama {studio_nama} telah dihapus dari studio_kevina")

    @staticmethod
    def edit_studio():
        conn, cursor = Crud.connect_db()
        studio_nama = input("Masukkan Nama Studio yang ingin diedit: ")
        kapasitas = input("Masukkan Kapasita Studio yang baru:")
        query = "UPDATE studio_kevina SET kapasitas = %s WHERE nama = %s"
        cursor.execute(query, (kapasitas,studio_nama,))
        conn.commit()
        print(f"Studio dengan nama {studio_nama} telah diedit menjadi berkapasitas {kapasitas}")

    @staticmethod
    def tambah_film():
        conn, cursor = Crud.connect_db()
        judul = input("Masukkan Judul Film: ")
        tahun = input("Masukkan Tahun Rilis Film: ")
        query = "INSERT INTO film_kevina (judul, tahun) VALUES (%s, %s)"
        values = (judul, tahun)
        cursor.execute(query, values)
        conn.commit()
        print(f"Data telah ditambahkan ke film_kevina")

    @staticmethod
    def hapus_film():
        conn, cursor = Crud.connect_db()
        film_judul = input("Masukkan Judul Film yang ingin dihapus: ")
        query = "DELETE FROM film_kevina WHERE judul = %s"
        cursor.execute(query, (film_judul,))
        conn.commit()
        print(f"Film dengan judul {film_judul} telah dihapus dari film_kevina")

    @staticmethod
    def edit_film():
        conn, cursor = Crud.connect_db()
        film_judul = input("Masukkan Judul Film yang ingin diedit: ")
        tahun = input("Masukkan Tahun Film yang baru: ")
        query = "UPDATE film_kevina SET tahun = %s WHERE judul = %s"
        cursor.execute(query, (tahun,film_judul,))
        conn.commit()
        print(f"Film dengan judul {film_judul} telah diedit ke tahun {tahun}")

    @staticmethod
    def add_ticket():
        conn, cursor = Crud.connect_db()
        query_check = "SELECT * FROM studio_kevina"
        cursor.execute(query_check)
        result = cursor.fetchall()
        if result:
            print("Pilih Studio ")
            for j in result:
                print(f"id: {j[0]}, Nama: {j[1]}, Kapasitas: {j[2]} ")
            studio_id = input("Masukkan ID Studio: ")
        query_check = "SELECT * FROM film_kevina"
        cursor.execute(query_check)
        result = cursor.fetchall()
        if result:
            print("Pilih Film ")
            for j in result:
                print(f"id: {j[0]}, Judul: {j[1]}, Tahun: {j[2]} ")
            film_id = input("Masukkan ID Film: ")
        tanggal = input("Masukkan Tanggal (YYYY-MM-DD): ")
        try:
            date_obj = datetime.strptime(tanggal, "%Y-%m-%d")
            tanggal = date_obj
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
        jam_tayang = input("Masukkan Jam Tayang: ")
        jam_selesai = input("Masukkan Jam Selesai: ")
        harga = input("Masukkan Harga: ")
        query = "INSERT INTO tiket_kevina (studio_id, film_id, tanggal, jam_tayang, jam_selesai, harga) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (studio_id, film_id, tanggal, jam_tayang, jam_selesai, harga)
        cursor.execute(query, values)
        conn.commit()
        print("Data tiket_kevina telah ditambahkan.")

def main_menu():
    crud_instance = Crud()

    while True:
        print("\n===== Menu =====")
        print("1. Tambah Studio")
        print("2. Hapus Studio")
        print("3. Edit Studio")
        print("4. Tambah Film")
        print("5. Hapus Film")
        print("6. Edit Film")
        print("7. Tambah tiket")
        print("0. Keluar")

        choice = input("Masukkan pilihan (0-7): ")
        if choice == '1':
            crud_instance.studio()
        elif choice == '2':
            crud_instance.hapus_studio()
        elif choice == '3':
            crud_instance.edit_studio()
        elif choice == '4':
            crud_instance.tambah_film()
        elif choice == '5':
            crud_instance.hapus_film()
        elif choice == '6':
            crud_instance.edit_film()
        elif choice == '7':
            crud_instance.add_ticket()
        # elif choice == '6':
        #     crud_instance.edit_film()
        elif choice == '0':
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka antara 1 dan 6.")

if __name__ == "__main__":
    main_menu()
