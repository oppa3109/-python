# coding=utf-8

# 한줄 주석
"""
여러줄 주석
"""

Myname = "에이미"
print("je m'appelle " + Myname)
print('je m"appelle ' + Myname)
print(Myname * 2)
name = Myname * 3
print(name)
print('\n' * 3)

print('%d' %(7/2))
print('%f' %(7/2))
print('%f' %(7./2.))
print('\n' * 3)

qu = "\"%d Etre ou ne pas etre" % 1
m_qu = ''' telle
est las
question %s\"''' % '---Shakespeare'
new_string = qu + m_qu
print(new_string)
print('\n' * 3)

la_semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', "dimanche"]
print('monday', la_semaine[0])
la_semaine[0] = 'monday'
print("monday", la_semaine[0])
print(la_semaine[1:3])
days = ['mon', 'tue', 'wed']
week = [days, la_semaine]
print(week)
print(week[1][1])
print(week[0][0])
la_semaine.append('Bonjour')
print(week)
la_semaine.insert(1, "aujourdi'hui")
print(week)
la_semaine.remove('jeudi')
la_semaine.sort()
print(week)
la_semaine.reverse()
print(week)
week2 = days + la_semaine;
print(week2)
print(len(la_semaine))
print(max(la_semaine))
print(min(la_semaine))
print('\n' * 3)

pi_tuple = (3, 1, 4, 1, 5, 9)
print(pi_tuple)
new = list(pi_tuple)
print(new)
new_tuple = tuple(new)
print(new_tuple)
i = len(pi_tuple)
print(i)
i = max(pi_tuple)
print(i)
i = min(pi_tuple)
print(i)
print(pi_tuple[1])
print(pi_tuple[-2])
print(pi_tuple[1:3])
print(pi_tuple[3:])
print(pi_tuple + pi_tuple)
print(pi_tuple * 3)
print('\n' * 3)

french_week = {'Monday' : 'lundi', 'Tuesday' : 'mardi', 'Wednesday' : 'mercredi',
'Thursday' : 'jeudi', 'Friday' : 'vendredi', 'Saturday' : 'samedi', 'Sunday' : 'dimanche'}
print(french_week['Friday'])
#del(french_week['Friday'])
print(french_week.keys())
print(french_week.values())
print(french_week.get('Friday'))
print(len(french_week))

print('\n' * 3)
