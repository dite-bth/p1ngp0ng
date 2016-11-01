import mysql
from mysql import connector

db = connector.connect(host="localhost", user="root", password="", db="skatefest")
cur = db.cursor()