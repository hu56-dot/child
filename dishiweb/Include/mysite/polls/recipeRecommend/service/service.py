# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-07 16:23:21
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-21 23:26:13

import sys
from random import *


import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append("..")
import numpy as np

from utils import physicalsigns
from conf import config
from dao import mongodb_dao

# 你的输入，



class userInform():
    '''
    用于建立用户的个人身体健康模型
    '''
    def __init__(self,name:str,height:float,weight:float,age:float,gender:str,ID:int,consumption=0,puberty=0,prefer=[],asser={}):
        self.name          = name   # 石亚军
        self.height        = height   # 
        self.weight        = weight
        self.age           = age
        self.gender        = gender
        self.ID            = ID
        # self.passord     = password
        self.consumption   = consumption
        self.mealsPercent  = config.mealsPercent
        self.mealsTypeSize = config.mealsTypeSize
        self.bodyType      = config.bodyType
        self.puberty       = puberty
        self.prefer        = prefer
        self.asser         = asser

        self.connect       = mongodb_dao.mongoDB(config.MONGODB_HOST,port=config.MONGODB_PORT,db=config.MONGODB_NAME)
        
        
    def getUserInform(self):
        '''
        用户信息模块，该模块的信息主要通过提供一个接口，输入用户的信息【年龄性别偏好和消耗等】，
        各项信息输入getUserInform()函数，
        
        1\说明方法或类的逻辑
        2\说明签名的属性、基本解释、类型、默认值
        3\功能调用的方式
        
        该函数功能如下：
        
        1、生成该用户的基本指标信息（包括BMI、偏瘦偏重等的指标信息），返回小孩的所有生理健康指标，
            小孩的指标信息构建的相关功能函数放在utilis.physicalsigns
            BMR,BMI,三餐摄入量：mealsIntake,
        2、为每个用户生成一个唯一的ID，并将数据写入mongodb的userInform数据库，便于后续的个性化信息管理,数据库的写入接口请放在dao.mongodb_dao
        3、2中提到的数据应该是一个json格式，无需嵌套，写为基本的python字典格式即可
        4、利用相关的数据指标生成小孩的个人每日各种食物成分的应该摄入量，成分量和热量含量
        
        【用户类型判定可以使用决策树的方式，尽量不要写大量的条件if-else】
        '''
        #获取BMR值
        BMR           = physicalsigns.calBMR(self.height,self.weight,self.age,self.gender,self.consumption)
        print(BMR)
        #计算BMI值
        BMI           = physicalsigns.calBMI(self.height,self.weight)
        #判断用户类型
        userType      = physicalsigns.calUserType(self.gender,self.age,BMI,self.puberty)
        print(userType)
        #计算个人全天摄入量
        userIntake    = physicalsigns.intake(BMR,userType)
        print(userIntake)
        #计算三餐摄入量
        userThrIntake = physicalsigns.calThrIntake(config.mealsPercent,userIntake)
        
        inform = {
            'ID' : self.ID,
            'name':self.name,
            'age': self.age,
            'height':self.height,
            'weight':self.weight,
            'gender':self.gender,
            'consumption':BMR[1],   # 运动消耗量
            'puberty':self.puberty,  # 是否青春发育期
            'prefer':self.prefer,  # 喜欢的味道 原味、酸甜
            'asser':self.asser,  # 不喜欢吃的
            'BMR':BMR,
            'BMI':BMI,  
            'userType':userType,   # 偏瘦  偏胖
            'userIntake':userIntake,  # 日摄入量
            'userThrIntake':userThrIntake, # 三餐各摄入量
            'dishTypeDailyIntake':physicalsigns.mealsTypesize()  #官方要求的标准量，还未结合身体特征  
                    
        }
        self.connect.wriUserInform(inform=inform,ID = self.ID)
        return inform

    def findById(self,ID):
        infom = self.connect.selectUsrInform(ID)
        return infom

    def recRecipe(self,ID,nums):
        '''
        #同时要指定餐时这一参数，早中晚的思路是一样的，根据餐时选择相关的标准
        1\ 首先需要调用mongodb的信息通过ID获取函数来获得用户的基本信息，这个函数放在mongodb_dao中，
        2\ 通过获取到的食物热量含量信息，去进行早餐的数据查询，请将查询函数放在mongodb_dao中
        3\ 查询的结果在此处拿到后进行返回    
        '''
        thrIntake = self.findById(ID)['userThrIntake']
        # print(thrIntake[0])
        a = randint(1,300)
        b = randint(1,300)
        c = randint(1,300)
        
        breakfast = []
        for i in self.connect.selectBreakfast(calBoundry=thrIntake[0]):
            breakfast.append(i)
            # print(i)
        # print(breakfast)
        launch = []
        for i in self.connect.selectLunch(calBoundry=thrIntake[0]):
            launch.append(i)
        dinner = []
        for i in self.connect.selectDinner(calBoundry=thrIntake[0]):
            dinner.append(i)
        
        
        # breakfast =physicalsigns.generate_thr_recipe_list(self.connect.selectBreakfast(calBoundry=thrIntake[0]))
        # launch = physicalsigns.generate_thr_recipe_list(self.connect.selectLunch(thrIntake[1]))
        # dinner = physicalsigns.generate_thr_recipe_list(self.connect.selectDinner(thrIntake[2]))
        if breakfast[a:a+nums] ==[] :
            a = 0
        if launch[b:b+nums] == [] :
            b = 0
        if dinner[c:c+nums] == []:
            c = 0
        
            
        
        todyRecipe = [breakfast[a:a+nums],launch[b:b+nums],dinner[c:c+nums]]   #算法随机匹配、
        
        return todyRecipe
    
        
    def recDishes(self,ID,kkk): #  kkk的取值为0,1,2,3
        '''
        kkk代表返回前kkk个餐时的搭配
        
        '''
        
        
        #同时指定餐时这一参数，获取各种成分的含量要求，
        '''
        在含量要求部分，首先要利用动态规划算法来获取结果，初步的设计如下
        
        使用动态规划的参数：设定背包的个数，及当前需要遍历的成分个数，使用while循环即可，设置一个字典对结果进行添加
        最终返回最后的结果
        1\在utils库中写出动态规划的方法，即设立三维背包，每个背包代表一种食物成分，完成1000次匹配后，
            如果相关的成分仍然没有,则，将剩余的成分重新创建一个背包，直到当前背包中各种成分的数量都有一定的值为止
        2、线性规划可以解决这个问题，线性规划可以将所有的菜谱提供一个0-1的线性可行解，这个解
        提供了不同的菜谱中对应的成分的多少。
        '''
        
        
        # 首先进行数据的选取
        # 结合用户的偏好和忌口进行筛选
        # 筛选结束后，将所有的菜谱构建出系数矩阵，
        # 利用系数矩阵进行线性规划，
        # 将拿到的结果
        
        # 连续一周的菜谱推荐交给食堂的工作人员
        # 将食谱推送给家长来做，系统设计的复杂性，（不考虑学校吃的情况）
        # 对不同的人群加一个限制，【在学校吃：标准的饮食推荐给食堂，】
        # 这个基本开发就完成了，我们这周会进行基本的接口文档的说明和配置
        inform  = self.findById(ID)
        # print(inform)
        prefer  = inform["prefer"]
        asser   = inform['asser']
        ass     = []
        for i,v in asser.items():
            ass = ass+v    
            ss  = self.connect.selectDishes(prefer=prefer,asser=ass)
        #ss 代表的是从数据库中拿到的所有排除了用户忌口和选择用户偏好的数据
        
        
        #构建线性规划矩阵
        resThr = []  # 三餐推荐结果,可以将i设定为k，用户来指定相关的推荐结果
        
        for i in range(3):
            linearMatrix = []
            dishids={}
            cals = []
            t = 0
            #随机推荐
            # randomSelect = np.random.randint(0, high=len(ss), size=None, dtype='l')
            randomSelect = np.random.randint(0, 10000, size=None, dtype='l')
            # randomSelect = 
            # print(randomSelect)
            for item in ss:  #-----------================这里将是随机推荐的入口======
                if t == randomSelect:
                    continue
                else:
                    dishid,dishvector,cal = physicalsigns.dishesVector(item,config.numsFamily,i)
                    linearMatrix.append(dishvector)
                    dishids[t] = dishid
                    cals.append(int(cal))
                    t=t+1
                
            #进行线性规划求解
            # print(dishids)
            
            res = physicalsigns.linear_match(linearMatrix,config.mealSize[i],cals,inform['userThrIntake'][i],config.numsDishs[i])  # 对早餐的最小量进行优化，推荐菜品数理论上小于10
            
                
        # print(res)
        #构建真实ID与变量解之间的关系
            outttt = {}
            # print(dishids)
            # print(res,end="--------------")
            for k1,_ in res.items():
                # print(dishids[k1])
                outttt[dishids[k1]] =  res[k1]
            resThr.append(outttt)
            
            # print("-------------------------------------\n\n",resThr)
            
        # 用前面拿到的数据ss进行匹配计算
        # 并且生成一定的json格式
        
        #将菜中的主成分进行一个乘积就行了
        
