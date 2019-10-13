import datetime

date=datetime.datetime.now()
h=int(date.strftime('%H'))
msg="Hello Bro How are you??"
if h<12:
    msg+="Good Morning!!!!!!"
    print(msg)
elif h<17:
    msg+="GOOd AfterNoon!!!!!!!"
    print(msg)
elif h<21:
    msg+="Good Evening!!!!!!!!!!"
    print(msg)
else:
    msg+="goood night!!!!!!!!"
    print(msg)
        