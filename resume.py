#import streamlit as st
import nltk
nltk.download('stopwords')
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

import io, random
import pymysql


load_dotenv()
SQL_HOST = os.environ['SQL_HOST']
SQL_USER = os.environ['SQL_USER']
SQL_PASSWORD = os.environ['SQL_PASSWORD']
SQL_DATABASE = os.environ['SQL_DATABASE']

""" connection = mysql.connector.connect(
    user=SQL_USER,
    password=SQL_PASSWORD,
    host=SQL_HOST,
    database=SQL_DATABASE,
    port=3306
) """
def insert_data(title, price, discount):
    DB_table_name = 'user_data'
    insert_sql = "insert into " + DB_table_name + """
    values (0,%s,%s,%s)"""
    rec_values = (title, price, discount)
    connection = pymysql.connect(host=SQL_HOST, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE, port=3306)
    cursor = connection.cursor()
    cursor.execute(insert_sql, rec_values)
    connection.commit()
    cursor.close()
    connection.close()

def run(pdf_file):
    # Connect to the database
    connection = pymysql.connect(host=SQL_HOST, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE, port=3306)
    cursor = connection.cursor()
    connection.select_db(SQL_DATABASE)



    # Create table
    DB_table_name = 'user_data'
    table_sql = "CREATE TABLE IF NOT EXISTS " + DB_table_name + """
                    (ID INT NOT NULL AUTO_INCREMENT,
                     title Varchar(100),
                     price VARCHAR(50),
                     discount VARCHAR(50),
                     PRIMARY KEY (ID));
                    """
    cursor.execute(table_sql)
    # st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Upload your resume, and get smart recommendation based on it."</h4>''',
    #             unsafe_allow_html=True)
    #pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
    if pdf_file is not None:
        l=[]
        o={}
        target_url=pdf_file

        resp = requests.get(target_url)
        soup=BeautifulSoup(resp.text,'html.parser')
        o["title"]=soup.find("h1",{"class":"x-item-title__mainTitle"}).text
        #o["rating"]=soup.find("span",{"class":"ebay-review-start-rating"}).text.strip()
        o["actual_price"]=soup.find("span",{"class":"ux-textspans"}).text
        box=soup.find("div",{"class":"x-additional-info"})
        o["list_price"]=box.find("span",{"class":"ux-textspans--STRIKETHROUGH"}).text
        o["discount"]=box.find("span",{"class":"ux-textspans--EMPHASIS"}).text
        o["shipping_price"]=soup.find("div",{"id":"SRPSection"}).find("span",{"class":"ux-textspans--BOLD"}).text
        l.append(o)
        print(l)
        
        product = l[0]  # Assuming the product details are at index 0

        # Access title and price
        title = product['title']
        price = product['list_price']
        discount = product['discount']
        insert_data(title, price, discount)
        connection.commit()
        # os.remove(save_image_path)
        cursor.close()
        connection.close()
        return 'Success'
    else:
        return 'Failed'
