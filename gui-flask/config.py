import mysql
from mysql import connector

db = connector.connect(host="localhost", user="root", password="", db="pingishack")
cur = db.cursor()