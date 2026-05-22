#购物车
# 商品库存字典
products = {
    'apple': 5,
    'banana': 3,
    'orange': 8,
    'pear': 2
}

cart = {}

#查
def show():
    print("-------当前库存-------")
    products_show = {name:numbers for name,numbers in products.items() if numbers >0}
    for name,numbers in products_show.items():
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
            a = int(a)  # 转换为整数
            if a <= 0:
                print("数量必须是正整数！")
            else:
                if products[shangpin]>= a:
                    products[shangpin] -= a
                    cart[shangpin] = cart.get(shangpin, 0) + a #如果 cart 中有 shangpin 这个键，就返回它的值；如果没有，就返回 0。
                elif products[shangpin] == 0:
                    print('当前商品库存不足，如有会及时通知您')
                else:   
                    print(f'不好意思商品库存只有{products[shangpin]}个，已经全加到您的购物车了')
                    cart[shangpin] = cart.get(shangpin, 0) + products[shangpin]
                    products[shangpin] = 0
                show()
        except ValueError:
            print("请输入有效的数字!")
    else:
        print('您的输入有误请重新输入')

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
                    cart[s_products] -=  n_products
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
        print('您的输入有误请重新输入')

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
                    products[name] = products.get(name,0) + buyao
                    cart[name] = numbers
                    if cart[name] == 0:
                        del cart[name]
                else:
                    haiyao = numbers - cart[name]
                    if haiyao > products[name]:
                        if products[name] != 0:
                            print(f'库存里只有{products[name]}个，已全部放入购物车，您现有 {cart[name] + products[name]} 个。')
                            cart[name] += products[name]
                            products[name] = 0
                        else:
                            print('当前商品库存不足，如有会及时通知您')
                    else:
                        cart[name] += haiyao
                        products[name] -= haiyao
                show()
        except ValueError:
            print('您的输入有误，请重新输入')
    else:
        print('您的输入有误请重新输入')

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

''' 购物车系统 - 核心知识点笔记
1️⃣ 可变对象的引用传递（最核心）
python字典是可变对象，传的是"地址"，不是"副本"
car = {'apple': 0}

def zeng():
    car['apple'] = 5  # ✅ 修改全局，因为指向同一个字典

def show():
    car = {'banana': 1}  # ❌ 不修改全局，因为创建了新局部变量
🔑 修改内容（car[key]=val）→ 影响全局
🔑 重新赋值（car=new_dict）→ 只影响局部

2️⃣ show() 过滤为什么"没用"？

def show():
    car = {k:v for k,v in car.items() if v>0}  # 创建新字典
    # 函数结束，局部变量销毁，全局 car 不变！
🔑 过滤只是"展示时好看"，不是"真正清理数据"
🔑 真正清理必须在增删改函数中做

3️⃣ if not car: 判断失效的原因
情况	if not car:	实际情况
car = {}	✅ True（空）	正确
car = {'apple': 0}	❌ False（非空）	错误！有僵尸数据
解决：数量为0时用 del 彻底删除，而非 = 0

4️⃣ del vs = 0（关键区别）
操作	代码	in 判断	数据是否干净
设为0	products['apple'] = 0	✅ True（键还在）	❌ 僵尸数据
彻底删除	del products['apple']	❌ False（键没了）	✅ 干净
🔑 数量为0 → del 删除 → 数据永远干净 → if not car: 永远可靠

5️⃣ 单一职责原则（最重要的设计思想）
函数	职责	✅ 该做	❌ 不该做
show()	展示	只打印	修改/过滤数据
zeng/shan/gai()	修改	改数据 + del清理	展示/过滤
🔑 展示就展示，修改就修改，各司其职
🔑 让 show() 干净到只需一行 print

6️⃣ 最终方案：show() 不需要传参
python
# 全局变量（所有函数共享）
products = {'apple': 5, 'banana': 3}
car = {}

# show() 只读不写，直接用全局变量
def show():
    for name, num in products.items():
        print(f'{name}: {num}')
    # 不需要传参！不需要过滤！直接打印！
🔑 前提：增删改函数中已用 del 清理干净
🔑 数据干净 → 展示简单 → 代码优雅

🎯 总结
在修改数据的地方用 del 彻底清理，show() 就能做到最简单——不传参、不过滤、直接打印。这就是"各司其职"的力量。
把复杂的逻辑放在该放的地方，让每个函数都简单到一看就懂.
'''

'''传参 vs 全局变量 - 什么时候用哪个
      情况	                 是否需要传参	          原因
函数修改全局数据（增删改）	    ❌ 不需要	    直接用全局变量，通过引用修改
函数只展示全局数据（show）	    ❌ 不需要	    直接用全局变量，只读不写
函数需要操作多个不同的字典	    ✅ 需要传参	    告诉函数操作哪个字典
函数需要独立运行（不依赖全局）	✅ 需要传参	    函数自给自足，更安全
'''

'''成长轨迹（最深刻的部分）
经历4个认知升级：
阶段	             想法	                                  认知水平
阶段1	"为什么 show() 里的过滤没用？"	                      🤔 发现问题
阶段2	"我把 if not car 改成检查所有值是否为0"	              🔧 临时修补
阶段3	"我让 show() 也去清理数据，这样就不用改其他函数了"	      💡 找到捷径，但违反原则
阶段4	"不对！展示就展示，修改就修改。我应该在增删改里用 del      🎯 真正理解了单一职责和数据一致性
'''