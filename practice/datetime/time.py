import time,datetime

epochsec = time.time()
print(epochsec)
t = time.ctime(epochsec)
print(t)
dt=datetime.datetime.today()
print(dt)
print(dt.day)
print(dt.month)
print(dt.year)
print("current Time :{}/{}/{}".format(dt.hour,dt.minute,dt.second))