# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-08 00:54:37
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-21 21:10:13
import sys

sys.path.append('..')
from conf import config


# 计算用户的BMR值
def calBMR(height: float, weight: float, age: float, gender: str, cons):
    # 生成性别代号
    if gender == '男':
        genderId = 1
    else:
        genderId = 0

    if float(age) >= 6.0 and float(age) <= 10.0 :
        ageId = 0
    else:
        ageId = 1

    baseBmr = 10 * weight + 6.25 * height - 5 * age + config.bmrDiffGender[
        genderId]
    arg = config.sportBmrArgs[ageId][genderId]
    if cons == 0:
        sportBmr = 420 * (arg[0] * weight + arg[1]) / 1440
    else:
        sportBmr = cons

    bmr = [baseBmr, sportBmr]

    return bmr


def calBMI(height: float, weight: float):
    bmi = weight / ((height / 100)**2)

    return bmi


#判断用户类型
def calUserType(gender: str, age: float, bmi: float, puberty: int):
    '''
    puberty: value = 0 or 1
    '''
    if puberty == 1 and gender == '女':
        return 4

    elif puberty == 1 and gender == '男':
        return 3

    else:
        # 生成性别代号
        if gender == '男':
            genderId = 1
        else:
            genderId = 0

        # 男
    if genderId == 1:
        # 9岁
        if age >= 9 and age < 10:
            if bmi >= 20.8:
                return 2
            elif 18.9 <= bmi < 20.8:
                return 1
            elif bmi < 14:
                return -1
            else:
                return 0

        # 10岁
        elif age >= 10 and age < 11:
            if bmi >= 21.9:
                return 2
            elif 19.6 <= bmi < 21.9:
                return 1
            elif bmi < 14.3:
                return -1
            else:
                return 0

        # 11岁
        elif age >= 11 and age < 12:
            if bmi >= 23:
                return 2
            elif 20.3 <= bmi < 23:
                return 1
            elif bmi < 14.7:
                return -1
            else:
                return 0

        # 12岁
        elif age >= 12 and age < 13:
            if bmi >= 24.1:
                return 2
            elif 21 <= bmi < 24.1:
                return 1
            elif bmi < 15.1:
                return -1
            else:
                return 0

        else:
            return 0

    # 女
    if genderId == 0:
        # 9岁
        if age >= 9 and age < 10:
            if bmi >= 20.4:
                return 2
            elif 19 <= bmi < 20.4:
                return 1
            elif bmi < 13.7:
                return -1
            else:
                return 0

        # 10岁
        if age >= 10 and age < 11:
            if bmi >= 21.5:
                return 2
            elif 20 <= bmi < 21.5:
                return 1
            elif bmi < 14.1:
                return -1
            else:
                return 0

        # 11岁
        if age >= 11 and age < 12:
            if bmi >= 22.7:
                return 2
            elif 21.1 <= bmi < 22.7:
                return 1
            elif bmi < 14.6:
                return -1
            else:
                return 0

        # 12岁
        elif age >= 12 and age < 13:
            if bmi >= 23.9:
                return 2
            elif 21.9 <= bmi < 23.9:
                return 1
            elif bmi < 15.2:
                return -1
            else:
                return 0

        else:
            return 0


#计算个人摄入量
def intake(bmr: list, userType: int):
    '''
    cons:consumption
    '''
    if userType == 4:
        perIntake = config.girlIntakePuberty
        return perIntake
    elif userType == 3:
        perIntake = config.boyIntakePuberty
        return perIntake

    else:
        perIntake = (sum(bmr)) * config.userTypePer[userType]

        return perIntake


def calThrIntake(percent, intake: float):
    '''
    percent: Proportion of meals consumed  [[0.25,0.3],[0.3,0.4],[0.3,0.35]]
    '''
    calThrIntak = []
    for i in percent:
        a = []
        for j in i:
            print(j,intake)
            a.append(j * intake)
        calThrIntak.append(a)

    return calThrIntak


# print(calThrIntake([[0.25,0.3],[0.3,0.4],[0.3,0.35]],1230))


