# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-07 16:22:49
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-21 16:08:07

## ------------------健康模型相关的医学配置----------------------

#三餐比例
mealsPercent = [[0.25, 0.3], [0.3, 0.4], [0.3, 0.35]]

#三餐各类食物比例
mealsTypeSize = {
    "谷薯类": [120, 140],
    "蔬菜类": [140, 160],
    "水果类": [80, 100],
    "畜禽肉类": [16, 20],
    "鱼虾类": [16, 20],
    "蛋类": [20, 20],
    "奶类及制品": [80, 80],
    "大豆及其制品和坚果": [35, 35]
}

#三餐的克数限制
mealSize = [[[90, 105], [105, 120], [60, 75], [12, 15], [12, 15], [15, 15],
             [60, 60], [11, 11]],
            [[120, 140], [140, 160], [80, 100], [16, 20], [16, 20], [20, 20],
             [80, 80], [35, 35]],
            [[120, 140], [140, 160], [80, 100], [16, 20], [16, 20], [20, 20],
             [80, 80], [35, 35]]]

#各类成分每100g所含热量
calOneHundred = []

# 允许推荐菜品数
numsDishs = [[3, 8], [5, 8], [4, 8]]
#一道菜设置为几人份
numsFamily = 2
#男生的青春期摄入量
boyIntakePuberty = 2600
#女生的青春期摄入量
girlIntakePuberty = 2300
#高热量食物的阈值
highCalR = [300, 300, 300]

bodyType = {-1: "偏瘦", 0: "正常", 1: "超重", 2: "肥胖"}
userTypePer = [1, 0.95, 0.9, 1]
sportBmrArgs = [[[20.315, 485.9], [22.706, 504.3]],
                [[13.384, 692.6], [17.686, 658.2]]]
bmrDiffGender = [-161.0, 5.0]  #分别为男女的BMR偏置



















## ---------------------MongoDB数据库部分---------------

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017

# 连接数据库名称+
MONGODB_NAME = "child_recipe"

# wj搭配好三餐的食谱文档
MONGODB_COLLECTION_dailyRecipes = "dailyRecipes2"

# 食物类型文档
MONGODB_COLLECTION_foodType = "foodType"

# 用户信息
MONGODB_COLLECTION_userInform = "userInform"

# 菜谱文档
MONGODB_COLLECTION_dishes_1 = "dishes_1"
MONGODB_COLLECTION_dishes_2 = "dishes_2"
MONGODB_COLLECTION_dishes_3 = "dishes_3"

#三个分片的大小:
SIZE_DISHS = [[0, 19970], [19971, 41563], [44764, 61950]]
