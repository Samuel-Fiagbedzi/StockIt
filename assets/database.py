import sqlite3 as sq


def create_database():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Items (
        Item_Name TEXT,
        Quantity TEXT,
        Category TEXT,
        Price TEXT,
        Date TEXT)
        """)
    conn.commit()
    conn.close()

    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Service_stock (
            Item_Name TEXT,
            Status TEXT,
            Category TEXT,
            Price TEXT,
            Date TEXT)
            """)
    conn.commit()
    conn.close()

    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Service_stock_saved (
            Item_Name TEXT,
            Status TEXT,
            Category TEXT,
            Price TEXT,
            Date TEXT)
            """)
    conn.commit()
    conn.close()

    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Items_saved (
            Item_Name TEXT,
            Quantity TEXT,
            Category TEXT,
            Price TEXT,
            Date TEXT)
            """)
    conn.commit()
    conn.close()

    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS Time_table (
                Time TEXT,
                Tab TEXT)
                """)
    conn.commit()
    conn.close()

    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS Items_uploaded (
                Time TEXT)
                """)
    conn.commit()
    conn.close()

    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Items_uploaded_service (
                    Time TEXT)
                    """)
    conn.commit()
    conn.close()

    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Comments (
                        Comment TEXT)
                        """)
    conn.commit()
    conn.close()

    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
                            CREATE TABLE IF NOT EXISTS User (
                            Name TEXT,
                            Password TEXT,
                            Email TEXT,
                            ApplicationPassword TEXT)
                            """)
    conn.commit()
    conn.close()

    conn = sq.connect("../items.db")
    cursor = conn.cursor()

    cursor.execute("""
                                CREATE TABLE IF NOT EXISTS Category (
                                Data TEXT)
                                """)
    conn.commit()
    conn.close()


def fetch_data():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data_user():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data_comment():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Comments")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data_category():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Category")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data_time():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Time_table")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data_service():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Service_stock")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data_service_saved():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Service_stock_saved")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data_saved():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items_saved")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data_items_uploaded():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items_uploaded")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data_items_uploaded_service():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items_uploaded_service")
    data = cursor.fetchall()
    conn.close()
    return data


def add_item(name, quantity, category, price, date):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Items (Item_name, Quantity, Category, Price, Date) VALUES (?, ?, ?, ?, ?)",
                   (name, quantity, category, price, date))
    conn.commit()
    conn.close()


def add_item_user(name, password, email, application_password):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO User (Name, Password, Email, ApplicationPassword) VALUES (?, ?, ?, ?)",
                   (name, password, email, application_password))
    conn.commit()
    conn.close()


def add_item_uploaded(time):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Items_uploaded (Time) VALUES (?)", (str(time),))
    conn.commit()
    conn.close()


def add_item_category(cat):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Category (Data) VALUES (?)", (cat,))
    conn.commit()
    conn.close()


def add_item_comment(comment):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Comments (Comment) VALUES (?)", (str(comment),))
    conn.commit()
    conn.close()


def add_item_uploaded_service(time):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Items_uploaded_service (Time) VALUES (?)", (str(time),))
    conn.commit()
    conn.close()


def add_item_time(name, table):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Time_table (Time, Tab) VALUES (?,?)", (name, table))
    conn.commit()
    conn.close()


def add_item_service(name, status, category, price, date):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Service_stock (Item_name, Status, Category, Price, Date) VALUES (?, ?, ?, ?, ?)",
                   (name, status, category, price, date))
    conn.commit()
    conn.close()


def remove_item(name):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Items WHERE Item_name = ?", (name,))
    conn.commit()
    conn.close()


def remove_item_upload(rowid):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Items_uploaded WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()


def remove_item_upload_service(rowid):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Items_uploaded_service WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()


def remove_item_service(name):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Service_stock WHERE Item_name = ?", (name,))
    conn.commit()
    conn.close()


def update_item(name, quantity, category, price, date):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE Items SET Item_name = ?, Quantity = ?, Category = ?, Price = ?, Date = ? 
    WHERE Item_name = ?""",
                   (name, quantity, category, price, date, name))
    conn.commit()
    conn.close()


def update_item_user(name, password, email, application_password):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE User SET Name = ?, Password = ?, Email = ?, ApplicationPassword = ? 
    WHERE Name = ?""",
                   (name, password, email, application_password, name))
    conn.commit()
    conn.close()


def update_item_service(name, status, category, price, date):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE Service_stock SET Item_name = ?, Status = ?, Category = ?, Price = ?, Date = ? 
    WHERE Item_name = ?""",
                   (name, status, category, price, date, name))
    conn.commit()
    conn.close()


def item_exist(name):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Items WHERE Item_Name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0


def item_exist_uploaded(time):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Items_uploaded WHERE Time = ?", (time,))
    result = cursor.fetchone()
    conn.close()
    return result


def item_exist_uploaded_service(time):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Items_uploaded_service WHERE Time = ?", (time,))
    result = cursor.fetchone()
    conn.close()
    return result


def item_exist_time(name):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Time_table WHERE Time = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result


def item_exist_service(name):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Service_stock WHERE Item_Name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0


def check():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items")
    data = cursor.fetchall()
    conn.close()
    return len(data)


def check_service():
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Service_stock")
    result = cursor.fetchall()
    conn.close()
    return len(result)


def save():
    exist = True
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items")
    data = cursor.fetchall()
    conn.close()
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items_saved")
    archived_data = cursor.fetchall()
    for x in data:
        if x in archived_data:
            exist = True
            break
        else:
            exist = False
            cursor.execute("""INSERT INTO Items_saved (Item_name, Quantity, Category, Price, Date)
                       VALUES (?, ?, ?, ?, ?)""", (x[0], x[1], x[2], x[3], x[4]))
            continue
    conn.commit()
    conn.close()
    return exist


def save_service():
    exist = True
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Service_stock")
    data = cursor.fetchall()
    conn.close()
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Service_stock_saved")
    archived_data = cursor.fetchall()
    for x in data:
        if x in archived_data:
            exist = True
            break
        else:
            exist = False
            cursor.execute("""INSERT INTO Service_stock_saved (Item_name, Status, Category, Price, Date)
                       VALUES (?, ?, ?, ?, ?)""", (x[0], x[1], x[2], x[3], x[4]))
            continue
    conn.commit()
    conn.close()
    return exist


def search(content):
    content1 = content.lower()
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM Items WHERE Item_name LIKE '{content1}%' """)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result


def search_service(content):
    content1 = content.lower()
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM Service_stock WHERE Item_name LIKE '{content1}%' """)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result


def search_by_date(content):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Items_saved WHERE Date = ? """, (content,))
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result


def search_by_date_service(content):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Service_stock_saved WHERE Date = ? """, (content,))
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result


def update_date(date):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    data_ = fetch_data()
    num = 0
    for x in data_:
        item_name = str(x[0])
        cursor.execute("""UPDATE Items SET Date = ? WHERE Item_name = ?""", (date, item_name,))
        num = num + 1
    conn.commit()
    conn.close()


def update_date_service(date):
    conn = sq.connect("../items.db")
    cursor = conn.cursor()
    data_ = fetch_data_service()
    num = 0
    for x in data_:
        item_name = str(x[0])
        cursor.execute("""UPDATE Service_stock SET Date = ? WHERE Item_name = ?""", (date, item_name,))
        num = num + 1
    conn.commit()
    conn.close()


create_database()
