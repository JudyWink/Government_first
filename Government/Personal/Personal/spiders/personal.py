import json
import os
import scrapy
from Mine.Map import m_map
from Mine.dataDo import OpOracle
from Mine.postdo import getBSurl
import urllib3


class PersonalSpider(scrapy.Spider):
    urllib3.disable_warnings()
    urllist = getBSurl().BSurl()
    name = 'personal'
    start_urls = urllist

    def parse(self, response):
        response.body.decode('utf8')
        map = m_map()
        item = {}

        # 事项名称
        sxtitle = response.xpath("//td[starts-with(text(),'事项名称')]/following-sibling::td[1]//text()").extract()
        sxtitle = Removespace(sxtitle)
        map.insert_One('sxtitle',sxtitle)
        item.update({'事项名称':sxtitle})

        # 网址
        thisurl = response.url
        map.updata_One('url', thisurl, sxtitle)
        item.update({'网址': thisurl})

        # 服务类型
        service_type = response.xpath("//td[starts-with(text(),'服务类型')]/following-sibling::td[1]//text()").extract()
        service_type = Removespace(service_type)
        if service_type != "":
            map.updata_One('service_type', service_type, sxtitle)
            item.update({'服务类型': service_type})

        # 事项编码
        Event_coding = response.xpath("//td[starts-with(text(),'事项编码')]/following-sibling::td[1]//text()").extract()
        Event_coding = Removespace(Event_coding)
        if Event_coding != "":
            map.updata_One('Event_coding' , Event_coding , sxtitle)
            item.update({'事项编码': Event_coding})

        # 权力来源
        Power_source = response.xpath("//td[starts-with(text(),'权力来源')]/following-sibling::td[1]//text()").extract()
        Power_source = Removespace(Power_source)
        if Power_source != "":
            map.updata_One('Power_source', Power_source, sxtitle)
            item.update({'权力来源': Power_source})

        # 事项类型
        Matter_type = response.xpath("//td[starts-with(text(),'事项类型')]/following-sibling::td[1]//text()").extract()
        Matter_type = Removespace(Matter_type)
        if Matter_type != "":
            map.updata_One('Matter_type', Matter_type, sxtitle)
            item.update({'事项类型': Matter_type})

        # 权力部门
        Power_sector = response.xpath("//td[starts-with(text(),'权力部门')]/following-sibling::td[1]//text()").extract()
        Power_sector = Removespace(Power_sector)
        if Power_sector != "":
            map.updata_One('Power_sector', Power_sector, sxtitle)
            item.update({'权力部门': Power_sector})

        # 服务部门
        Service_sector= response.xpath("//td[starts-with(text(),'服务部门')]/following-sibling::td[1]//text()").extract()
        Service_sector = Removespace(Service_sector)
        if Service_sector != "":
            map.updata_One('Service_sector', Service_sector, sxtitle)
            item.update({'服务部门': Service_sector})

        # 办理条件
        Handling_conditions = response.xpath("//td[starts-with(text(),'办理条件')]/following-sibling::td[1]//text()").extract()
        Handling_conditions = Removespace(Handling_conditions)
        if Handling_conditions != "":
            map.updata_One('Service_sector', Handling_conditions, sxtitle)
            item.update({'办理条件': Handling_conditions})

        # 办理时限
        dotime = response.xpath("//td[starts-with(text(),'办理时限')]/following-sibling::td[1]//text()").extract()
        dotime = Removespace(dotime)
        if dotime != "":
            map.updata_One('dotime', dotime, sxtitle)
            item.update({'办理时限': dotime})

        # 办件类型
        Work_type = response.xpath("//td[starts-with(text(),'办件类型')]/following-sibling::td[1]//text()").extract()
        Work_type = Removespace(Work_type)
        if Work_type != "":
            map.updata_One('Work_type', Work_type, sxtitle)
            item.update({'办件类型': Work_type})

        # 办理对象
        Work_characters = response.xpath("//td[starts-with(text(),'办理对象')]/following-sibling::td[1]/@service_obectj").extract()
        if len(Work_characters) > 1:
            Work_characters = Work_characters[1].split(',')
            Work_characters = serviceObject(Work_characters)
            map.updata_One('Work_characters', Work_characters, sxtitle)
            item.update({'办理对象:': Work_characters})
        elif ',' in Work_characters:
            Work_characters = serviceObject(Work_characters)
            map.updata_One('Work_characters', Work_characters, sxtitle)
            item.update({'办理对象:': Work_characters})
        else:
            Work_characters = response.xpath("//td[starts-with(text(),'办理对象')]/following-sibling::td[1]//text()").extract()
            if len(Work_characters)>1:
                Work_characters = Work_characters[1]
            else:
                Work_characters = Removespace(Work_characters)
            if Work_characters != "":
                map.updata_One('Work_characters', Work_characters, sxtitle)
                item.update({'办理对象': Work_characters})

        # 服务对象
        fwcharacters = response.xpath("//td[starts-with(text(),'服务对象')]/following-sibling::td[1]/@service_obectj").extract()
        if len(fwcharacters) > 1:
            fwcharacters = fwcharacters[1].split(',')
            fwcharacters = serviceObject(fwcharacters)
            map.updata_One('fwcharacters', fwcharacters, sxtitle)
            item.update({'服务对象': fwcharacters})
        elif ',' in fwcharacters:
            fwcharacters = serviceObject(fwcharacters)
            map.updata_One('fwcharacters', fwcharacters, sxtitle)
            item.update({'服务对象': fwcharacters})
        else:
            fwcharacters = response.xpath("//td[starts-with(text(),'服务对象')]/following-sibling::td[1]//text()").extract()
            if len(fwcharacters) > 1:
                fwcharacters = fwcharacters[1]
            else:
                fwcharacters = Removespace(fwcharacters)
            if fwcharacters != "":
                map.updata_One('fwcharacters', fwcharacters, sxtitle)
                item.update({'服务对象': fwcharacters})

        # 检查对象
        Inspection_object = response.xpath("//td[starts-with(text(),'检查对象')]/following-sibling::td[1]/@service_obectj").extract()
        if len(Inspection_object) > 1:
            Inspection_object = Inspection_object[1].split(',')
            Inspection_object = serviceObject(Inspection_object)
            map.updata_One('Inspection_object', Inspection_object, sxtitle)
            item.update({'检查对象': Inspection_object})
        elif ',' in Inspection_object:
            Inspection_object = serviceObject(Inspection_object)
            map.updata_One('Inspection_object', Inspection_object, sxtitle)
            item.update({'检查对象': Inspection_object})
        else:
            Inspection_object = response.xpath("//td[starts-with(text(),'检查对象')]/following-sibling::td[1]//text()").extract()
            if len(Inspection_object) > 1:
                Inspection_object = Inspection_object[1]
            else:
                Inspection_object = Removespace(Inspection_object)
            if Inspection_object != "":
                map.updata_One('Inspection_object', Inspection_object, sxtitle)
                item.update({'检查对象': Inspection_object})

        # 处罚对象
        Punishment_object = response.xpath("//td[starts-with(text(),'处罚对象')]/following-sibling::td[1]/@service_obectj").extract()
        if len(Punishment_object) > 1:
            Punishment_object = Punishment_object[1].split(',')
            Punishment_object = serviceObject(Punishment_object)
            map.updata_One('Punishment_object', Punishment_object, sxtitle)
            item.update({'处罚对象': Punishment_object})
        elif ',' in Punishment_object:
            Punishment_object = serviceObject(Punishment_object)
            map.updata_One('Punishment_object', Punishment_object, sxtitle)
            item.update({'处罚对象': Punishment_object})
        else:
            Punishment_object = response.xpath("//td[starts-with(text(),'处罚对象')]/following-sibling::td[1]//text()").extract()
            if len(Punishment_object) > 1:
                Punishment_object = Punishment_object[1]
            else:
                Punishment_object = Removespace(Punishment_object)
            if Punishment_object != "":
                map.updata_One('Punishment_object', Punishment_object, sxtitle)
                item.update({'处罚对象': Punishment_object})

        # 强制对象
        Mandatory_object = response.xpath("//td[starts-with(text(),'强制对象')]/following-sibling::td[1]/@service_obectj").extract()
        if len(Mandatory_object) > 1:
            Mandatory_object = Mandatory_object[1].split(',')
            Mandatory_object = serviceObject(Mandatory_object)
            map.updata_One('Mandatory_object', Mandatory_object, sxtitle)
            item.update({'强制对象': Mandatory_object})
        elif ',' in Mandatory_object:
            Mandatory_object = serviceObject(Mandatory_object)
            map.updata_One('Mandatory_object', Mandatory_object, sxtitle)
            item.update({'强制对象': Mandatory_object})
        else:
            Mandatory_object = response.xpath("//td[starts-with(text(),'强制对象')]/following-sibling::td[1]//text()").extract()
            if len(Mandatory_object) > 1:
                Mandatory_object = Mandatory_object[1]
            else:
                Mandatory_object = Removespace(Mandatory_object)
            if Mandatory_object != "":
                map.updata_One('Mandatory_object', Mandatory_object, sxtitle)
                item.update({'强制对象': Mandatory_object})

        # 法定时限
        legal_time = response.xpath("//td[starts-with(text(),'法定时限')]/following-sibling::td[1]//text()").extract()
        legal_time = Removespace(legal_time)
        if legal_time != "":
            map.updata_One('legal_time', legal_time, sxtitle)
            item.update({'法定时限': legal_time})

        # 承诺时限
        Promise_time = response.xpath("//td[starts-with(text(),'承诺时限')]/following-sibling::td[1]//text()").extract()
        Promise_time = Removespace(Promise_time)
        if Promise_time != "":
            map.updata_One('Promise_time', Promise_time, sxtitle)
            item.update({'承诺时限': Promise_time})

        # 许可数量
        Permitted_quantity = response.xpath("//td[starts-with(text(),'许可数量')]/following-sibling::td[1]//text()").extract()
        Permitted_quantity = Removespace(Permitted_quantity)
        if Permitted_quantity != "":
            map.updata_One('Permitted_quantity', Permitted_quantity, sxtitle)
            item.update({'许可数量': Permitted_quantity})

        # 办理窗口
        Processing_window = response.xpath("//td[starts-with(text(),'办理窗口')]/following-sibling::td[1]//text()").extract()
        Processing_window = Removespace(Processing_window)
        if Processing_window != "":
            map.updata_One('Processing_window', Processing_window, sxtitle)
            item.update({'办理窗口': Processing_window})

        # 办理地点
        doplace = response.xpath("//td[starts-with(text(),'办理地点')]/following-sibling::td[1]//text()").extract()
        doplace = Removespace(doplace)
        if doplace != "":
            map.updata_One('doplace', doplace, sxtitle)
            item.update({'办理地点': doplace})

        # 办理时间
        Processing_time = response.xpath("//td[starts-with(text(),'办理时间')]/following-sibling::td[1]//text()").extract()
        Processing_time = Removespace(Processing_time)
        if Processing_time != "":
            map.updata_One('Processing_time', Processing_time, sxtitle)
            item.update({'办理时间': Processing_time})

        # 咨询电话
        phone = response.xpath("//td[starts-with(text(),'咨询电话')]/following-sibling::td[1]//text()").extract()
        phone = Removespace(phone)
        if phone != "":
            map.updata_One('phone', phone, sxtitle)
            item.update({'咨询电话': phone})


        # 投诉电话
        tsphone = response.xpath("//td[starts-with(text(),'投诉电话')]/following-sibling::td[1]//text()").extract()
        tsphone = Removespace(tsphone)
        if tsphone != "":
            map.updata_One('tsphone', tsphone, sxtitle)
            item.update({'投诉电话': tsphone})


        # 网上申请
        Online_application = response.xpath("//td[starts-with(text(),'网上申请')]/following-sibling::td[1]//text()").extract()
        Online_application = Removespace(Online_application)
        if Online_application != "":
            map.updata_One('Online_application', Online_application, sxtitle)
            item.update({'网上申请': Online_application})

        # 到现场次数
        attendance_times = response.xpath("//td[starts-with(text(),'到现场次数')]/following-sibling::td[1]//text()").extract()
        attendance_times = Removespace(attendance_times)
        if attendance_times != "":
            map.updata_One('attendance_times', attendance_times, sxtitle)
            item.update({'到现场次数': attendance_times})

        # 网办深度
        Network_depth = response.xpath("//td[starts-with(text(),'网办深度')]/following-sibling::td[1]//text()").extract()
        Network_depth = Removespace(Network_depth)
        if Network_depth != "":
            map.updata_One('Network_depth', Network_depth, sxtitle)
            item.update({'网办深度': Network_depth})

        # 办理形式
        Handling_form = response.xpath("//td[starts-with(text(),'办理形式')]/following-sibling::td[1]//text()").extract()
        Handling_form = Removespace(Handling_form)
        if Handling_form != "":
            map.updata_One('Handling_form', Handling_form, sxtitle)
            item.update({'办理形式': Handling_form})

        # 联办机构
        Joint_agency = response.xpath("//td[starts-with(text(),'联办机构')]/following-sibling::td[1]//text()").extract()
        Joint_agency = Removespace(Joint_agency)
        if Joint_agency != "":
            map.updata_One('Joint_agency', Joint_agency, sxtitle)
            item.update({'联办机构': Joint_agency})

        # 网上支付
        Online_payment = response.xpath("//td[starts-with(text(),'网上支付')]/following-sibling::td[1]//text()").extract()
        Online_payment = Removespace(Online_payment)
        if Online_payment != "":
            map.updata_One('Online_payment', Online_payment, sxtitle)
            item.update({'网上支付': Online_payment})

        # 是否智慧审批事项
        Wisdom_approval = response.xpath("//td[starts-with(text(),'是否智慧审批事项')]/following-sibling::td[1]//text()").extract()
        Wisdom_approval = Removespace(Wisdom_approval)
        if Wisdom_approval != "":
            map.updata_One('Wisdom_approval', Wisdom_approval, sxtitle)
            item.update({'是否智慧审批事项': Wisdom_approval})

        # 是否同城通办事项
        Same_city = response.xpath("//td[starts-with(text(),'是否同城通办事项')]/following-sibling::td[1]//text()").extract()
        Same_city = Removespace(Same_city)
        if Same_city != "":
            map.updata_One('Same_city', Same_city, sxtitle)
            item.update({'是否同城通办事项': Same_city})

        # 是否可代办事项
        AgencyOrnot = response.xpath("//td[starts-with(text(),'是否可代办事项')]/following-sibling::td[1]//text()").extract()
        AgencyOrnot = Removespace(AgencyOrnot)
        if AgencyOrnot != "":
            map.updata_One('AgencyOrnot', AgencyOrnot, sxtitle)
            item.update({'是否可代办事项': AgencyOrnot})

        # 是否就近办理事项
        Handle_nearby = response.xpath("//td[starts-with(text(),'是否就近办理事项')]/following-sibling::td[1]//text()").extract()
        Handle_nearby = Removespace(Handle_nearby)
        if Handle_nearby != "":
            map.updata_One('Handle_nearby', Handle_nearby, sxtitle)
            item.update({'是否就近办理事项': Handle_nearby})

        # 是否信用惩诫事项
        Credit_punishment = response.xpath("//td[starts-with(text(),'是否信用惩诫事项')]/following-sibling::td[1]//text()").extract()
        Credit_punishment = Removespace(Credit_punishment)
        if Credit_punishment != "":
            map.updata_One('Credit_punishment', Credit_punishment, sxtitle)
            item.update({'是否信用惩诫事项': Credit_punishment})

        # 是否有中介服务
        Intermediary_services = response.xpath("//td[starts-with(text(),'是否有中介服务')]/following-sibling::td[1]//text()").extract()
        Intermediary_services = Removespace(Intermediary_services)
        if Intermediary_services != "":
            map.updata_One('Intermediary_services', Intermediary_services, sxtitle)
            item.update({'是否有中介服务': Intermediary_services})

        # 数据共享
        data_sharing = response.xpath("//td[starts-with(text(),'数据共享')]/following-sibling::td[1]//text()").extract()
        data_sharing = Removespace(data_sharing)
        if data_sharing != "":
            map.updata_One('data_sharing', data_sharing, sxtitle)
            item.update({'数据共享': data_sharing})

        # 审批结果共享
        Approval_result_sharing = response.xpath("//td[starts-with(text(),'审批结果共享')]/following-sibling::td[1]//text()").extract()
        Approval_result_sharing = Removespace(Approval_result_sharing)
        if Approval_result_sharing != "":
            map.updata_One('Approval_result_sharing', Approval_result_sharing, sxtitle)
            item.update({'审批结果共享': Approval_result_sharing})

        # 办理便捷度
        Convenient_handling = response.xpath("//td[starts-with(text(),'办理便捷度')]/following-sibling::td[1]//text()").extract()
        Convenient_handling = Removespace(Convenient_handling)
        if Convenient_handling != "":
            map.updata_One('Convenient_handling', Convenient_handling, sxtitle)
            item.update({'办理便捷度': Convenient_handling})

        # 是否收费
        Approval_fee = response.xpath("//td[starts-with(text(),'是否收费')]/following-sibling::td[1]//text()").extract()
        Approval_fee = Removespace(Approval_fee)
        if Approval_fee != "":
            map.updata_One('Approval_fee', Approval_fee, sxtitle)
            item.update({'是否收费': Approval_fee})

        # 办理公示
        Handling_publicity = response.xpath("//td[starts-with(text(),'办理公示')]/following-sibling::td[1]//text()").extract()
        Handling_publicity = Removespace(Handling_publicity)
        if Handling_publicity != "":
            map.updata_One('Handling_publicity', Handling_publicity, sxtitle)
            item.update({'办理公示': Handling_publicity})

        # 年审或年检
        Annual_review = response.xpath("//td[starts-with(text(),'年审或年检')]/following-sibling::td[1]//text()").extract()
        Annual_review = Removespace(Annual_review)
        if Annual_review != "":
            map.updata_One('Annual_review', Annual_review, sxtitle)
            item.update({'年审或年检': Annual_review})

        # 办理查询
        Enquiry = response.xpath("//td[starts-with(text(),'办理查询')]/following-sibling::td[1]//text()").extract()
        Enquiry = Removespace(Enquiry)
        if Enquiry != "":
            map.updata_One('Enquiry', Enquiry, sxtitle)
            item.update({'办理查询': Enquiry})

        # 咨询
        Consultation = response.xpath("//td[starts-with(text(),'咨 询')]/following-sibling::td[1]//text()").extract()
        Consultation = Removespace(Consultation)
        if Consultation != "":
            map.updata_One('Consultation', Consultation, sxtitle)
            item.update({'咨询': Consultation})

        # 监督投诉
        Supervision_complaints = response.xpath("//td[starts-with(text(),'监督投诉')]/following-sibling::td[1]//text()").extract()
        Supervision_complaints = Removespace(Supervision_complaints)
        if Supervision_complaints != "":
            map.updata_One('Supervision_complaints', Supervision_complaints, sxtitle)
            item.update({'监督投诉': Supervision_complaints})

        # 行政复议行政诉讼
        Administrative_proceedings = response.xpath("//td[starts-with(text(),'行政复议行政诉讼')]/following-sibling::td[1]//text()").extract()
        Administrative_proceedings = Removespace(Administrative_proceedings)
        if Administrative_proceedings != "":
            map.updata_One('Administrative_proceedings', Administrative_proceedings, sxtitle)
            item.update({'行政复议行政诉讼': Administrative_proceedings})

        # 处罚条件
        Penalty_conditions = response.xpath("//td[starts-with(text(),'处罚条件')]/following-sibling::td[1]//text()").extract()
        Penalty_conditions = Removespace(Penalty_conditions)
        if Penalty_conditions != "":
            map.updata_One('Penalty_conditions', Penalty_conditions, sxtitle)
            item.update({'处罚条件': Penalty_conditions})


        # 处罚种类或方式
        Punishment_type = response.xpath("//td[starts-with(text(),'处罚种类或方式')]/following-sibling::td[1]//text()").extract()
        Punishment_type = Removespace(Punishment_type)
        if Punishment_type != "":
            map.updata_One('Punishment_type', Punishment_type, sxtitle)
            item.update({'处罚种类或方式': Punishment_type})

        # 处罚信息公示
        Punishment_information = response.xpath("//td[starts-with(text(),'处罚信息公示')]/following-sibling::td[1]//text()").extract()
        Punishment_information = Removespace(Punishment_information)
        if Punishment_information != "":
            map.updata_One('Punishment_information', Punishment_information, sxtitle)
            item.update({'处罚信息公示': Punishment_information})

        # 处罚查询
        Penalty_inquiry = response.xpath("//td[starts-with(text(),'处罚查询')]/following-sibling::td[1]//text()").extract()
        Penalty_inquiry = Removespace(Penalty_inquiry)
        if Penalty_inquiry != "":
            map.updata_One('Penalty_inquiry', Penalty_inquiry, sxtitle)
            item.update({'处罚查询': Penalty_inquiry})

        # 检查种类或方式
        Inspect_type = response.xpath("//td[starts-with(text(),'检查种类或方式')]/following-sibling::td[1]//text()").extract()
        Inspect_type = Removespace(Inspect_type)
        if Inspect_type != "":
            map.updata_One('Inspect_type', Inspect_type, sxtitle)
            item.update({'检查种类或方式': Inspect_type})

        # 检查信息公示
        Inspect_infos = response.xpath("//td[starts-with(text(),'检查信息公示')]/following-sibling::td[1]//text()").extract()
        Inspect_infos = Removespace(Inspect_infos)
        if Inspect_infos != "":
            map.updata_One('Inspect_infos', Inspect_infos, sxtitle)
            item.update({'检查信息公示': Inspect_infos})

        # 检查查询
        Inspect_inquiry = response.xpath("//td[starts-with(text(),'检查查询')]/following-sibling::td[1]//text()").extract()
        Inspect_inquiry = Removespace(Inspect_inquiry)
        if Inspect_inquiry != "":
            map.updata_One('Inspect_inquiry', Inspect_inquiry, sxtitle)
            item.update({'检查查询': Inspect_inquiry})

        # 强制种类或方式
        Mandatory_type = response.xpath("//td[starts-with(text(),'强制种类或方式')]/following-sibling::td[1]//text()").extract()
        Mandatory_type = Removespace(Mandatory_type)
        if Mandatory_type != "":
            map.updata_One('Mandatory_type', Mandatory_type, sxtitle)
            item.update({'强制种类或方式': Mandatory_type})

        # 强制信息公示
        Mandatory_infos = response.xpath("//td[starts-with(text(),'强制信息公示')]/following-sibling::td[1]//text()").extract()
        Mandatory_infos = Removespace(Mandatory_infos)
        if Mandatory_infos != "":
            map.updata_One('Mandatory_infos', Mandatory_infos, sxtitle)
            item.update({'检查信息公示': Mandatory_infos})

        # 强制查询
        Mandatory_inquiry = response.xpath("//td[starts-with(text(),'强制查询')]/following-sibling::td[1]//text()").extract()
        Mandatory_inquiry = Removespace(Mandatory_inquiry)
        if Mandatory_inquiry != "":
            map.updata_One('Mandatory_inquiry', Mandatory_inquiry, sxtitle)
            item.update({'强制查询': Mandatory_inquiry})

        print('\033[0;30;44m《',sxtitle,'》\033[0m')

        # 字典转换json格式
        jsondata = json.dumps(item, sort_keys=True, indent=4, separators=(',', ':'),ensure_ascii=False)

        # 关闭数据库连接
        OpOracle().Ora_Cur_Close()
        OpOracle().Ora_db_Close()

        # 生成json文件
        if (not os.path.exists('./办事指南演示/')):
            os.makedirs('./办事指南演示/')
        title = './办事指南演示/' + sxtitle + '.json'
        f = open(title, 'w',encoding='utf-8')
        f.write(jsondata)
        f.close()

        pass


# 服务对象转换
def serviceObject(character):
    for i in range(0, len(character)):
        if (character[i] == "0"):
            character[i] = '公民'
        elif (character[i] == "1"):
            character[i] = '法人'
        elif (character[i] == "2"):
            character[i] = '其他组织'
        else:
            character[i] = '无'
    characters = ",".join(character)
    return characters
    pass


# 去除空格
def Removespace(text):
    for i in range(0, len(text)):
        text[i] = text[i].replace('\n', '')
        text[i] = text[i].replace('\t', '')
        text[i] = text[i].replace(' ', '')
    texts = "".join(text)
    return texts
    pass
