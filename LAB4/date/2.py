import datetime
yest=datetime.datetime.now()-datetime.timedelta(1)
tod=datetime.datetime.now()
tom=datetime.datetime.now()+datetime.timedelta(1)
print("Yesterday:",yest)
print("Today:", tod)
print("Tomorrow:", tom)