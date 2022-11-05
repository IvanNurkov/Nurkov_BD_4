import psycopg2

conn = psycopg2.connect(database="task4", user="postgres", password="post")


with conn.cursor() as cur:

    def creat_table(cur):
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client_info(
        id SERIAL PRIMARY KEY,
        client_name VARCHAR(40) NOT NULL,
        client_surname VARCHAR(60) NOT NULL,
        client_email TEXT NOT NULL,
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client_phon_namber(
        id_namber SERIAL PRIMARY KEY, 
        client_id integer NOT NULL REFERENCES cLient_info(id)
        namber INTEGER
        );
        """)

    def add_client_info(cur, name, surname, email):
        cur.execute("""
        INSERT INTO cLient_info(client_name, client_surname, client_email)
        VALUES (%s, %s, %s); 
        """, (name, surname, email))
    
    def add_client_namber(cur, client_id, namber):
        cur.execute("""
        INSERT INTO cLient_phon_namber(client_id, namber)
        VALUES (%s, %s); 
        """, (client_id, namber))

    def change_client_info(cur):
        nam = input(f'Какую информацию хотите поменять?')
        
        if nam == 'Имя':
            client_id = int(input(f"Введите id клиента: "))
            new_name = input(f'Введите новое имя: ')
            cur.execute("""
            UPDATE client_info SET client_name = %s 
            WHERE id = %s;
            """, (new_name, client_id))

        elif nam == 'Фамилия':
            client_id = int(input(f"Введите id клиента: "))
            new_surname = input(f'Введите новую фамилию: ')
            cur.execute("""
            UPDATE client_info SET client_surname = %s 
            WHERE id = %s;
            """, (new_surname, client_id))

        elif nam == 'Почта':
            client_id = int(input(f"Введите id клиента: "))
            new_email = input(f'Введите новую почту: ')
            cur.execute("""
            UPDATE client_info SET client_email = %s 
            WHERE id = %s;
            """, (new_email, client_id))

        elif nam == "Номер":
            old_namber = int(input(f"Введите номер который хотите изменить: "))
            new_namber = int(input(f"Введите новый номер теоефона: "))
            cur.execute("""
            UPDATE client_phon_namber SET namber = %s
            WHERE namber = %s;
            """, (new_namber, old_namber))

        else: print(f'Повторите запрос')

    def delete_phone_namber(cur, client_id, namber):
        cur.execute("""
        DELETE FROM client_phon_namber
        WHERE namber =%s AND id = %s;
        """, (namber, client_id))

    def delete_client(cur, client_id):
        cur.execute("""
        DELETE FROM client_phon_namber 
        WHERE id=%s;
        """, (client_id))
        cur.execute("""
        DELETE FROM client_info 
        WHERE id=%s;
        """, (client_id))
    
    def serch_client(cur):
        nam = input(f"Какую информацию вы знаете о клиенте?: ")

        if nam == 'Имя':
            s_name = input(f'Введите имя человека: ')
            cur.execute("""
            SELECT ci.id, ci.client_name, ci.client_surname, ci.email, cp.namber 
            FROM client_info ci
            JOIN client_phon_namber cp on ci.id = cp.client_id
            WHERE client_name = %s;
            """, (s_name))
            print(cur.fetchall())
        
        elif nam == 'Фамилия':
            sur_name = input(f'Введите фамилию человека: ')
            cur.execute("""
            SELECT ci.id, ci.client_name, ci.client_surname, ci.email, cp.namber 
            FROM client_info ci
            JOIN client_phon_namber cp on ci.id = cp.client_id
            WHERE client_surname = %s;
            """, (sur_name))
            print(cur.fetchall())
        
        elif nam == 'Почта':
            sur_email = input(f'Введите почту человека: ')
            cur.execute("""
            SELECT ci.id, ci.client_name, ci.client_surname, ci.email, cp.namber 
            FROM client_info ci
            JOIN client_phon_namber cp on ci.id = cp.client_id
            WHERE client_email = %s;
            """, (sur_email))
            print(cur.fetchall())

        elif nam == 'Номер':
            sur_namber = input(f'Введите номер телефона человека: ')
            cur.execute("""
            SELECT ci.id, ci.client_name, ci.client_surname, ci.email, cp.namber 
            FROM client_info ci
            JOIN client_phon_namber cp on ci.id = cp.client_id
            WHERE client_email = %s;
            """, (sur_namber))
            print(cur.fetchall())
        
        else: print(f'Повторите запрос')

def check_function(cur):
    cur.execute("""
    SELECT * FROM clients_Homework5;
    """)
    print(cur.fetchall())
    cur.execute("""
    SELECT * FROM client_phonenumbers;
    """)
    print(cur.fetchall())
    

with psycopg2.connect(database="task4", user="postgres", password="post") as conn:
    with conn.cursor() as cur:
        creat_table(cur)
        check_function(cur)
        add_client_info(cur, "Андрей", "Кузнецов", "АК@dram.com")
        add_client_info(cur, "Олег", "Вольнов", "ОВ@dram.com")
        add_client_namber(cur, 1, "8932")
        add_client_namber(cur, 2, "2526")
        change_client_info()
        delete_phone_namber()
        delete_client()
        serch_client()