import re
from idcard_utils.area import get_area

IDCARD_REGEX = '[1-9][0-9]{14}([0-9]{2}[0-9X])?'

def is_valid_idcard(idcard):
    if isinstance(idcard, int):
        idcard = str(idcard)
    
    # 校验身份证格式
    if not re.match(IDCARD_REGEX, idcard):
        return False
    
    # 校验地区码
    area_code = idcard[:6]
    if get_area(area_code) == '未知地区':
        return False
    
    # 计算校验码
    items = [int(item) for item in idcard[:-1]]
    factors = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    copulas = sum([a * b for a, b in zip(factors, items)])
    ckcodes = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    
    return ckcodes[copulas % 11].upper() == idcard[-1].upper()

# 测试
if is_valid_idcard(210112200404170249):
    print("有效")
else:
    print("无效")
   