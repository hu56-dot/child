# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-18 10:14:29
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-21 22:29:35
# Create your views here.
from bson import json_util
from django.http import HttpResponse,HttpResponseRedirect
import os
import sys
import json
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.base import View

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append("..")
from recipeRecommend.main import gte_dish, gte_daily,userInformManagement


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def userInform(request):
    try:
        name        = request.POST.get('name', '')
        # print(name)
        id          = request.POST.get('id', '')
        # print(id)
        height      = request.POST.get('height', '')
        weight      = request.POST.get('weight', '')
        age         = request.POST.get('age', '')
        gender      = request.POST.get('gender', '')
        consumption = request.POST.get('consumption', '')
        puberty     = request.POST.get('puberty', '')
        prefer      = request.POST.get('prefer', '')
        asser       = request.POST.get('asser', '')
        
        
        if name== '':
            name = 'yajun'
        if id == '':
            id = 0
        if age == '':
            age = 9.5
        if height == '':
            height = 140.0
        if weight == '':
            weight = 40.0
        if gender == '':
            gender = '男'
        if prefer == '':
            puberty = 0
        

        if consumption == '':
            consumption = float(0)
        
        
        preferee = []
        if prefer=='':
            prefer = ['超辣','葱香','果味','酱香','咖喱','苦味','麻辣','奶香','其他','清淡','酸辣','酸甜','酸咸','蒜香','甜味','微辣','五香','咸甜','咸鲜','香草','鱼香','原味','糟香','中辣','孜然']
        else:
            # print(prefer)
            for i in prefer.split(','):
                # print(i,end="-------------------------------- ")
                preferee.append(i)
            prefer = preferee
        
        # print(preferee[0],type(preferee))
        assera = {}
        
        if asser == '':
            asser = {'很棒':['很棒','很棒']}
        else:  
            for i in asser.split(','):
                ii = i.split(':')
                # print(ii)
                assera[ii[0]] = [t for t in ii[1].split('\\')]
            # print(assera,type(assera))
            
            asser = assera        
        
        
        print(name,id,height, 'drfsfg',weight,age,gender,consumption,puberty,'dsgfdg',prefer,asser)

        # 判断参数中是否含有a和b
        # 各个值不能取0
        
        if name and id and height and weight and age and gender  :
            ok,res = userInformManagement(name = str(name), ID = int(id), height = float(height), weight = float(weight), age = float(age),gender = str(gender), consumption = float(consumption),puberty = int(puberty),prefer = prefer,asser = asser)
            if ok: 
                out = json_util.dumps(res,ensure_ascii=False)
                # return HttpResponse(dic,content_type='application/json ,charset=utf-8')
                return render(request,'outdish.html',{'out':out})
            else:
                return HttpResponse('信息没有录入成功')
        else:
            return HttpResponse('输入错误')
    except:
        return HttpResponse("{'status':'fail', 'msg':'多试几次！'}",
                                content_type='application/json')





#获取菜谱+成分推荐
def get_dish(request):
    '''
    参数小于3
    '''
    try:
        print(request)
        ID = request.GET.get('id', 1)
        q = request.GET.get('nums', default=1)
        out = 0

        
        if ID:
            a = gte_dish(id=int(ID), kkk=int(q))
            # print(a)
            # outs = json.dumps(s[:int(q)])
            out = json_util.dumps(a, ensure_ascii=False)
            print(out,end="---------------------------")
        if out:
            # return HttpResponse(out,
                                # content_type='application/json ,charset=utf-8')
            return render(request,'outdish.html',{'out':out})
        # return redirect('dish?id={}&nums={}'.format(ID,q))
        # return redirect('')
        # cc = '/echorec/dish?id={}&nums={}'.format(ID,q)
        # print(cc)
        # return HttpResponseRedirect(cc)
    except :
        return HttpResponse("{'status':'fail', 'msg':'多试几次！'}",
                                content_type='application/json')
        
        
   




    # def get_daily(request):
    #     ID = request.GET.get("id", '')
    #     q = request.GET.get("nums", '')
    #     if ID:
    #         s = gte_daily(id=int(ID), nums=int(q))
    #         out = json_util.dumps(s, ensure_ascii=False)
    #     if out:
    #         return render(request,'outdish.html',{'out':out})
    #         return HttpResponse(out, content_type='application/json,charset=utf-8')
    #     else:
    #         return HttpResponse("{'status':'fail', 'msg':'多试几次！'}",
    #                             content_type='application/json')


#获取每天的三餐推荐

class tess(View):
    def get(self,request):
        try:
            ID = request.GET.get("id", '')
            q = request.GET.get("nums", '')
            if ID:
                s = gte_daily(id=int(ID), nums=int(q))
                out = json_util.dumps(s, ensure_ascii=False)
            if out:
                return render(request,'outdish.html',{'out':out})
                return HttpResponse(out, content_type='application/json,charset=utf-8')
            else:
                return HttpResponse("{'status':'fail', 'msg':'多试几次！'}",
                                    content_type='application/json')
        except :
            return HttpResponse("{'status':'fail', 'msg':'多试几次！'}",
                                content_type='application/json')
