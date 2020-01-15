import requests
import json
from Mine.getCode import getCode

class getBSurl():
    def BSurl(self):
        first_urls = []
        print("1.按主题；2.按部门；3.按行业")
        choise = int(input("请选择模块（数字）:"))
        if choise == 1:
            text = "主题"
        elif choise == 2:
            text = "部门"
        elif choise == 3:
            text = "行业"
        print("......正在按 \033[0;30;44m",text,"\033[0m 爬取个人办事指南......")
        code = getCode().Code(choise)
        length = len(code)
        for i in range(0,length):
            urls = []
            if choise == 1:
                data = {
                    'area_code': "520000",
                    'PageSize': "1500",
                    'page': "1",
                    'org_code': "",
                    'item_zt_code': code[i],
                    'hycode': "",
                    'isqueryxz': "1",
                }
            elif choise == 2:
                data = {
                    'area_code': "520000",
                    'PageSize': "1500",
                    'page': "1",
                    'org_code': code[i],
                    'item_zt_code': "",
                    'hycode': "",
                    'isqueryxz': "1",
                }
            elif choise == 3:
                data = {
                    'area_code': "520000",
                    'PageSize': "1500",
                    'page': "1",
                    'org_code': "",
                    'item_zt_code': "",
                    'hycode': code[i],
                    'isqueryxz': "1",
                }
            else:print("选择有误")

            url = "https://zwfw.guizhou.gov.cn/ytbase/system/default.aspx?yt_out_lay=1&YtAction=BaseIEx&ClassName=ZnzwSvr.page.QltAction&YtOpt=GetQltFolderList"
            headers = {
                'Host': 'zwfw.guizhou.gov.cn',
                'Origin': 'https://zwfw.guizhou.gov.cn',
                'Referer': 'https://zwfw.guizhou.gov.cn/myfw.do?ctype=1&code=0&status=0&areacode=520000',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
            }
            requests.packages.urllib3.disable_warnings()
            r = requests.post(url=url, data=data, headers=headers, verify=False)




            jsondata = json.loads(r.text)
            if ('data' in jsondata):
                data = json.loads(r.text)['data']
                if('Data' in data):
                    Datas = json.loads(r.text)['data']['Data']
                    for a in range(len(Datas)):
                        if('QltList' in Datas[a]):
                            QltLists = json.loads(r.text)['data']['Data'][a]['QltList']
                            if type(QltLists) is list:
                                for b in range(0,len(QltLists)):
                                    if('ITEM_CODE' in QltLists[b]):
                                        ITEM_CODE = json.loads(r.text)['data']['Data'][a]['QltList'][b]['ITEM_CODE']
                                        Org_code = json.loads(r.text)['data']['Data'][a]['QltList'][b]['Org_code']
                                        bszn_url = "https://zwfw.guizhou.gov.cn/bsznindex.do?otheritemcode=" + ITEM_CODE + "&orgcode=" + Org_code + "&areacode=520100"
                                        first_urls.append(bszn_url)
        return first_urls


