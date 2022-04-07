import mysql.connector

mydb = mysql.connector.connect(
  host="mysql-db.caprover.diplomportal.dk",
  user="s205975",
  password="AchMD1mmX4asAx9DEZIDx",
  database="s205975"
)

class Database:
  def showAnmodninger(self):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Anmodninger")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)

  def addAnmodninger(self, underviser,kursus,dato,tid):
    self.underviser = underviser
    self.kursus = kursus
    self.dato = dato
    self.tid = tid
    mycursor = mydb.cursor()
    sql = "INSERT INTO Anmodninger (underviser,kursus,dato,tid) VALUES (%s, %s,%s,%s)"
    val = (underviser,kursus,dato,tid)
    mycursor.execute(sql, val)
    mydb.commit()


db = Database()
db.addAnmodninger('Anton','Oste undervisning','04-04-2022','06:15-09:15')
db.showAnmodninger()