# Отдельный файл для установки или хотябы создания контейнера баз
# ! именно здесь надо менять права на файлы и каталоги, а не в доставщике файлов!



def create_container(container_name, port):
  # 1) create directory
    # f'/var/lib/pysql/{container_name}'
  # 2) create pcatalog
  # 3) create pdba
  print(f'Congrats! New RDBMS container {container_name} was born.')