import sqlite3

PATH_TO_DB = ""

bdd = sqlite3.connect(PATH_TO_DB)

cursor = bdd.cursor()

# Pour récupérer les ids des mails avec pdf joints
cursor.execute(
    "SELECT DISTINCT pff_identifier "
    "FROM message "
    "INNER JOIN attachment ON message.id = attachment.message_id "
    "WHERE attachment.mime_type = 'application/pdf'"
)
resp = cursor.fetchall()
print([r[0] for r in resp])


# Pour lire le sha256 du ficher
cursor.execute(
    "SELECT sha256 FROM file_report"
)
print(cursor.fetchall())

# Pour lire les dates
# cursor.execute(
#     "SELECT date FROM message LIMIT 10"
# )
print(cursor.fetchall())