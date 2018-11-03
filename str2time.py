import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    delta = int(tz_str[3:-3])
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt = dt.replace(tzinfo=timezone(timedelta(hours=delta))) #只要强制转换为utc时间，即可转为timestamp
    print(dt)
    return dt.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
