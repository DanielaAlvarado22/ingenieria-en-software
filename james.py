import re
from xml import dom
import datetime

hrsTest1 = 'Sun 10:00-20:00\nFri 05:00-10:00\nFri 16:30-23:50\nSat 10:00-24:00\nSun 01:00-04:00\nSat 02:00-06:00\nTue 03:30-18:15\nTue 19:00-20:00\nWed 04:25-15:14\nWed 15:14-22:40\nThu 00:00-23:59\nMon 05:00-13:00\nMon 15:00-21:00'
hrsTest2 = 'Mon 01:00-22:00\nTue 04:00-18:00\nWed 01:00-23:00\nThu 08:00-20:00\nFri 10:00-22:00\nSat 02:00-22:00\nSun 06:00-22:00'

def primera(e):
    return datetime.timedelta(hours=int(e[4]+e[5]),minutes=int(e[7]+e[8]))
def segunda(e):
    return datetime.timedelta(hours=int(e[10]+e[11]),minutes=int(e[13]+e[14]))
    

separados = re.split(r'\n', hrsTest2)
lunes = ['Mon 00:00-00:00']
martes = []
miercoles = []
jueves = []
viernes = []
sabado = []
domingo = ['Sun 24:00-24:00']
tiempos = []

for i in separados:
    if (i[0]+i[1]+i[2] == 'Mon'):
        lunes.append(i)
    if (i[0]+i[1]+i[2] == 'Tue'):
        martes.append(i)
    if (i[0]+i[1]+i[2] == 'Wed'):
        miercoles.append(i)
    if (i[0]+i[1]+i[2] == 'Thu'):
        jueves.append(i)
    if (i[0]+i[1]+i[2] == 'Fri'):
        viernes.append(i)
    if (i[0]+i[1]+i[2] == 'Sat'):
        sabado.append(i)
    if (i[0]+i[1]+i[2] == 'Sun'):
        domingo.append(i)


lunes.sort(key=lambda e: e[4]+e[5]+'.'+e[7]+e[8])
martes.sort(key=lambda e: e[4]+e[5]+'.'+e[7]+e[8])
miercoles.sort(key=lambda e: e[4]+e[5]+'.'+e[7]+e[8])
jueves.sort(key=lambda e: e[4]+e[5]+'.'+e[7]+e[8])
viernes.sort(key=lambda e: e[4]+e[5]+'.'+e[7]+e[8])
sabado.sort(key=lambda e: e[4]+e[5]+'.'+e[7]+e[8])
domingo.sort(key=lambda e: e[4]+e[5]+'.'+e[7]+e[8])

semana = lunes+martes+miercoles+jueves+viernes+sabado+domingo
a = 0
while(a != len(semana)-1):
    tiempos.append(primera(semana[a+1])-segunda(semana[a]))
    if (tiempos[a] < datetime.timedelta(seconds=0)):
        tiempos[a] += datetime.timedelta(days=1)
    a+=1

print(max(tiempos))