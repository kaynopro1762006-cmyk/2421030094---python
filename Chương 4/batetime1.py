#su dung dir() de hien thi danh sach 
import datetime
print(dir(datetime))
#tra ve ngay gio hien tai
import datetime
ngay_gio = datetime.datetime.now()
print(ngay_gio)
#tra ve ngay hien tai
import datetime
ngay = datetime.date.today()
print(ngay)
#vd
import datetime
x = datetime.datetime(2021,6,17)
print(x)
# phuong thuc strftime()
import datetime
now = datetime.datetime.now()
print(now)
s = now.strftime("%d/%m/%y,%h:%m:%s")
#dinh dang dd/mm/yy h:m:s
print("s",s)
#phuong thuc strftime()
from datetime import datetime.strptime(dt_string,"%d/%m/%y")
s = ngay_thang.strftime("%d/%m/%y")
print(s)