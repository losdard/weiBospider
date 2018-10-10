import pymssql

def createConnection():
  conn = pymssql.connect(host='192.168.1.6', user='vd', password='1234', database='weiboUser')
  return conn

def closeConnection(conn):
  conn.close()

def ExecNonQuery(SqlStr,conn):
    cursor = conn.cursor()
    cursor.execute(SqlStr)
    conn.commit()

def queryWeiboID(SqlStr, conn):
  cursor = conn.cursor()
  cursor.execute(SqlStr)
  data = cursor.fetchone()
  sdata=[]
  if data:
      while data:
          sdata.append(str(data[1]))
          #iVid.append(data[8])
          data= cursor.fetchone()
  else:
      sdata="0"
  return sdata

def closeConnection(conn):
  conn.close()