import pymysql


con = pymysql.connect('localhost', 'beconlab', 'beconlab', 'beconlab')
with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    cur.close()
    print("Database version: {}".format(version[0]))

