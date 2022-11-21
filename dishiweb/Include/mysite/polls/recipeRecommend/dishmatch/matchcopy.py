# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-10-28 21:58:26
# @Last Modified by:   echo.suisui echojarn@gmail.com

from os import curdir
import json
import pandas as pd
import os


class IngredientsMatch():
    def __init__(self,path,sheetInfo):
        '''
        该path是一个三元的列表，包含食谱path、成分类型path、json path
        '''
        self.curDir = os.path.dirname(os.path.abspath(__file__))
        
        self.path = [os.path.join(self.curDir,x) for x in path]
        self.recipePath = self.path[0]
        self.containsTypePah = self.path[1]
        self.jsonPath = self.path[2]
        self.recipeSheetname,self.recipeColumns,self.typeSheetname,self.typeColumns = \
            sheetInfo['recipeSheetname'],sheetInfo['recipeColumns'],sheetInfo['typeSheetname'],sheetInfo['typeColumns']
        
        
    def testobjectRecipe(self):
        
        print(self.curDir)
        print(self.path)
        print(self.recipePath)
        print(self.containsTypePah)
        print(self.jsonPath)
        
        
        return 0
    
    def objectRecipe(self,start,end,p,z1):
        print("这是第{}个线程".format(p))
        with open(self.jsonPath,'w',encoding='utf-8') as f:
            f.write('{ "match":[')
            
            # dfRecipe = pd.read_excel(self.recipePath)
            # print("读取完毕...\n")
            # # dfRecipe =  pd.DataFrame(dfRecipe)
            # # print(dfRecipe)
            # mainInform = dfRecipe.iloc[:,:3]
            # z = list(mainInform.values)
            # z1 = [list(x[2:]) for x in z]
            # print(len(z1))
            for i in range(start,end):
                finish = int(i/10)
                not_finish = 100-finish
                s = '#'*finish+'-'*not_finish
                
                if self.match(z1[i]) == -1:
                    continue
                else:
                    # print(z[i][0])
                    # print(self.match(z1[i]))
                    json_out = self.generateJson(i,z[i][0],self.match(z1[i]))
                    # a[z[i][0]] = self.match(z1[i])
                    jsonDict = json.dumps(json_out,ensure_ascii=False)
                    # print(jsonDict)
                    try:
                        
                        f.write("{},".format(jsonDict))
                        print("第{}条数据写入成功".format(i))
                        print("第{}个线程的当前进度为{}% : {}".format(i,finish,s),end = '\n\n')
                
                    except:
                        print("第{}条数据写入失败".format(i))
                        pass
            f.write(']}')  
        


    def generateJson(self,p,z,y):
        
        outt = {}
        for _,v in y.items():
            
            for k1,v1 in v.items():
                dd = {
                        'type':k1,
                        "size":v1[-1],
                        'calory':v1[1],
                        'others':v1[2:8]
                }
                outt[v1[0]] = dd
                        
        outT = {
            'id': p ,
            'name': z,
            'containsInfo':outt
        }
        
        return outT
        
    
    def match(self,boo):
        d = {}
        boo = self.containsSegment(boo[0])
        # print(boo[1][1])
        for i in range(len(boo)):
            if self.findMatch(boo[i])==-1:
                continue
            else:
                d[i] = self.findMatch(boo[i])

        if len(d) == 0:
            return -1
        else:
            # print(d)
            return d
        
    def findMatch(self,strrr):
        c = {}
        # print(strrr)
        a = self.transferPdtoDict()
        # print(a)
        for k,v in a.items():
            b = []
            for vv in v:
                if strrr[0] == vv[0]:
                    
                    ## 这里可以进行计量单位的匹配
                    vv.append(strrr[1])
                    # print(vv)
                    c[k] = vv
                else:
                    continue
            
                
        if len(c) == 0:
            return -1
        else:
            # print(c)
            return c
        
        
        
    def transferPdtoDict(self):
        dfTypes = {}
        for i in self.typeSheetname:
            b = pd.read_excel(self.containsTypePah,sheet_name=i)
            c = pd.DataFrame(b)
            # print(c)
            c = c.loc[:,self.typeColumns]
            c = [ list(j) for j in list(c.values)]
            dfTypes[i] = c
        return dfTypes
            
    def containsSegment(self,strr):
        a = []     
        text = str(strr).split(',') 
        for i in text:
            i = i.split(":")
            bb = []
            for s in i :
                s = s.replace(" ","")             
                bb.append(s)     
            a.append(bb)
        return a



def mai(start,end,i,z1):
    # test 
    import datetime
    s = '%d%H%M%S'+str(i)
    thetime = datetime.datetime.now().strftime(s)
    b = 'outJson\matchOut'+thetime+'.json'
    files = ['recipe.xlsx','type.xlsx',b]
    sheetInfo = {
        'recipeSheetname':["Sheet1"],
        'recipeColumns':['name','intruction','maincontains'],
        'typeSheetname':['谷薯芋、杂豆、主食','蔬菜类','饮料','坚果、大豆及制品','鱼虾水产类',
                         '蛋类','奶类及制品','肉类及制品','菌藻类','水果类','零食、点心、冷饮','速食食品'], #,'调味品'],
        'typeColumns':['name','calory','url','碳水化合物','脂肪','蛋白质','纤维素']

        }
    # print(sheetInfo['recipeColumns'])
    
    a = IngredientsMatch(files,sheetInfo)
    a.objectRecipe(start,end,i,z1)

    
  
a = [[x*1000+1,(x+1)*1000] for x in range(136)]

# def ss(start,end):
#     print(start,end,end='\n\n') 


curDir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(curDir,'recipe.xlsx') 
print("开始读取食谱文件...\n")
dfRecipe = pd.read_excel(path)
print("读取完毕...\n")
# dfRecipe =  pd.DataFrame(dfRecipe)
# print(dfRecipe)
mainInform = dfRecipe.iloc[:,:3]
z = list(mainInform.values)
z1 = [list(x[2:]) for x in z]
# print(len(z1)) 
 
 
from threading import Thread
for i in range(len(a)):
    
    thred = Thread(target=mai,args=(a[i][0],a[i][1],i,z1))
    thred.start()    
    
   