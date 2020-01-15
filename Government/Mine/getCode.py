import requests
from lxml import etree

class getCode():
    def Code(self,choise):
        url = "https://zwfw.guizhou.gov.cn/myfw.do?ctype=1&code=0&status=0&areacode=520000"
        headers = {
            'Host': 'zwfw.guizhou.gov.cn',
            'Origin': 'https://zwfw.guizhou.gov.cn',
            'Referer': 'https://zwfw.guizhou.gov.cn/myfw.do?ctype=1&code=0&status=0&areacode=520000',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        r = requests.post(url=url, data="",headers=headers,verify=False)
        r.raise_for_status()
        text = etree.HTML(r.text)
        code = {}
        # 按主题
        if choise == 1:
            item_zt_code = text.xpath("//div[@class ='layui-col-xs2 zt-item']/@code")
            item_zt_codename = text.xpath("//div[@class ='layui-col-xs2 zt-item']//p/text()")
            item_zt_codename = Removespace(item_zt_codename)
            code = item_zt_code
        # 按部门
        elif choise == 2:
            ocode = text.xpath("//div[@class ='bmfw-item bmfont']/@ocode")
            orgcode = text.xpath("//div[@class ='bmfw-item bmfont']/@orgcode")
            ocodename = text.xpath("//div[@class ='bmfw-item bmfont']/@title")
            code = ocode
        # 按行业
        elif choise == 3:
            hycode = text.xpath("//div[starts-with(@class,'hyfw-item')]/@hycode")
            hycodename = text.xpath("//div[starts-with(@class,'hyfw-item')]/text()")
            code = hycode
        return code
        pass

def Removespace(text):
    for i in range(0, len(text)):
        text[i] = text[i].replace('\n', '')
        text[i] = text[i].replace('\t', '')
        text[i] = text[i].replace(' ', '')
        text[i] = text[i].replace('\u3000', '')
    return text







