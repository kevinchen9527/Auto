# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:atm.py
@Time:2022/5/25 12:35

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""

user = '123456'  # 账户
user2 = '000000'
psd = "123456"  # 密码
psd2 = '000000'


# 登陆开户界面
def menu():
    print('''登录成功
    欢迎使用ATM取款机
    1.登陆
    2.注册
    ...''')


# 登陆成功后的界面


def menu2():
    print('''
        1.查询
        2.取款
        3.存款
        4.转账
        5.改密
        6.销户
        0.退出
        ...''')


class atm_test:
    def __init__(self, money) -> None:
        self.money = money  # 余额

    # 登陆功能
    def denglu(self):
        while True:
            userinp = input('请输入你的账号')
            if userinp != user:
                print('您输入的卡号不存在，请重新输入')
            else:
                psdinp = input('请输入你的密码')
                if psdinp != psd:
                    print('您的密码输入有误请重新输入')
                else:
                    print('登陆成功')
                    break
        self.denglu2()

    # 查询
    def getmoney(self):
        print('您当前的余额为：', self.money)

    # 注册
    def zuce(self):
        shoujihao = input('请输入手机号')
        yanzhengma = input('请输入验证码')
        zhanghao = input('请输入注册账号')
        mima = input('请输入注册密码')
        for i in range(3):
            mima = input('请输入您要注册的密码')
            if len(mima) > 5:
                while True:
                    mima2 = input('请再次输入您要注册的密码')
                    if mima == mima2:
                        h = mima
                        print('注册成功，请记住您的密码:%s' % (h))
                        break
                    else:
                        print('两次密码不相符请重新输入')
                break
            else:
                if i < 5:
                    print('密码长度小于五位请重新输入：')
                if i == 5:
                    print('注册失败')

    # 取款
    def qk(self):
        userinp = input('请输入你的账号')
        if userinp != user:
            print('您输入的卡号不存在，请重新输入')
        else:
            psdinp = input('请输入你的密码')
            if psdinp != psd:
                print('您的密码输入有误请重新输入')
            else:
                print('登陆成功')
                money1 = int(input('请输入取款金额：'))
                if money1 > self.money:
                    print('余额不足 ！ ！ 取款失败.....')
                    return -1
                self.money -= money1
                print('取款成功！ ！ 余额： %d' % self.money)

    # 存款
    def ck(self):
        userinp = input('请输入你的账号')
        if userinp != user:
            print('您输入的卡号不存在，请重新输入')
        else:
            psdinp = input('请输入你的密码')
            if psdinp != psd:
                print('您的密码输入有误请重新输入')
            else:
                print('登陆成功')
                money1 = int(input('请输入存款金额：'))
                self.money += money1
                print('存款成功！ ！ 余额： %d' % self.money)

    # 转账
    def zz(self):
        user2inp = input('请输入转账对方账号')
        if user2inp != user2:
            print('您输入的卡号不存在，请重新输入')
        else:
            psdinp = input('请输入你的密码')
            if psdinp != psd:
                print('您的密码输入有误请重新输入')
            else:
                print('登陆成功')
                money2 = int(input('请输入转账金额：'))
                if money2 > self.money:
                    print('余额不足 ！ ！ 转账失败.....')
                    return -1
                self.money -= money2
                print('转账成功！ ！ 余额： %d' % self.money)

    # 改密
    def gm(self):
        for i in range(3):
            psd = input('请输入您要修改的密码')
            if len(psd) > 5:
                while True:
                    gm = input('请再次输入您要修改的密码')
                    if psd == gm:
                        h = psd
                        print('请记好您的密码:%s' % (h))
                        break
                    else:
                        print('两次密码不相符请重新输入')
                break
            else:
                if i < 5:
                    print('密码长度小于五位请重新输入：')
                if i == 5:
                    print('密码修改失败')

    # 销户
    def xh(self):
        user = False
        print('你的账号已注销')

    # 登陆成功后的功能
    def denglu2(self):
        while True:
            menu2()
            print('登陆后执行的代码选项')
            inp = input('=====请选择====')
            if inp == '1':
                self.getmoney()
            elif inp == '2':
                self.qk()
            elif inp == '3':
                self.ck()
            elif inp == '4':
                self.zz()
            elif inp == '5':
                self.gm()
            elif inp == '6':
                self.xh()
            elif inp == '0':
                break


# 登陆主程序
if __name__ == '__main__':
    while True:
        menu()
        inp = int(input('请输入你要执行的操作'))
        atm = atm_test(1000)
        if inp == 1:
            atm.denglu()
        elif inp == 2:
            atm.zuce()
        elif inp == 0:
            break
        else:
            print('你输入的有误请重新输入')

