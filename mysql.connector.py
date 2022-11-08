import mysql.connector



con = mysql.connector.connect(host=input('Digite a host:'),database=input('Digite a base:'),user= input('Digite seu usuário:'),password = input('Digite sua senha:'))

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado ao servidor MySQL versão %s' % (db_info))
    cursor = con.cursor()
    cursor.execute("Select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados %s" %(linha))

if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão ao Mysql foi encerrada.')