#这里是一个每天标准摄入的计算
def mealsTypesize():
    cc = {}
    for k, v in config.mealsTypeSize.items():
        singleType = []
        for i in config.mealsPercent:
            d = [i[0] * v[0], i[1] * v[1]]
            singleType.append(d)
        cc[k] = singleType
    return cc


# print(mealsTypesize())

# 测试用例
# '''
# 性别：女
# 年龄：10
# 身高：158
# 体重：40
# 偏好：酸甜、微辣、咸鲜
# 忌口：牛奶、大豆
# '''
# print(cal_BMR(158,40,10,'男'))


def generate_thr_recipe_list(s):
    a = []
    for ss in s:
        # print(s)
        a.append(s)

    return a


# 针对一条记录进行矩阵填充
# mealsTypeSize = {"谷薯类":[120,140],"蔬菜类":[140,160],
#  "水果类":[80,100],"畜禽肉类":[16,20],"鱼虾类":[16,20],"蛋类":[20,20],
#  "奶类及制品":[80,80],"大豆及其制品和坚果":[35,35]}


def dishesVector(dish, familyNumbers, j):
    gredientsize = [0, 0, 0, 0, 0, 0, 0, 0]
    contain = dish['containsInfo']
    call = [0, 0, 0, 0, 0, 0, 0, 0]

    # print(contain)
    for i in range(len(contain)):
        v = contain[i]
        if v['calory[千卡(每100克)]'] < config.highCalR[j]:
            bb = v['含量（g）'] / familyNumbers
            call[i] = v['calory[千卡(每100克)]'] * bb / 100

            if v['type'] == '谷薯类':
                gredientsize[0] = bb
            elif v['type'] == '蔬菜类':
                gredientsize[1] = bb
            elif v['type'] == '水果类':
                gredientsize[2] = bb
            elif v['type'] == '畜禽肉类':
                gredientsize[3] = bb
            elif v['type'] == '鱼虾类':
                gredientsize[4] = bb
            elif v['type'] == '蛋类':
                gredientsize[5] = bb
            elif v['type'] == '奶类及制品':
                gredientsize[6] = bb
            else:
                gredientsize[7] = bb
        else:
            continue

    return dish['id'], gredientsize, sum(call)


#构造菜品搭配的线性规划求解器

import numpy as np
from scipy import optimize
import cvxpy as cp


def linear_match(matrix_, bias, cals, mealstotalcal, dish_nums):
    d = len(cals)
    # print(mealstotalcal)
    # print(matrix_)
    sing = np.array([1 for i in range(len(cals))])
    A = np.array(matrix_).T
    B_1 = np.array([i[0] for i in bias])
    B_2 = np.array([i[1] for i in bias])

    x = cp.Variable(d, integer=False)  #定义两个整数决策变量
    # print(cals)
    print(np.shape(A), np.shape(x.T), np.shape(B_1))
    obj = cp.Minimize(cals * x - sum(mealstotalcal) / 2)  #构造目标函数
    # print(obj)
    cons = [
        A * x >= B_1, A * x <= B_2, x >= 0, x <= 1,
        cals * x - mealstotalcal[0] >= 0, cals * x - mealstotalcal[1] <= 0,
        cp.sum(x) <= dish_nums[1],
        cp.sum(x) >= dish_nums[0]
    ]  #构造约束条件

    prob = cp.Problem(obj, cons)  #构建问题模型

    prob.solve(solver='GLPK_MI')  #求解问题

    print("最优值为:", prob.value)
    # print("最优解为：\n",x.value)
    # print("x的和为:",cp.sum(x.value))

    explain_id = {}
    outMatrix_ = []
    outMatrix_A = []

    for j in range(len(x.value)):
        if x.value[j] != 0:
            explain_id[j] = x.value[j]
            outMatrix_.append(x.value[j])
            outMatrix_A.append(matrix_[j])
    # 生成结果矩阵
    outArray_x = np.array(outMatrix_).reshape(len(outMatrix_), 1)
    outArray_A = np.array(outMatrix_A)
    gredientsMatrix = np.dot(outArray_A.T, outArray_x)
    # print(gredientsMatrix)
    return explain_id


def dpBag_match(matrix_, bias, cals, mealstotalcal, dish_nums):
    pass



''''''
# a = [ ]
# a = { } hash哈希算法