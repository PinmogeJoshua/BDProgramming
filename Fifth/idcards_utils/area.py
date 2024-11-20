# area.py
import pandas as pd

df = pd.read_csv("area.csv")

AREA_CODE = dict(zip(df["area_id"],df["area_name"]))

def get_area(areacode):
    return AREA_CODE.get(areacode, "未知地区")
