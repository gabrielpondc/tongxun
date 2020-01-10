import json
import urllib.request, urllib.parse, urllib.error
import ssl
import os
print("------------------------------查询手机运营商------------------------------\n")
s= input("请输入查询手机号码：")
print("-------------------------------搜索中···-------------------------------\n")
try:
    shuju= "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel="+s+"&_ksTS=1578624022274_222&callback=result"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # use urllib to achieve the web data (json)
    url=shuju
    data = urllib.request.urlopen(url, context=ctx).read()

    newdata=data.decode("GBK")
    c = json.dumps(newdata)
    s1 = json.loads(str(c))
    try:
        print("\n")
        print("手机号码:"+s)
        result = s1[42]+s1[43]+s1[46]+s1[47]
        print("所属省份:"+result.replace("ce", " "))
        result2 = s1[60]+s1[61]+s1[62]+s1[63]+s1[64]+s1[65]+s1[66]+s1[67]
        print("通讯服务提供商（ISP):"+result2.replace("',", " ").replace("me:'", " "))
    except IndexError:
        print("手机号码格式有误，请重新输入")
except urllib.error.URLError:
    print("\n")
    print("通讯异常请检查网络连接以及接口")
print("------------------------------CopyRight©GuJiaKai--------------------------\n")
os.system('pause')