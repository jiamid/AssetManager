# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from AssetManager.models import AssetDate
from django.http import QueryDict
from io import BytesIO
import xlsxwriter
import datetime
import json
from django.http.multipartparser import MultiPartParser

# Create your views here.

class apiAsset(APIView):
    def post(self,request,*args,**kwargs):
        try:
            body  = eval(request._request.body)
            assetNum1 = body.get('assetNum')

            if AssetDate.objects.filter(assetNum=assetNum1):
                return HttpResponse('已存在')
            assetName1 = body.get('assetName')
            empId1 = body.get('empId')
            userName1 = body.get('userName')
            ownerDept1 = body.get('ownerDept')
            adminId1 = body.get('adminId')
            tagText1 = body.get('tagText')

            AssetDate.objects.create(assetNum=assetNum1, assetName=assetName1, empId=empId1, \
                                     userName=userName1, ownerDept=ownerDept1, adminId=adminId1, tagText=tagText1)
            res = {'code': 200, 'data': '创建成功'}
        except Exception as e:
            res = {'code': 200, 'data': '创建失败' }
        return JsonResponse(res)

    def get(self,request,*args,**kwargs):
        if  request._request.GET.get('assetNum') is None :
            oneData = AssetDate.objects.all().values()
        else:
            assetNum = request._request.GET.get('assetNum')
            oneData = AssetDate.objects.filter(assetNum=assetNum).values()
            #print(oneData[0].get('lastTime'))
        res = {'code': 200, 'data': list(oneData)}
        return JsonResponse(res,safe=False)

    def put(self,request,*args,**kwargs):
        res = {'code': 200, 'data': 'put成功'}
        try:
            data = request._request.body
            data = eval(list(QueryDict(data).keys())[0])
            assetNum1 = data.get('assetNum')
            if assetNum1:
                xx = AssetDate.objects.get(assetNum=assetNum1)
                xx.assetName = data.get('assetName')
                xx.empId = data.get('empId')
                xx.userName = data.get('userName')
                xx.ownerDept = data.get('ownerDept')
                xx.adminId = data.get('adminId')
                xx.tagText = data.get('tagText')
                xx.save()
        except Exception as e :
            res = {'code': 201, 'data': 'put失败'}
        return JsonResponse(res)

    def delete(self,request,*args,**kwargs):
        res = {'code': 200, 'msg': 'del成功'}
        try:
            body = eval(request._request.body)
            assetNum1 = body.get('assetNum')
            delOne = AssetDate.objects.get(assetNum=assetNum1)
            delOne.delete()
        except Exception as e:
            res = {'code': 201, 'msg': 'del失败'}
        return JsonResponse(res)

class getAssets(APIView):
    def get(self,request,*args,**kwargs):
        oneData = AssetDate.objects.all().values()
        x_io = BytesIO()
        work_book = xlsxwriter.Workbook(x_io)
        work_sheet = work_book.add_worksheet()
        work_sheet.set_column(0,2,14)
        work_sheet.set_column(3,3,8)
        work_sheet.set_column(4,5,10)
        work_sheet.set_column(6,6,15)
        work_sheet.set_column(7,7,30)
        boldStyle = work_book.add_format({'border': 1, 'align': 'center', 'valign': 'vcenter', 'bold': True})
        style = work_book.add_format({'align': 'center', 'valign': 'vcenter'})
        work_sheet.merge_range('A1:H1', '资产数据汇总', boldStyle)
        titleTag = ['资产编号', '资产名称', '用户工号', '用户姓名','资产归属','管理账号','备注','最后修改时间']
        work_sheet.write_row('A2', titleTag, boldStyle)
        flag = 3
        for one in oneData:
            one_time  = one.get('lastTime') + datetime.timedelta(hours=8)
            one_time = one_time.strftime('%Y-%m-%d %H:%M:%S')

            one_row = [one.get('assetNum'),one.get('assetName'),one.get('empId'), \
                       one.get('userName'),one.get('ownerDept'),one.get('adminId'), \
                       one.get('tagText'),one_time]
            work_sheet.write_row('A'+ str(flag), one_row, style)
            flag += 1
        work_book.close()
        res = HttpResponse()
        res["Content-Type"] = "application/octet-stream"
        res["Content-Disposition"] = 'filename="AllAsset.xlsx"'
        res.write(x_io.getvalue())
        return res

    def post(self,request,*args,**kwargs):
        try:
            print(request._request.body)
            body  = eval(request._request.body)
            assetNum1 = body.get('assetNum')
            if AssetDate.objects.filter(assetNum=assetNum1):
                return HttpResponse('已存在')
            assetName1 = body.get('assetName')
            empId1 = body.get('empId')
            userName1 = body.get('userName')
            ownerDept1 = body.get('ownerDept')
            adminId1 = body.get('adminId')
            tagText1 = body.get('tagText')

            AssetDate.objects.create(assetNum=assetNum1, assetName=assetName1, empId=empId1, \
                                     userName=userName1, ownerDept=ownerDept1, adminId=adminId1, tagText=tagText1)
            res = {'code': 200, 'data': '创建成功'}
        except Exception as e:
            res = {'code': 200, 'data': '创建失败' }
        return JsonResponse(res)
    def delete(self,request,*args,**kwargs):
        res = {'code': 200, 'msg': 'del成功'}
        oneData = AssetDate.objects.all()
        for x in oneData:
            print(x)
            print('已删除')
            x.delete()
        return JsonResponse(res)

