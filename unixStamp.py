import time
from datetime import datetime
import sys

def getUNIXStamp(tyme=None,tipe="day"):
    if tyme:
        now=tyme
    else:
        now=datetime.now()
    if tipe=="day":
        return int(time.mktime(now.date().timetuple()))
    else:
        return int(time.mktime(now.timetuple()))

def main():
    arglen=len(sys.argv)
    if arglen==1:
        ts=getUNIXStamp()
    elif arglen==2:
        day= datetime.strptime(sys.argv[1],"%Y-%m-%d")
        ts=getUNIXStamp(day)
    elif arglen==3:
        day=sys.argv[1]+' '+sys.argv[2]
        day=datetime.strptime(day,'%Y-%m-%d %H:%M')
        ts=getUNIXStamp(day,'hour')
    print(ts)
    return ts

if __name__ == "__main__":
    main()