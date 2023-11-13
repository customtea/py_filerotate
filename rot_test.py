from filerotate import FileRotate
import datetime
import time
from random import randint

rot = FileRotate("./test", crontext="* * * * *", csv_mode=True)

while True:
    dt_now = datetime.datetime.now()
    # rot.write(dt_now.isoformat() + "\n")
    rot.writerow([dt_now, 1, 2 ,3, 4, randint(0, 100)])
    time.sleep(1)
