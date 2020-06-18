from django.shortcuts import render
from django.http import HttpResponse
from AssetManager.models import AssetDate
# Create your views here.
from django.views import View


def index(request):
    try:
        allAssetData = AssetDate.objects.all()
    except:
        return HttpResponse('数据库获取失败')
    #return HttpResponse(allAssetData)
    return render(request,'index.html',{'allAssetData':allAssetData})


def addPage(request):
    return render(request,'addOne.html')



def assetOne(request,assetNum):
    oneData = AssetDate.objects.get(assetNum = assetNum)
    return render(request,'OneData.html',{'oneData':oneData})

def addOneAsset(request):
    try:
        if  request.POST :
            assetNum1 = request.POST.get('assetNum')
            if AssetDate.objects.filter(assetNum = assetNum1):
                return HttpResponse('已存在')
            assetName1 = request.POST.get('assetName')
            empId1 = request.POST.get('empId')
            userName1 = request.POST.get('userName')
            ownerDept1 = request.POST.get('ownerDept')
            adminId1 = request.POST.get('adminId')
            tagText1 = request.POST.get('tagText')
            AssetDate.objects.create(assetNum = assetNum1,assetName = assetName1,empId = empId1,\
                                            userName = userName1,ownerDept = ownerDept1,adminId = adminId1, tagText = tagText1)
    except Exception as e:
        return HttpResponse(e)
    return render(request,'status.html',{'message':'添加成功'})

def delOneAsset(request):
    try:
        if  request.POST:
            assetNum1 = request.POST.get('assetNum')
            delOne = AssetDate.objects.get(assetNum = assetNum1)
            delOne.delete()
    except Exception as e:
        print(e)
        print('删除失败')
        return HttpResponse('删除失败')
    print(request.POST.get('assetNum'))
    print('删除成功')
    return HttpResponse('删除成功')

def apiAsset(request):
    pass
