import json
import urllib.request, urllib.parse, urllib.error
import ssl
import os
print("------------------------------查询手机运营商------------------------------")
s= input("请输入查询手机号码：")
print("-------------------------------搜索中···-------------------------------")
try:
    #使用API调用手机查询数据库
    shuju= "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel="+s+"&_ksTS=1578624022274_222&callback=result"
    shuju2="http://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={"+s+"}&resource_id=6004&ie=utf8&oe=utf8&format=json"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # 使用urllib进行网页数据遍历 (json)
    url=shuju
    data = urllib.request.urlopen(url, context=ctx).read()
    url=shuju2
    data2 = urllib.request.urlopen(url, context=ctx).read()
    shi=data2.decode("UTF-8")
    newdata=data.decode("GBK")
    b=json.dumps(shi)
    c = json.dumps(newdata)
    s1 = json.loads(str(c))
    s2=json.loads(str(b))
    try:
        print("\n")
        print("手机号码:" + s)
        result = s1[42] + s1[43]+s1[44] + s1[46] + s1[47]+s1[48]
        print("所属省份:" + result.replace("ce", "").replace("\n", "").replace("'","").replace(",",""))
        result3=s2[132]+s2[133]+s2[134]+s2[135]
        print("所属市辖:" + result3.replace("\",", "").replace("\"",""))
        result2 = s1[60] + s1[61] + s1[62] + s1[63] + s1[64] + s1[65] + s1[66] + s1[67]
        print("通讯服务提供商（ISP):" + result2.replace("',", " ").replace("me:'", " ").replace("\n", "").replace("'",""))



    except IndexError:
        print("手机号码格式有误，请重新输入")
        os.system('pause')
except urllib.error.URLError:
    print("\n")
    print("通讯异常请检查网络连接以及接口")
    os.system('pause')
print("------------------------------CopyRight©GuJiaKai--------------------------\n")
os.system('pause')