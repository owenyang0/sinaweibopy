# -*- coding: cp936 -*-
from weibo import APIClient
from datetime import datetime
import urllib
import json
import webbrowser

APP_KEY = '1673559992'
APP_SECRET = '71ac7ba608fcb5314bd3413aaed3f5e1'
CALLBACK_URL = None#'127.0.0.1'
SOME_CODE = None
UID_C = None #用户ID
text_towrite = '' #将获取到的微博写入文本

ACCESS_TOKEN = '2.00zlRX5CG6FQpB56bc127b5d8bSnFE'
TEXT_TO = None
PIC_TO = None
weibo_text = ''
pic_path = ''

class WeiboControl(object):
    
    def __init__(self, weibo_text, pic_path):
        self.TEXT_TO = weibo_text
        self.PIC_TO = pic_path
    
        self.client = APIClient(APP_KEY, APP_SECRET, CALLBACK_URL)
    
        access_token =  ACCESS_TOKEN #r.access_token # access token，e.g., abc123xyz456
        expires_in = 3600 #r.expires_in      # token expires in
        self.client.set_access_token(access_token, expires_in)

    #print json.dumps(client.statuses.user_timeline.get(), ensure_ascii=False)
    def sendTo(str):
        return json.dumps(str,ensure_ascii=False)


    def getUserInfo():
        global UID_C
        UID_C = client.account.get_uid.get().get('uid')
        user_info = client.users.show.get(uid=UID_C)
        print '用户ID：'+str(UID_C)
        print u'昵称：'+user_info.get('screen_name')+u'｜来自：'+user_info.get('location')
        
    def updateText(self, object):
        
         #raw_input('微博文字：').decode('gbk')
        #self.PIC_TO = pic_path #raw_input('图片地址：')

        if self.TEXT_TO == '':
            return '无微博需要发送，请检查文字框！'
            
        elif self.PIC_TO == '':
            send_text = self.client.statuses.update.post(status=self.TEXT_TO)
        else:
            pic_f = open(self.PIC_TO,'rb')
            send_text = self.client.statuses.upload.post(status=self.TEXT_TO,pic=pic_f)
            pic_f.close()
        return u'微博发送成功，发送时间：'+send_text.get('created_at')
        
    def getPic(url, pic_name):
        """获取微博图片，将以微博创建的时间保存"""
        urllib.urlretrieve(url,'images\%s.jpg' % pic_name)

    def getNewWeibo(ui,coun_t):
        def strTimeToInt(str):
            time_utc = str.replace('+0800 ','')
            print time_utc
            d_tmp = datetime.strptime(time_utc,'%a %b %d %H:%M:%S %Y')
            dt = d_tmp.strftime('%Y%m%d%H%M')
            return dt
            
        weibo_text = client.statuses.user_timeline.get(trim_uesr=1, uid=ui,count=coun_t)
        #print sendTo(weibo_text)
        statuses = weibo_text['statuses']
        global text_towrite
        for item in statuses:
            create_time = item.get(u"created_at").encode('gbk')
            pic_url = item.get(u"pic_urls")
            if pic_url != None:
                if len(pic_url) == 1:
                    pic_url_f = pic_url[0].get('thumbnail_pic').replace('thumbnail','large')
                    pic_name = strTimeToInt(create_time)
                    getPic(pic_url_f,pic_name)
                    print '正在下载 '+create_time+' 的图片'
                else:
                    for i in range(len(pic_url)):
                        pic_url_f = pic_url[i].get('thumbnail_pic').replace('thumbnail','large')
                        pic_name = strTimeToInt(create_time)+'_%s'%(i+1)
                        getPic(pic_url_f,pic_name)
                        print '正在下载 '+create_time+' 的图片'
            text_towrite = text_towrite + item.get('text')+'\n'+create_time+'\n---------------------------------------------------\n\n'
        print text_towrite

    def writeText(str):
        strPath = 'weibo.txt'
        str_f = open(strPath,'w')
        str_f.write(str)
        str_f.close()

    def decideToGo():
        decide = raw_input('请选择操作：F 发微博｜G 获取微博\n命令：')
        if decide.lower() == 'f':
            updateText()
        elif decide.lower() == 'g':
            getNewWeibo(UID_C,5)
            writeText(text_towrite.encode('utf8'))
        else:
            print '输入有误，请重新输入！'
            

if __name__ == '__main__':
    #getUserInfo()
    print '-------------------------------'
    #decideToGo()    

    #writeText(text_towrite.encode('utf8'))
    #updateText()
    #a=raw_input('按任意键返回！')
