###############################################################################
## All my SQL executors v0.03
## Пока не понятно какие данные сискаталога глобальные, какие нет,
## какие где хранить, сколько сискаталогов делать
###############################################################################

def double(arg):
  return (int(arg)*2, False, False)

def triple(arg):
  return (int(arg)*3, False, False)

def disconnect():
  # print(f'Client {client_address} exited.')
  return ('Disconnecting from server...', True, False)

def kill_server(server_version):
  print(f'Shutdown PythonSQL server {server_version} started.')
  return ('Starting server shutdown.', True, True)


class PRIVILEGES:
  def __init__(self, ):
    pass

class USER:
  def __init__(self, username, password, privileges):
    self.username = username
    self.password = password
    self.privileges = PRIVILEGES()

class currentDB:
  def __init__(self, server_ip, server_port, dbname, owner):
    self.server_ip = server_ip
    self.server_port = server_port
    self.dbname = dbname
    self.owner = owner


  # --------------- DDL CREATE ------------------------------------------------------
#   def create_database(newDBname, owner):
#     if owner not in pcatalog.users:
#       print(f'ERROR: user {owner} doesn`t exist!')
#     else:
#       if owner not in pcatalog.createDBgrantees:
#         print(f'ERROR: user {owner} doesn`t have CREATEDB privilege!')
#       else:
#         # create new record in pcatalog
#         # create directory code
#         print(f'Database {newDBname} created.')

#   def create_schema(dbname=dbname, owner='pdba'):
#     # is db exists check
#     # create new record in pcatalog
#     # create directory inside database code
#     pass

  def create_table(dbname='db0', schemaName='pdba', tableName='', owner='pdba'):
    # is schema exists check
    # create new record in pcatalog
    # create table logic
    pass

  def create_user():
    # create new record in pcatalog
    # create user logic
    pass

  # --------------- DML -------------------------------------------------------
  def insert(tablename, data):
    nrows = 0
    # insert logic
    print(f'{nrows} inserted into {tablename}.')

  def update(tablename, condition, newval):
    nrows = 0
    # update logic
    print(f'{nrows} updated in {tablename}.')

  def delete(tablename, condition):
    nrows = 0
    # delete logic
    print(f'{nrows} deleted from {tablename}.')

  # --------------- SELECT ----------------------------------------------------
  def select():
    # SELECT logic
    # return dataset # then it goes to prettytable in main code
    pass

  # --------------- DCL -------------------------------------------------------
  