#将{id:pro}的列表生成{id:dishinform}和{id:pro}两个
        abcc = {}
        for iii in range(kkk):
            abc = {}
            print(iii,end = "\n\n\n\------------n\n\n\n")
            for k,v in resThr[iii].items():
                info = self.connect.findd(id = k)
                info["percent"] = v
                # print(k)
                abc[k] = info
            
            abcc[iii] = abc 
            # print(abcc)           
        return abcc
            
    
        
        
        
        
        '''
        先按照克数做线性规划，然后进行热量筛选，热量根据菜谱提供的。
        
        我们的推荐结果有点过于秀气了，只凭借食物类型清单和每一类的含量其实就可以了
        
        对于推荐考虑什么菜的问题，可以借助其他平台的推荐算法，比如京东的商品推荐，（考虑季节属性等等，地域性因素很大【必须做筛选库】，同时基本上都是常规的，）
       @@@@@@ 基于关联算法为他提供相关的食物，=================这一个可以利用数据进行相关的推荐，接入蔬菜平台=========================
        
        
        菜谱的搜索引擎
        '''
        
        
        '''
        有些菜品的主成分没有匹配到，用jieba分词做匹配，遍历的效率比较慢，我们的数据集很庞大，因为嫩芹菜芯匹配芹菜，滑动窗口的匹配效率会非常低，且如果提高效率只能借助搜索引擎这会增加工程开发的复杂性
        
        
        '''



## 

