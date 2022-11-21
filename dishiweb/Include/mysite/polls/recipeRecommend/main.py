# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-07 16:22:34
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-20 01:29:20

import sys
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append("..")

from service import service

a = service.userInform(name="wan",
                       height=180.0,
                       age=23,
                       gender='男',
                       weight=67,
                       puberty=0,
                       ID=2201001900,
                       prefer=["咸鲜", "酱香", "酸甜"],
                       asser={'蛋类': ['咸鸭蛋']})

# a.getUserInform()
# out = a.findById(a.ID)
# print(type(out))
# a.getUserInform()
# a.rec_recipe()
# print(a.recDishes())
# print(a.recRecipe(1,ID=199))   #这里指定了提供几天的食谱计划
# print(len(a.recDishes(ID=199)))
# print(a.recDishes(ID=199,kkk=3))


#用户信息的写入
def userInformManagement(name, height, age, gender, weight, puberty, ID,
                         prefer, asser,consumption):
    
    print(height, weight,age,gender,consumption,puberty,prefer,asser)

    a = service.userInform(name = name, ID = ID, height = height, weight = weight, age = age,gender = gender, consumption = consumption,puberty = puberty,prefer = prefer,asser = asser)
    
    # print(a)
    c = a.getUserInform()

    return True,c


def gte_dish(id: int, kkk: int):
    # print(a.recDishes(ID=id,kkk=kkk))
    return a.recDishes(ID=id, kkk=kkk)


#gte(199)
def gte_daily(id: int, nums: int):
    return a.recRecipe(id, nums)