#Vars 
hour=14
minutes=13
seconds=15

#Seconds since midnight():
a=(minutes*60+hour*3600+seconds)
a1="Seconds since midnight={}"
#Seconds r day():
b=(86400-a)
b1="Seconds reamaining in the day={}"
#Num fullmins midnight():
c=((hour*60)+minutes)
c1="Full minutes elapsed={}"
#Printer go brrr
print(a1.format(a))
print(b1.format(b))
print(c1.format(c))
