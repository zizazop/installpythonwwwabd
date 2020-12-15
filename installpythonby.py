from os.path import expanduser,os
import time,subprocess,wget,os
print('SCRIPT BY ANDREI ZHUK')
time.sleep(1)
print('https://vk.com/andrey47785')
#НЕ ВОЛНУЙТЕСЬ ПО ПОВОДУ ТОГО,ЧТО МОДУЛИ НЕ БУДУТ ИМПОРТИРОВАТСЯ ПОТОМУЧТО ЗА ВАС ЭТО СДЕЛАЕТ И ЗАПАКУЕТ В ПРОГРАММУ МОДУЛИ ПАЙ ИНСТАЛЛ
home= expanduser("~")
time.sleep(1.56)
print('Закачиваю файлы...')
time.sleep(1)
print('.\\WHAIT//.')
s='https://www.python.org/ftp/python/3.8.7/python-3.8.7rc1-amd64.exe'
filename= wget.download(s)
os.rename(filename,u''+os.getcwd()+'/'+filename)
subprocess.call([home+'/Desktop/python-3.9.1-amd64.exe'])
print('OK')
os.remove(home+'/Desktop/python-3.9.1-amd64.exe')
print('DELETED TO INSTALATOR')
time.sleep(3)
print('УДАЛЯЮ СЕБЯ...')
os.remove(home+'/Desktop/installpythonby.exe')

