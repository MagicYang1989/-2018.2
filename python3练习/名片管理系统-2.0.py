#1.打印功能提示
print("="*50)
print("     名片管理系统 v2.0")
print("1. 添加一张新的名片")
print("2. 删除一张名片")
print("3. 修改一张名片")
print("4. 查询一张名片")
print("5. 显示所有的名片")
print("6. 退出系统")
print("="*50)

#定义一个空列表用来存储名片
card_infors = []

while True:
#2.获取用户信息
    num = int(input("请输入操作序号："))

#3.根据用户输入的信息来实现对应功能
    #实现功能1.添加
    if num == 1:
        new_name = input("请输入新的姓名：")
        new_qq = input("请输入QQ：")
        new_weixin = input("请输入微信：")
        new_addr = input("请输入地址：")

        #定义一个新的字典用来存储名片
        new_infor = {}
        new_infor["name"] = new_name
        new_infor["qq"] = new_qq
        new_infor["weixin"] = new_weixin
        new_infor["addr"] = new_addr

        #将名片字典添加到空里表中
        card_infors.append(new_infor)
        print("名片已添加")

        #print(card_infors)


    #实现功能2.删除
    elif num == 2:
        del_name = input("请输入要删除名片的姓名：")
        
        j = 0 #默认没有找到要删除名片的信息

        for temp in card_infors:
            if del_name == temp["name"]:
                j = 1 #表示找到了要删除的名片信息
                card_infors.remove(temp)
                print("已删除名片")
                break
        if j == 0:
            print("没有找到要删除的名片信息")


    #实现功能3.修改
    elif num == 3:
        rename = input("请输入要修改名片的姓名：")

        k = 0
        for temp in card_infors:
            if rename == temp["name"]:
                k = 1
                print("找到名片信息，开始修改：")
                new_name = input("请输入新的姓名：")
                new_qq = input("请输入QQ：")
                new_weixin = input("请输入微信：")
                new_addr = input("请输入地址：")
                temp["name"] = new_name
                temp["qq"] = new_qq
                temp["weixin"] = new_weixin
                temp["addr"] = new_addr
                print("修改成功，请使用功能5.来查看更新")
                break
        if k == 0:
            print("没有找到要修改的名片信息")

    #实现功能4.查询
    elif num == 4:
        find_name = input("请输入要查询的姓名：")

        i = 0 #定义一个变量为零，默认表示没有找到
        
        for temp in card_infors:
            if find_name == temp["name"]:
                i = 1 #表示找到了
                print("姓名\tQQ\t微信\t地址")
                print("%s\t%s\t%s\t%s\t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
                break

        if i == 0:#表示没有找到
            print("查无此人！")


    #实现功能5.查看
    elif num == 5:
        print("姓名\tQQ\t微信\t地址")
        for temp in card_infors:
            print("%s\t%s\t%s\t%s\t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))


    #实现功能6.退出
    elif num == 6:
        break
    else:
        print("您输入的序号有误，请重新输入：")


    print("")
