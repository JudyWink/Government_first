from Mine.dataDo import OpOracle

class m_map():

    # def insert(self,item):
    #     data = OpOracle()
    #     sql = "INSERT INTO PERSONAL_AFFAIRS (sxtitle,Event_coding,Power_source,Matter_type,Power_sector,Work_type,characters,legal_time,Promise_time,Permitted_quantity,Processing_window,Processing_time,Online_application,attendance_times,Network_depth,Handling_form,Joint_agency,Online_payment,Wisdom_approval,Same_city,AgencyOrnot,Handle_nearby,Credit_punishment,Intermediary_services,data_sharing,Approval_result_sharing,Convenient_handling,Approval_fee,Handling_publicity,Annual_review,Enquiry,Consultation,Supervision_complaints,Administrative_proceedings) VALUES ('"+item['事项名称']+"','"+item['事项编码']+"','"+item['权力来源']+"','"+item['事项类型']+"','"+item['权力部门']+"','"+item['办件类型']+"','"+item['办理对象']+"','"+item['法定时限']+"','"+item['承诺时限']+"','"+item['许可数量']+"','"+item['办理窗口']+"','"+item['办理时间']+"','"+item['网上申请']+"','"+item['到现场次数']+"','"+item['网办深度']+"','"+item['办理形式']+"','"+item['联办机构']+"','"+item['网上支付']+"','"+item['是否智慧审批事项']+"','"+item['是否同城通办事项']+"','"+item['是否可代办事项']+"','"+item['是否就近办理事项']+"','"+item['是否信用惩诫事项']+"','"+item['是否有中介服务']+"','"+item['数据共享']+"','"+item['审批结果共享']+"','"+item['办理便捷度']+"','"+item['审批收费']+"','"+item['办理公示']+"','"+item['年审或年检']+"','"+item['办理查询']+"','"+item['咨询']+"','"+item['监督投诉']+"','"+item['行政复议行政诉讼']+"')"
    #     data.Ora_IUD_Single(sql)

    def select(self):
        data = OpOracle()
        sql = "SELECT * FROM PERSONAL_AFFAIRS_TEST"
        info = data.Ora_Select(sql)
        return info

    def insert_One(self,column,value):
        data = OpOracle()
        sql = "INSERT INTO PERSONAL_AFFAIRS_TEST ("+column+") VALUES ('"+value+"')"
        data.Ora_IUD_Single(sql)

    def updata_One(self,column,value,title):
        data = OpOracle()
        sql = 'UPDATE PERSONAL_AFFAIRS_TEST SET '+ column+ ' =\' '+value+ '\'WHERE SXTITLE = \'' +title + '\''
        data.Ora_IUD_Single(sql)
