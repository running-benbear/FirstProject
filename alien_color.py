# 6-1 存储熟人信息
friend_1 = {
    "first_name": "惠兰",
    "last_name": "朴",
    "age": 52,
    "city": "上海"
}
friend_2 = {
    "first_name": "栏",
    "last_name": "张",
    "age": 22,
    "city": "上海"
}
friend_3 = {
    "first_name": "华",
    "last_name": "李",
    "age": 32,
    "city": "北京"
}
people = [friend_1, friend_2, friend_3]
# 遍历列表
for person in people:
    print("姓："+person['last_name'])
    print("名："+person["first_name"])
    print("年龄："+str(person["age"]))
    print("居住城市："+person["city"]+"\n")

# 6-9 喜欢的地方
favorite_places = {
    "Liminqing": ["厦门", "东京", "首尔"],
    "Alice": ["纽约"],
    "Sarah": ["巴黎", "曼谷"]
}
for name, places in favorite_places.items():
    if len(places) == 1:
        print("\n"+name+"'s favorite place is:")
    else:
        print("\n"+name+"'s favorite places are:")
    for place in places:
        print(place)

# 6-11 创建cities字典
cities = {
    "上海": {
        "country": "中国",
        "population": 2154,
        "fact": "中国一线城市"
    },
    "纽约": {
        "country": "美国",
        "population": 833,
        "fact": "美国最大城市"
    },
    "东京": {
        "country": "日本",
        "population": 1395,
        "fact": "日本首都"
    }
}
for name, info_dic in cities.items():
    print("\n" + name + "的信息显示如下：")
    for info in info_dic.items():
        if info[0] == "country":
            print("国家：" + info[1])
        elif info[0] == "population":
            print("人口：" + str(info[1]))
        else:
            print("事实：" + info[1])


# 6-10 喜欢的数字
favorite_number = {
    "alice": [1, 2, 3, 4],
    "sarah": [3, 17],
    "john": [66]
}
for person, number_list in favorite_number.items():
    print("\n"+person+"最喜欢的数字是：")
    for number in number_list:
        print(number)
