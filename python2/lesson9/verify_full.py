"""
Verifies that every animal in the "animal" table eats at least one food from the "food" table.
"""

import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

cursor.execute("SELECT * FROM animal WHERE id NOT IN (SELECT anid FROM food)")

id = cursor.fetchone()

if id:
    print("Not every animal eats at least one food item from the food table.")
else:
    print("Every animal eats at least one food item from the food table.")
