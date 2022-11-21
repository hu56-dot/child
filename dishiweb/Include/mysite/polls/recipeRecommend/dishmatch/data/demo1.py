# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-07 16:18:07
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-08 00:25:27
import pandas as pd


def rec_diet(high, weight, age, gender, consumption):
    '''
    high：单位为cm
    weight：单位为kg
    age：单位为年
    gender：1为男，0为女
    consumption：为用户输入，单位为kcal（这里不确定输入的单位是什么，可能之后要进行换算）
    '''

    # 计算基础代谢率BMR
    if gender == 1:
        BMR = 10 * weight + 6.25 * high - 5 * age + 5
    else:
        BMR = 10 * weight + 6.25 * high - 5 * age - 161

    # 计算BMI
    BMI = weight / ((high/100) ** 2)
    # 判断用户类型，肥胖1、正常0、偏瘦-1
    user_type = find_type(gender, age, BMI)

    # 计算标准饮食摄入量stdIntake
    std_intake = BMR + consumption

    # 计算个人推荐饮食摄入量intake
    if user_type == -1:
        intake = std_intake + 500
        print("用户体型偏瘦")

    elif user_type == 1:
        intake = std_intake - 500
        print("用户体型偏胖")

    else:
        intake = std_intake
        print("用户体型正常")

    # 推荐具体食谱
    rec(age, intake)


def find_type(gender, age, BMI):
    # 男
    if gender == 1:
        # 6岁
        if age == 6:
            if BMI >= 16.9:
                return 1
            elif BMI < 13.4:
                return -1
            else:
                return 0
        # 7岁
        elif age == 7:
            if BMI >= 17.4:
                return 1
            elif BMI < 13.6:
                return -1
            else:
                return 0
        # 8岁
        elif age == 8:
            if BMI >= 18.1:
                return 1
            elif BMI < 13.8:
                return -1
            else:
                return 0
        # 9岁
        elif age == 9:
            if BMI >= 18.9:
                return 1
            elif BMI < 14.0:
                return -1
            else:
                return 0
        # 10岁
        elif age == 10:
            if BMI >= 19.6:
                return 1
            elif BMI < 14.3:
                return -1
            else:
                return 0
        # 11岁
        elif age == 11:
            if BMI >= 20.3:
                return 1
            elif BMI < 14.7:
                return -1
            else:
                return 0
        # 12岁
        elif age == 12:
            if BMI >= 21.0:
                return 1
            elif BMI < 15.1:
                return -1
            else:
                return 0
        # 13岁
        elif age == 13:
            if BMI >= 21.9:
                return 1
            elif BMI < 15.7:
                return -1
            else:
                return 0
        # 14岁
        elif age == 14:
            if BMI >= 22.6:
                return 1
            elif BMI < 16.3:
                return -1
            else:
                return 0
        # 15岁
        elif age == 15:
            if BMI >= 23.1:
                return 1
            elif BMI < 17.3:
                return -1
            else:
                return 0
        # 16岁
        elif age == 16:
            if BMI >= 23.5:
                return 1
            elif BMI < 17.7:
                return -1
            else:
                return 0
        # 17岁
        elif age == 17:
            if BMI >= 23.8:
                return 1
            elif BMI < 18.1:
                return -1
            else:
                return 0

        else:
            print("非学龄儿童")

    # 女
    else:

        # 6岁
        if age == 6:
            if BMI >= 16.7:
                return 1
            elif BMI < 13.1:
                return -1
            else:
                return 0
        # 7岁
        elif age == 7:
            if BMI >= 17.2:
                return 1
            elif BMI < 13.2:
                return -1
            else:
                return 0
        # 8岁
        elif age == 8:
            if BMI >= 18.1:
                return 1
            elif BMI < 13.4:
                return 0
            else:
                return -1
        # 9岁
        elif age == 9:
            if BMI >= 19.0:
                return 1
            elif BMI < 13.7:
                return -1
            else:
                return 0
        # 10岁
        elif age == 10:
            if BMI >= 20.0:
                return 1
            elif BMI < 14.1:
                return -1
            else:
                return 0
        # 11岁
        elif age == 11:
            if BMI >= 21.1:
                return 1
            elif BMI < 14.6:
                return -1
            else:
                return 0
        # 12岁
        elif age == 12:
            if BMI >= 21.9:
                return 1
            elif BMI < 15.2:
                return -1
            else:
                return 0
        # 13岁
        elif age == 13:
            if BMI >= 22.6:
                return 1
            elif BMI < 15.8:
                return -1
            else:
                return 0
        # 14岁
        elif age == 14:
            if BMI >= 23.0:
                return 1
            elif BMI < 16.3:
                return -1
            else:
                return 0
        # 15岁
        elif age == 15:
            if BMI >= 23.4:
                return 1
            elif BMI < 16.7:
                return -1
            else:
                return 0
        # 16岁
        elif age == 16:
            if BMI >= 23.7:
                return 1
            elif BMI < 16.9:
                return -1
            else:
                return 0
        # 17岁
        elif age == 17:
            if BMI >= 23.8:
                return 1
            elif BMI < 17.1:
                return -1
            else:
                return 0

        else:
            print("非学龄儿童")


def rec(age, intake):
    # 计算三餐推荐摄入量限制limit
    low_breakfast = intake * 0.25
    up_breakfast = intake * 0.3
    low_lunch = intake * 0.3
    up_lunch = intake * 0.4
    low_dinner = intake * 0.3
    up_dinner = intake * 0.35

    # 早餐
    # 读取早餐饮食数据，删除不用的行和列
    df = pd.read_excel("早、中、晚餐食谱-热量.xlsx", sheet_name=0, skiprows=9, usecols=(0, 1, 2, 3, 4, 5, 6))

    # 寻找合适的热量限制
    df = df.loc[(df['热量总计'] >= low_breakfast) & (df['热量总计'] <= up_breakfast)]

    # 输出食谱
    print("早餐推荐")
    print(df.head(5))

    # 午餐
    # 读取午餐饮食数据，删除不用的行和列
    df = pd.read_excel("早、中、晚餐食谱-热量.xlsx", sheet_name=1, skiprows=9, usecols=(0, 1, 2, 3, 4, 5, 6))

    # 寻找合适的热量限制
    df = df.loc[(df['热量总计'] >= low_lunch) & (df['热量总计'] <= up_lunch)]

    # 输出食谱
    print("午餐推荐")
    print(df.head(5))

    # 晚餐
    # 读取晚餐餐饮食数据，删除不用的行和列
    df = pd.read_excel("早、中、晚餐食谱-热量.xlsx", sheet_name=2, skiprows=9, usecols=(0, 1, 2, 3, 4, 5, 6))

    # 寻找合适的热量限制
    df = df.loc[(df['热量总计'] >= low_dinner) & (df['热量总计'] <= up_dinner)]

    # 输出食谱
    print("晚餐推荐")
    print(df.head(5))


# 测试
# rec_diet(high, weight, age, gender, consumption)
# 身高165cm, 体重45kg, 13岁, 男性
rec_diet(150, 40, 13, 1, 0)

