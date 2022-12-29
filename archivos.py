from io import open

file_db=open("read_db.txt", "w")

hola='hola'

file_db.write(hola)

file_db.close()