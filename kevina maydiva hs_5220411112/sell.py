import mysql.connector
from datetime import datetime

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

def katalog_tickets(cursor):
    current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = f"""
        SELECT tiket_kevina.Id, film_kevina.judul, tiket_kevina.tanggal, tiket_kevina.jam_tayang, tiket_kevina.harga
        FROM tiket_kevina
        INNER JOIN film_kevina ON tiket_kevina.film_id = film_kevina.Id
        WHERE tiket_kevina.tanggal > '{current_date_time}'
    """
    cursor.execute(query)
    tickets = cursor.fetchall()

    print("Tiket Yang Tersedia:")
    for ticket in tickets:
        print(f"Ticket ID: {ticket[0]}, Film: {ticket[1]}, Date: {ticket[2]}, Time: {ticket[3]}, Price: {ticket[4]}")

def sell_ticket(cursor, ticket_id, quantity):
    query = f"SELECT * FROM tiket_kevina WHERE Id = {ticket_id}"
    cursor.execute(query)
    ticket = cursor.fetchone()

    if not ticket:
        print(f"Ticket with ID {ticket_id} not found.")
        return

    studio_id = ticket[1]
    query = f"SELECT kapasitas FROM studio_kevina WHERE Id = {studio_id}"
    cursor.execute(query)
    studio_capacity = cursor.fetchone()[0]


    query = f"SELECT COUNT(*) FROM tr_penjualan_kevina WHERE tiket_id = {ticket_id}"
    cursor.execute(query)
    sold_tickets = cursor.fetchone()[0]

    if sold_tickets + quantity > int(studio_capacity):
        print(f"Not enough seats available for {quantity} tickets.")
        return

    total_price = int(ticket[6]) * quantity

    current_date = datetime.now().strftime('%Y-%m-%d')

    payment = float(input(f"Harga: {total_price}. Masukkan Saldo: "))

    if payment < total_price:
        print("Pembayaran Gagal. Transaksi Dibatalkan.")
        return


    change = payment - total_price


    query = """
        INSERT INTO tr_penjualan_kevina (tiket_id, jumlah, bayar, kembalian, tanggal)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (ticket_id, quantity, total_price, change, current_date)
    cursor.execute(query, values)

    print(f"Pebayaran Berhasil Kembalian anda adalah: {change}")

def main():
    conn, cursor = connect_db()

    katalog_tickets(cursor)

    ticket_id = input("Masaukkan ID tiket yang ingin di beli: ")
    quantity = int(input("Masukkan total dari tiket yang ingin dibeli: "))

    sell_ticket(cursor, ticket_id, quantity)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
