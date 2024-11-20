from astral import LocationInfo

# 创建一个 LocationInfo 对象，表示大连市的信息
city = LocationInfo("dalian", "china", "Asia/Shanghai", 38.888, 121.519)

# 打印城市信息，包括名称、地区、时区、纬度和经度
print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
))

import datetime
from astral.sun import sun

# 获取今天的日期
today = datetime.date.today()

# 计算大连市今天的日出、日落等时间
s = sun(city.observer, date=today, tzinfo=city.timezone)

# 打印日出、日落等时间
print((
    f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {s["sunrise"]}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'
))
