import sqlite3
import csv

username = input('Create your username: ')
userID = input('what number are you? ')

with open('users.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([username, userID])
