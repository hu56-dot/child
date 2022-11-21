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
        '''
        用于测试path的读取
        '''
        print(self.curDir)
        print(self.path)
        print(self.recipePath)
        print(self.containsTypePah)
        print(self.jsonPath)
        return 0

    
    def objectRecipe(self):
        with open(self.jsonPath,'w',encoding='utf-8') as f:
            f.write('{ "match":[')
            print("开始读取食谱文件...\n")
            print(self.recipePath)
            dfRecipe = pd.read_excel(self.recipePath)
            print("读取完毕...\n")
            # dfRecipe =  pd.DataFrame(dfRecipe)
            # print(dfRecipe)
            mainInform = dfRecipe.iloc[:,:]
            # print(mainInform)
            z = list(mainInform.values)
            print(z)
            z1 = [list(x[1:7]) for x in z]
            # print(z1)
            print(len(z1))
            z2 = []
            for kk in range(len(z1)):
                g = z1[kk]
                z22 = str(g[0])+':'+str(g[1])+','+str(g[2])+':'+str(g[3])+','+str(g[4])+':'+str(g[5])
                
                print(z22)
                z2.append([z22])
            
            
            
            for i in range(len(z2)):
                # finish = i/(len(z1))
                # not_finish = 1-finish
                # s = '#'*int(finish*100)+'-'*int(not_finish*100)
                # print("当前进度{}% : {}".format(int(finish*100),s))
                
                
                if self.match(z2[i]) == -1:
                    continue
                else:
                    # print(z[i])
                    # print(z[i][0])
                    # print(self.match(z1[i]))
                    json_out = self.generateJson(i,z[i],self.match(z2[i]))
                    # a[z[i][0]] = self.match(z1[i])
                    jsonDict = json.dumps(json_out,ensure_ascii=False)
                    # print(jsonDict)
                    try:
                        
                        f.write("{},".format(jsonDict))
                        print("第{}条数据写入成功,        当前进度为{}%".format(i,i*100/62415))
                    except:
                        print("第{}条数据写入失败".format(i))
                        pass
            f.write(']}')  
        


    def generateJson(self,p,z,y):
        
        outt = {}
        ingredients = []
        for _,v in y.items():
            
            for k1,v1 in v.items():
                # ['name','calory[千卡(每100克)]','碳水化合物（g）','脂肪（g）','蛋白质（g）','纤维素（g）']
                dd = {
                        'type':k1,
                        "含量（g）":v1[-1],
                        'calory[千卡(每100克)]':v1[1],
                        '碳水化合物（g）':v1[2],
                        '脂肪（g）':v1[3],
                        '蛋白质（g）':v1[4],
                        '纤维素（g）':v1[5]
                }
                outt[v1[0]] = dd
                ingredients.append(v1[0])
                        
        outT = {
            'id': p ,
            'name': z[0],
            'introduxtion':z[7],
            'ingredients':z[8],
            'type':z[9],
            'feature':z[10],
            'level':z[11],
            'method':z[12],
            'time':z[13],
            'prefer':z[14],
            'containsInfo':outt,
            'containsInfolist' : ingredients
        }
        
        return outT
        
    
    def match(self,boo):
        d = {}
        # print(boo,end="dsgaf---------\n\n")
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



def main():
    # test 
    import datetime
    s = '%Y%m%d%H%M%Sf'
    thetime = datetime.datetime.now().strftime(s)
    b = '.\\outJson\\matchOut'+thetime+'.json'
    files = ['data\\recipe_1.xlsx','data\\type.xlsx',b]
    sheetInfo = {
        'recipeSheetname':["Sheet1"],
        'recipeColumns':['name','intruction','maincontains'],
        # 'typeSheetname':['谷薯芋、杂豆、主食','蔬菜类','饮料','坚果、大豆及制品','鱼虾水产类',
        #                  '蛋类','奶类及制品','肉类及制品','菌藻类','水果类','零食、点心、冷饮','速食食品'], #,'调味品'],
        'typeSheetname':['谷薯类','蔬菜类','水果类','畜禽肉类','鱼虾类','蛋类','奶类及制品','大豆及其制品和坚果'],
        'typeColumns':['name','calory[千卡(每100克)]','碳水化合物（g）','脂肪（g）','蛋白质（g）','纤维素（g）']

        }
    # print(sheetInfo['recipeColumns'])
    
    a = IngredientsMatch(files,sheetInfo)
    a.objectRecipe()
    # a.testobjectRecipe()

if __name__ == '__main__':
    main()
    
  
    
    
   