import random
import string

def generate_random_email():
    """生成随机邮箱: 6位字母+6位数字@outlook.com"""
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    numbers = ''.join(random.choice(string.digits) for _ in range(6))
    print(f"{letters}{numbers}@outlook.com")
    return f"创建一个outlook邮箱，邮箱{letters}{numbers}@outlook.com，密码Qwe#147258。国家/地区为中国，不要进入国家/地区选择框。出生日期为1995年8月2日，不要打开月份和日的选择框。姓氏为尼，名字为克"



if __name__ == '__main__':
    print(generate_random_email())