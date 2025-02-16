###############################################################################
## FileSender v0.9 By Leo
## Прога для доставки файлов из Windows в Linux хосты
## Через scp код намного длиннее, пока нет желания его применять тут.
## pip install paramiko
###############################################################################

import paramiko
import traceback


def send_file_sftp(hostname, username, password, files_list):
    # Создаем объект клиента SSH
    ssh_client = paramiko.SSHClient()
    
    # Добавляем политику автоматического добавления ключей хоста
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Подключаемся к серверу
        ssh_client.connect(hostname=hostname, username=username, password=password)
        
        # Открываем SFTP-сессию
        with ssh_client.open_sftp() as sftp:
            # Передаем файлы
            for file in files_list:
                source, dest = file['source'], file['dest']
                sftp.put(source, dest)
                print(f'Файл {source} успешно доставлен на {dest}')
                stdin, stdout, stderr = ssh_client.exec_command(f'chmod 0700 {dest}')
                exit_status = stdout.channel.recv_exit_status()
                if exit_status == 0:
                    print('chmod 0700 succeeded.')
                else:
                    error_message = stderr.read().decode('utf-8')
                    print(f"chmod 0700 FAILED: {error_message}")

    except FileNotFoundError:
        print('Каталог назначения не существует! Попрбуем его создать.')

        command = f'mkdir -p /opt/pythonsql'
        stdin, stdout, stderr = ssh_client.exec_command(command)
        exit_status = stdout.channel.recv_exit_status()  # Код завершения команды
        if exit_status == 0:
            print("Каталог /opt/pythonsql успешно создан. Вторая попытка передачи файлов:")
            with ssh_client.open_sftp() as sftp:
                for file in files_list:
                    source, dest = file['source'], file['dest']
                    sftp.put(source, dest)
                    print(f'Файл {source} успешно доставлен на {dest}')
        else:
            error_message = stderr.read().decode('utf-8')
            print(f"Произошла ошибка при создании каталога: {error_message}")
    except Exception as e:
        error_traceback = traceback.format_exc()
        print(f"Произошла ошибка при передаче файла: {e}\nТрассировка:\n{error_traceback}")
    finally:
        # Закрываем соединение
        ssh_client.close()


# Config
hostname = '192.168.1.71'
username = 'root'
password = 'root'
files = [
    {'source':r'C:\Leo\GitHub\PythonSQL\PythonSQL_server.py', 'dest':'/opt/pythonsql/PythonSQL_server.py'},
    {'source':r'C:\Leo\GitHub\PythonSQL\sql2py.py', 'dest':'/opt/pythonsql/sql2py.py'},
    {'source':r'C:\Leo\GitHub\PythonSQL\pysql', 'dest':'/opt/pythonsql/pysql'}
]

print('Started')
send_file_sftp(hostname, username, password, files)
print('Finished')