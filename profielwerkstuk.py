import execjs
import requests
params={
            'time_interval': '',
            'tag': '',
            'tag_type':'',
            'province': '',
            'lunci':'' ,
            'page': '1',
            'num': '20',
            'unionid': ''
}

r=requests.post('https://vipapi.qimingpian.cn/DataList/productListVip',params=params).json()['encrypt_data']
with open('test.js',mode='r')as f:
    jscode=f.read()
ss=execjs.compile(jscode).call('s',r)
#清除
print(ss)
for i in range(1,20):
    product=ss['list'][i]['product']
    hangye1 = ss['list'][i]['hangye1']
    yewu = ss['list'][i]['yewu']
    province = ss['list'][i]['province']
    time= ss['list'][i]['time']
    with open('profielwerkstuk.txt',mode='a',encoding='utf-8')as f2:
        f2.write('product='+str(product))
        f2.write('hangye='+str(hangye1))
        f2.write('yewu='+str(yewu))
        f2.write('province='+str(province))
        f2.write('time='+str(time))
        f2.write('\n')
