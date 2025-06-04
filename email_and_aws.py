import random
import string

def generate_random_email_and_register():
    """生成随机邮箱: 6位字母+6位数字@outlook.com"""
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    numbers = ''.join(random.choice(string.digits) for _ in range(6))
    print(f"创建一个outlook邮箱，邮箱{letters}{numbers}@outlook.com，密码Qwe#147258。国家/地区为中国，不要进入国家/地区选择框。出生日期为1995年8月2日，不要打开月份和日的选择框。姓氏为尼，名字为克")
    print(f"注册aws账号，邮箱地址{letters}{numbers}@outlook.com， 账号名{letters}，再登陆邮箱，邮箱密码为Qwe#147258，去查询最新的验证码，并输入验证码框。然后输入root用户的密码，同样为Qwe#147258。之后进入联系信息页面，选择Personal，全名为John，电话的Country Code为+86，手机号为18910839859，国家或地区选United States，地址填写123 Main St，城市选New York，州/省/地区选择NY，邮政编码选10001。然后进入支付信息页面，点击Sign Out")

if __name__ == '__main__':
    generate_random_email_and_register()