import xlrd
import requests
import json

class RUasset():
    def __init__(self,url='http://10.8.40.218/api/v1/getAsset/',filename = 'Assets.xls',dbname = 'one'):
        self.filename = filename
        self.dbname = dbname
        self.url = url
        self.assetNums = []
        self.assetNames = []
        self.empIds = []
        self.userNames = []
        self.ownerDepts = []
        self.adminIds = []
        self.tagTexts = []
        
    def getAsset(self):
        db = xlrd.open_workbook(self.filename)
        sheet = db.sheet_by_name(self.dbname)
        self.assetNums = sheet.col_values(0)[1:]
        self.assetNames = sheet.col_values(1)[1:]
        self.empIds = sheet.col_values(2)[1:]
        self.userNames = sheet.col_values(3)[1:]
        self.ownerDepts = sheet.col_values(4)[1:]
        self.adminIds = sheet.col_values(5)[1:]
        self.tagTexts = sheet.col_values(6)[1:] 
        
    def updataAsset(self):
        for x in range(len(self.assetNums)):
            formdata = {
                'assetNum':str(int(self.assetNums[x])),
                'assetName':self.assetNames[x],
                'empId':self.empIds[x],
                'userName':self.userNames[x],
                'ownerDept':self.ownerDepts[x],
                'adminId':self.adminIds[x],
                'tagText':self.tagTexts[x]
                }
            header = {'Content-Type':'application/json'}
            response = requests.post(self.url,data=json.dumps(formdata))
            print(str(self.assetNums[x]) + str(response.text))
         
    
test = RUasset()
test.getAsset()
test.updataAsset()


