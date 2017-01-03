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
question %s\"''' % "---Shakespeare"
new_string = qu + m_qu
print(new_string)
print('\n' * 3)
