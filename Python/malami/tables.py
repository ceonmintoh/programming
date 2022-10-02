import sqlite3

from numpy import product
class createTables():
    conn = sqlite3.connect('malami.db')
    def userTable(conn):
        c = conn.cursor()
        c.execute("""CREATE TABLE users (
            username text,
            firstName text,
            lastName text,
            address text,
            dob text,
            phone integer,
            email text)
        """)

        conn.commit()
        conn.close()
        return
    def adminTable(conn):
        c = conn.cursor()
        c.execute("""CREATE TABLE admins (
            username text,
            firstName text,
            lastName text,
            address text,
            dob text,
            phone integer,
            email text)
        """)

        conn.commit()
        conn.close()
        return
    def productTable(conn):
        c = conn.cursor()
        c.execute("""CREATE TABLE products (
            pBrandName text,
            pPackage text,
            pPrice integer,
            pSize integer,
            dob text,
            pSupplier integer,
            pinstock text)
        """)

        conn.commit()
        conn.close()
        return
    def logTables(conn):
        c = conn.cursor()
        c.execute("""CREATE TABLE loginlogs (
            username text,
            Date text,
            Time text,
        """)

        conn.commit()
        conn.close()
    def companyTable(conn):
        c = conn.cursor()
        c.execute("""CREATE TABLE company (
            cName text,
            cFounder text,
            cAddress text,
            cRegNo text,
            cPhone text,
            cMail text,
            cTag integer
            )
        """)

        conn.commit()
        conn.close()
        return
    def customertable(conn):
        c = conn.cursor()
        c.execute("""CREATE TABLE customer (
            firstName text,
            lastName text,
            address text,
            phone integer,
            email text)
        """)

        conn.commit()
        conn.close()

    def orderstable(conn):
            c = conn.cursor()
            c.execute("""CREATE TABLE orders (
                dateOfOrder text,
                customerName text,
                lastName text,
                deliver text,
                payment text,
                amount integer,
                balance integer,)
            """)

            conn.commit()
            conn.close()
