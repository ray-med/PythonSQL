###############################################################################
## All my SQL executors v0.02
## Пока не понятно какие данные сискаталога глобальные, какие нет,
## какие где хранить, сколько сискаталогов делать
###############################################################################

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
  def create_database(newDBname, owner):
    if owner not in pcatalog.users:
      print(f'ERROR: user {owner} doesn`t exist!')
    else:
      if owner not in pcatalog.createDBgrantees:
        print(f'ERROR: user {owner} doesn`t have CREATEDB privilege!')
      else:
        # create new record in pcatalog
        # create directory code
        print(f'Database {newDBname} created.')

  def create_schema(dbname=dbname, owner='pdba'):
    # create new record in pcatalog
    # create directory inside database code
    pass

  def create_table(dbname='db0', schemaName='pdba', tableName='', owner='pdba'):
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