# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-07 16:24:56
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-20 15:18:12
import sys

sys.path.append('..')
from conf import config

import pymongo

# myclient = pymongo.MongoClient(host=config.MONGODB_HOST,port=config.MONGODB_PORT)
# db = myclient.child_recipe
# collectionsName = db.list_collection_names()
# print(collectionsName)


class mongoDB():

    def __init__(self, host, port, db, usrname=None, password=None) -> None:
        self.host = host
        self.port = port
        self.username = usrname
        self.password = password
        self.db = db
        self.client = pymongo.MongoClient(host=self.host, port=self.port)

    def wriUserInform(self, inform,ID):
        '''用户信息写入'''
        # client = self.connectdb
        dbb = self.client.child_recipe  ##注意这里直接使用了食材库
        usrCollection = dbb[config.MONGODB_COLLECTION_userInform]
        #这里连接成功数据库，
        # findOut = usrCollection.find({'ID': ID})[0]

        try:
            usrCollection.delete_one({'ID':ID})
            
        except :
            pass
        
    

        res = usrCollection.insert_one(inform)
        # post_id = usrCollection.insert_one(inform).inserted_id
        # print(post_id)
        print("数据写入成功", res)

        return res


#"应该让用户信息的增删改查放在同一个接口下面，只是加一些判断，就好"

    def selectUsrInform(self, ID):
        '''用户信息查询'''
        dbb = self.client.child_recipe  ##注意这里直接使用了食材库
        usrCollection = dbb[config.MONGODB_COLLECTION_userInform]
        try:
            findOut = usrCollection.find({'ID': ID})[0]
            print("用户信息数据查询成功")
            return findOut
        except IndexError:
            return '用户ID不正确'

    def findd(self, id: int):
        '''
            单条信息查询
            '''
        if id <= config.SIZE_DISHS[0][1] and id >= config.SIZE_DISHS[0][0]:
            dbb = self.client.child_recipe
            dishesInfo_1 = dbb[config.MONGODB_COLLECTION_dishes_1]
            # findOutDishes_1 = dishesInfo_1.find({"containsInfo.含量（g）":{"$gte":200,"$lte":300} ,"containsInfo.type":"谷薯类","prefer":{"$in":prefer},"containsinfolist":{"$nin":asser}})
            findOutDishes_1 = dishesInfo_1.find({"id": id})
            # print(findOutDishes_1,end="\n\n\n\n-------------------------\n\n\n")
            return findOutDishes_1[0]
        elif id <= config.SIZE_DISHS[1][1] and id >= config.SIZE_DISHS[1][0]:
            dbb = self.client.child_recipe
            dishesInfo_2 = dbb[config.MONGODB_COLLECTION_dishes_2]
            # findOutDishes_1 = dishesInfo_1.find({"containsInfo.含量（g）":{"$gte":200,"$lte":300} ,"containsInfo.type":"谷薯类","prefer":{"$in":prefer},"containsinfolist":{"$nin":asser}})
            findOutDishes_2 = dishesInfo_2.find({"id": id})
            return findOutDishes_2[0]
        else:
            dbb = self.client.child_recipe
            dishesInfo_3 = dbb[config.MONGODB_COLLECTION_dishes_3]
            # findOutDishes_1 = dishesInfo_1.find({"containsInfo.含量（g）":{"$gte":200,"$lte":300} ,"containsInfo.type":"谷薯类","prefer":{"$in":prefer},"containsinfolist":{"$nin":asser}})
            findOutDishes_3 = dishesInfo_3.find({"id": id})
            return findOutDishes_3[0]

    def selectBreakfast(self, calBoundry):
        '''早餐匹配查询'''
        dbb = self.client.child_recipe
        # print(dbb)
        dailyrecipe = dbb[config.MONGODB_COLLECTION_dailyRecipes]
        findOut = dailyrecipe.find({
            '餐时': '早餐',
            '热量总计': {
                '$gte': calBoundry[0],
                '$lte': calBoundry[1]
            }
        })
        if findOut[0]:
                
            print('早餐匹配成功！')
            return findOut

    def selectLunch(self, calBoundry):
        '''午餐匹配查询'''
        dbb = self.client.child_recipe
        dailyRecipe = dbb[config.MONGODB_COLLECTION_dailyRecipes]
        findOut = dailyRecipe.find({
            '餐时': '午餐',
            '热量总计': {
                '$gte': calBoundry[0],
                '$lte': calBoundry[1]
            }
        })
        if findOut[0]:
                
            print('午餐匹配成功！')
            return findOut

    def selectDinner(self, calBoundry):
        '''晚餐匹配查询'''
        dbb = self.client.child_recipe
        dailyrecipe = dbb[config.MONGODB_COLLECTION_dailyRecipes]
        findOut = dailyrecipe.find({
            '餐时': '晚餐',
            '热量总计': {
                '$gte': calBoundry[0],
                '$lte': calBoundry[1]
            }
        })
        print(findOut[0])
        if findOut[0]:
            
            print('晚餐匹配成功！')
            return findOut

    def selectDishes(self, prefer, asser):
        '''进行数据的粗提取'''
        # 首先提取数据
        # 这里是指先拿出全部的数据
        # 只拿出id,prefer,containsInfo,containsinfolist
        findOutDishes = []
        dbb = self.client.child_recipe
        dishesInfo_1 = dbb[config.MONGODB_COLLECTION_dishes_1]
        # findOutDishes_1 = dishesInfo_1.find({"containsInfo.含量（g）":{"$gte":200,"$lte":300} ,"containsInfo.type":"谷薯类","prefer":{"$in":prefer},"containsinfolist":{"$nin":asser}})
        findOutDishes_1 = dishesInfo_1.find({
            "prefer": {
                "$in": prefer
            },
            "containsinfolist": {
                "$nin": asser
            }
        })
        for i in findOutDishes_1:
            findOutDishes.append(i)

        dishesInfo_2 = dbb[config.MONGODB_COLLECTION_dishes_2]
        findOutDishes_2 = dishesInfo_2.find({
            "prefer": {
                "$in": prefer
            },
            "containsinfolist": {
                "$nin": asser
            }
        })
        for i in findOutDishes_2:
            findOutDishes.append(i)

        dishesInfo_3 = dbb[config.MONGODB_COLLECTION_dishes_3]

        # findOutDishes_3 = dishesInfo_3.find({"prefer":{"$in":prefer},"containsinfolist":{"$nin":asser}},{'id':1,'prefer':1,'containsInfo':1,'containsinfolist':1})
        findOutDishes_3 = dishesInfo_3.find({
            "prefer": {
                "$in": prefer
            },
            "containsinfolist": {
                "$nin": asser
            }
        })

        for i in findOutDishes_3:
            findOutDishes.append(i)

        # print(findOutDishes)
        return findOutDishes
