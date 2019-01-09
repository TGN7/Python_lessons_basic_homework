# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os, platform
import sys
print('sys.argv = ', sys.argv)


def print_help():
	print("help - получение справки")
	print("mkdir <dir_name> - создание директории")
	print("ping - тестовый ключ")
	print("cp <file_name> - создает копию указанного файла")
	print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
	print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
	print("ls - отображение полного пути текущей директории")

def cp():
    if not dir_name:
        print("Необходимо указать имя файла для копирования")
        return
	if platform.system() == 'Windows':
		filename=dir_name.split('\\')[-1]
        print(filename)
        os.system('copy {} copy_{}'.format(dir_name,filename))
	else: 
		filename=dir_name.split('/')[-1]
        os.system('cp {} copy_{}'.format(dir_name,filename))  
	
def rm():
	if not dir_name:
        print("Необходимо указать имя удаляемого файла")
        return
	if os.path.exists(dir_name):
		print('Файлу {} существует и будет удален'.format(dir_name))
		yesnot=input('y - Подтвердите удаление')
		if yesnot=='y':
			try:   
				os.remove(dir_name)
			except Exception:
				print('Отмена удаления')
	else:
		print('Файл не существует')
	

def cd():
if not dir_name:
		print("необходимо указать путь")
		return
	if platform.system() == 'Windows':
		if re.search('^[A-Z]:',dir_name) is None:
			print('Относительный путь')
		else:
			print('Абсолютный путь')
		try:
			os.chdir(dir_name)
			print(os.getcwd())
		except Exception as error:
			print(error)
	else:
		if re.search('^/',dir_name) is None:
			print('Относительный путь')
		else:
			print('Абсолютный путь')
		try:
			os.chdir(dir_name)
			print(os.getcwd())
		except Exception as error:
			print(error)

def ls():
	print(os.getcwd())
	

def make_dir():
	if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
	dir_path = os.path.join(os.getcwd(), dir_name)
	try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_name))
	except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

do = {
	"help": print_help,
	"mkdir": make_dir,
	"ping": ping,
	"cp": cp,
	"rm": rm, 
	"cd": cd,
	"ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
print("Укажите ключ help для получения справки")
