
from datetime import datetime
import webbrowser

tday = datetime.today()
day = tday.day
month = str(tday.month).zfill(2)
year = tday.year

a_link = f'https://epaper.eenadu.net/Home/Index?date={day}/{month}/{year}&eid=1'

a = datetime.now().hour
if a>12:
    a = a-12

if a < 10:
    webbrowser.open(a_link)




