# import datetime
#
# datetime_from_timestamp_old = datetime.datetime.fromtimestamp(0, datetime.timezone.utc)
# datetime_from_timestamp = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0)
# # dfto_stamp = datetime_from_timestamp_old.timestamp()
# # dft_stamp = datetime_from_timestamp.timestamp()
#
# #print(dfto_stamp)
# print(datetime_from_timestamp_old)
# print(datetime_from_timestamp)
from datetime import time
import datetime
from datetime import timedelta

set = timedelta(seconds=60)

# def second(set)str -> int


vel = 0
for i in range(60):
    if vel and i != 60:
        vel +=1
if vel == 60:
    print("go")
    # while vel == 60:
    #     print("all")

# def second():
#