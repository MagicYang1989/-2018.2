
print("="*50)
print("欢迎使用姓名管理系统v1.0")

print("1.添加新的名字")
print("2.删除已有名字")
print("3.修改已有名字")
print("4.查找已有名字")
print("5.退出系统")
print("="*50)

names = []



while True:

	nums = int(input("请输入您要使用的功能序号："))

	if nums == 1:
		new_name = input("请输入您要添加的名字：")
		names.append(new_name)
		print(names)

	elif nums == 2:
		del_name = input("请输入您要的删除的名字：")
		names.remove(del_name)
		print(names)

	elif nums == 3:
		oldname = input("请输入您要修改的名字：")
		if oldname in names:
			rename = input("请输入新的名字：")
			names.remove(oldname)
			names.append(rename)
			print(names)
		else:
			print("查无此人！请从下方已有名字中选择您要修的名字")
			print(names)

	elif nums == 4:
		while True:
			find_name = input("请输入您要查找的名字：")
			if find_name in names:
				print("查有此人")
			else:
				tips = input("查无此人！\n是否要显示全部名字？yes/no:")
				if tips == "yes":
					print(names)
				elif tips == "no":
					break

	elif nums == 5:
		break
	else:
		print("您输入的序号有误，请重新输入")




