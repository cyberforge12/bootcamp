import time
import datetime

t = (3, 30, 2019, 9, 25)
t_adj = t[2:5] + t[:2] + (0,0,0,0)
ret = time.struct_time(t_adj)
print(time.strftime("%m/%d/%Y %H:%M", ret))
