'''
1.Python 多态
“多态”（polymorphism）一词意为“多种形式”，在编程中，它指的是可以在许多对象或类上执行的具有相同名称的方法/函数/操作符。
a.函数多态：一个可用于不同对象的 Python 函数的例子是 len() 函数,
b.类多态:多态经常在类方法中使用，我们可以在其中有多个具有相同方法名的类。

2.Python 作用域
变量仅在创建区域内可用。这称为作用域。
a.局部作用域
在函数内部创建的变量属于该函数的局部作用域，并且只能在该函数内部使用。
b.全局作用域
在 Python 代码主体中创建的变量是全局变量，属于全局作用域。全局变量在任何范围（全局和局部）中可用。
c.命名变量
如果在函数内部和外部操作同名变量，Python 会将它们视为两个单独的变量，
一个在全局范围内可用（在函数外部），而一个在局部范围内可用（在函数内部）。
d.Global 关键字
如果您需要创建一个全局变量，但被卡在本地作用域内，则可以使用 global 关键字。
global 关键字使变量成为全局变量。使用 global 关键字引用该变量.
'''
#购物车
# 商品库存字典
products = {
    'apple': 5,
    'banana': 3,
    'orange': 8,
    'pear': 2
}

cart = {}

#查 - 不传参，不过滤，直接打印
def show():
    print("-------当前库存-------")
    for name, numbers in products.items():
        print(f'商品：{name}，库存：{numbers}个')

    print("\n-------您的购物车-------")
    if not cart:
        print('您的购物车是空的，快去选购商品吧')
    else:
        for name, numbers in cart.items():
            print(f'商品：{name}，数量：{numbers}个')

#增
def zeng():
    shangpin = input('请输入您要的商品：').strip().lower()
    if shangpin in products:
        a = input("请输入您要的数量：")
        try:
            a = int(a)
            if a <= 0:
                print("数量必须是正整数！")
            else:
                if products[shangpin] >= a:
                    products[shangpin] -= a
                    cart[shangpin] = cart.get(shangpin, 0) + a
                    if products[shangpin] == 0:
                        del products[shangpin]
                else:
                    print(f'不好意思商品库存只有{products[shangpin]}个，已经全加到您的购物车了')
                    cart[shangpin] = cart.get(shangpin, 0) + products[shangpin]
                    del products[shangpin]
                show()
        except ValueError:
            print("请输入有效的数字!")
    else:
        print('当前商品库存不足，如有会及时通知您')

#删
def shan():
    if not cart:
        print('您的购物车是空的，快去选购商品吧')
        return
    show()
    s_products = input('请选择您要删除的商品：').strip().lower()
    if s_products in cart:
        n_products = input('请输入您要删除的数量：')
        try:
            n_products = int(n_products)
            if n_products <= 0:
                print('请输入一个正整数！')
            else:
                if cart[s_products] >= n_products:
                    cart[s_products] -= n_products
                    products[s_products] += n_products
                    if cart[s_products] == 0:
                        del cart[s_products]
                else:
                    print(f'您购物车里只有{cart[s_products]}个，已经帮您全部删除了')
                    products[s_products] += cart[s_products]
                    del cart[s_products]
                show()
        except ValueError:
            print('请输入有效的数字!')
    else:
        print('您输入的商品不在购物车中')

#改
def gai():
    if not cart:
        print('您的购物车是空的，快去选购商品吧')
        return
    show()
    name = input('请输入您要修改的商品：')
    if name in cart:
        numbers = input('您要修改数量为：')
        try:
            numbers = int(numbers)
            if numbers < 0:
                print('请输入一个非负整数！')
            else:
                if cart[name] >= numbers:
                    buyao = cart[name] - numbers
                    products[name] = products.get(name, 0) + buyao
                    cart[name] = numbers
                    if cart[name] == 0:
                        del cart[name]
                else:
                    haiyao = numbers - cart[name]
                    if haiyao > products[name]:
                        print(f'库存里只有{products[name]}个，已全部放入购物车，您现有 {cart[name] + products[name]} 个。')
                        cart[name] += products[name]
                        del products[name]
                    else:
                        cart[name] += haiyao
                        products[name] -= haiyao
                show()
        except ValueError:
            print('您的输入有误，请重新输入')
    else:
        print('您输入的商品不在购物车中')

def man():
    while True:
        print('\n-------购物车系统--------')
        print('查看购物车商品请输入：1')
        print('增加购物车商品请输入：2')
        print('删除购物车商品请输入：3')
        print('修改购物车商品请输入：4')
        print('退出请输入：0')
        choice = input('请输入要进行的操作:')
        try:
            choice = int(choice)
            if choice == 1:
                show()
            elif choice == 2:
                zeng()
            elif choice == 3:
                shan()
            elif choice == 4:
                gai()
            elif choice == 0:
                print('感谢使用，欢迎下次再来')
                break
            else:
                print('您的输入有误请重新输入')
        except ValueError:
            print('您的输入有误请重新输入')

man()

