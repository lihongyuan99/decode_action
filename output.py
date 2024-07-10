#2024-07-10 13:55:40
'''
cron: 30 11 * * *
new Env('�����Ķ��齱');
���ⷴ����ϵ����ϵ��https://t.me/bwersgt
Ⱥ�飺https://t.me/yangmaoxz
Ƶ����ַ��https://t.me/ymxzpd
ʹ�÷�����
1.��app������Ķ�����
2.ץ��https://xmt.taizhou.com.cn/prod-api/user-read/app/login�ӿڵ�id,sessionId,deviceId����
3.�����ļ����
���˻���export wcread="[ {'name': 'xxx','aid': 'id', 'sid': 'sessionId', 'deviceId':'deviceId'}]"
���˻���export wcread="[
{'name': 'xxx','aid': 'xxxx', 'sid': 'xxxx', 'deviceId':'xxxx'},
{'name': 'xxx','aid': 'xxxx', 'sid': 'xxxx', 'deviceId':'xxxx'}
]"
����˵����
bz:��ע��������д
aid:2�����е�id����
sid:2�����е�sessionId����
deviceId:2�����е�deviceId����
'''
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsAW=None
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv=print
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWA=exit
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAvs=Exception
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAvW=True
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAsv=str
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAsW=int
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAWv=False
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAWs=id
import requests
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvsW=requests.get
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvsA=requests.session
import time
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvWs=time.strftime
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvAW=time.time
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvAs=time.sleep
import random
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvWA=random.randint
import hashlib
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsvA=hashlib.md5
import os
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsvW=os.getenv
import json
VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsAv=json.loads
def VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWQs(text):
 m=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsvA(text.encode(encoding='utf-8'))
 return m.hexdigest()
def VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWQA():
 VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsA=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsvW('wcread')
 if VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsA==VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsAW:
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('env is none')
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWA(0)
 try:
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsA=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsAv(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsA.replace("'",'"'))
  return VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsA
 except VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAvs as e:
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('err:',e)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('your env is:',VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsA)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWA(0)
class VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAWs:
 def __init__(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW,cg):
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.deviceId=cg['deviceId']
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.aid=cg["aid"]
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sid=cg["sid"]
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.name=cg['name']
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvsA()
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec.headers={'Host':'xmt.taizhou.com.cn','User-Agent':'Mozilla/5.0 (Linux; Android 9; LIO-AN00 Build/LIO-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36;xsb_wangchao;xsb_wangchao;5.3.2;native_app','X-Requested-With':'com.shangc.tiennews.taizhou','Referer':'https://srv-app.taizhou.com.cn/luckdraw/'}
 def VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWsQ(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW):
  u='https://xmt.taizhou.com.cn/prod-api/user-read/app/login?id='+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.aid+'&sessionId='+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sid+'&deviceId='+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.deviceId
  r=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec.get(u)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv(r.text)
  rj=r.json()
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQAs=rj.get('data')
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvAs(1)
  if VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQAs:
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQAW=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQAs.get('needYz')
   if VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQAW==VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAvW:
    VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQWs=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQAs.get('yzm')
    ts=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAsv(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAsW(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvAW()*1000))
    ms='&&TlGFQAOlCIVxnKopQnW&&'+ts+'&&'+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQWs
    VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQWA=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWQs(ms)
    uu=f'https://xmt.taizhou.com.cn/prod-api/user-read/yzmyz?signature='+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQWA+'&timestamp='+ts+'&yzm='+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQWs
    rr=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec.get(uu)
    VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv(rr.text)
    if '���ܴ���' in rr.text:
     try:
      import notify
      VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('���ܴ���')
      notify.send('�����������','���ܴ����쳣')
     except VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAvs as e:
      VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv(e)
      VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('����ʧ��')
     return VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAWv
  else:
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('��¼ʧ�ܣ��˺��쳣')
   return VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAWv
 def VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWsA(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW):
  u1='https://xmt.taizhou.com.cn/prod-api/user-read/list/'+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAsv(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvWs("%Y%m%d"))
  r1=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec.get(u1)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv(r1.text)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsQA=r1.json().get('data').get('articleIsReadList')
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvAs(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvWA(2,4))
  for i in VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsQA:
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('-'*50)
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAWs=i.get('id')
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsQW=i.get('title')
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsAQ=i.get('isRead')
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('�Ķ�����',VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsQW)
   if VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsAQ==VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAvW:
    VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv(f'���£�'+'title'+'�Ѿ��Ķ���')
    continue
   ts=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAsv(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAsW(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvAW()*1000))
   ms='&&'+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAsv(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAWs)+'&&TlGFQAOlCIVxnKopQnW&&'+ts
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQWA=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWQs(ms)
   u2='https://xmt.taizhou.com.cn/prod-api/already-read/article?articid='+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAsv(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAWs)+'&timestamp='+ts+'&signature='+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQWA
   r2=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec.get(u2)
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('�Ķ�������',r2.text)
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvAs(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvWA(2,4))
 def VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWAQ(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW):
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec.headers.update({'Referer':'https://srv-app.taizhou.com.cn/luckdraw/','Host':'srv-app.taizhou.com.cn'})
  u1='https://srv-app.taizhou.com.cn/tzrb/awardUpgrade/list?activityId=67'
  r1=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvsW(u1)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsAW=r1.json()
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsWQ=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsAW.get('data')
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsWA={}
  for i in VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsWQ:
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsWA.update({i.get('id'):i.get('title')})
  u2='https://srv-app.taizhou.com.cn/tzrb/user/loginWC?accountId='+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.aid+'&sessionId='+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sid
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec.get(u2)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvAs(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQvWA(2,4))
  u3='https://srv-app.taizhou.com.cn/tzrb/userAwardRecordUpgrade/saveUpdate'
  p='activityId=67&sessionId=undefined&sig=undefined&token=undefined'
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec.headers.update({'Content-type':'application/x-www-form-urlencoded'})
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQs=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.sec.post(u3,data=p)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQW=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQs.json()
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQW)
  if VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQW.get('code')==200:
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('�齱���:'+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsWA.get(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQW.get("data")))
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAsQ='�齱���:'+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvsWA.get(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQW.get("data"))
  elif VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQW.get('code')==500:
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('��ȡ���˽�Ʒ',VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQW.get('message'))
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAsQ='��ȡ���˽�Ʒ:'+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAQW.get("message")
  else:
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('δ֪���')
   VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAsQ='δ֪���'
  return VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.name+':'+VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAsQ+'\n'
 def VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWAs(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW):
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWsQ()
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWsA()
  return VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvQsW.VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWAQ()
if __name__=='__main__':
 VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAsW=''
 VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('''
If you have any questions, please contact me:��https://t.me/bwersgt
Telegram group��https://t.me/yangmaoxz
Telegram Address��https://t.me/ymxzpd
    ''' )
 for VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAWQ in VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWQA():
  sa=VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAWs(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAWQ)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAsW+=sa.VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvWAs()
 VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv(VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAsW)
 try:
  import notify
  notify.send('�����齱����',VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLvAsW)
 except VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQAvs as e:
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv(e)
  VMjagNSpbJdqRcDwFzxEokfKXOHnitIluhyCGBUYmerPTLQsWv('����ʧ��')
