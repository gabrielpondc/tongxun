import json
import urllib.request, urllib.parse, urllib.error
import ssl
import os
import subprocess
import socket
import re

print("TIP：请确认主机信息以防止隐私盗取")
#获取本机ipv6
child=subprocess.Popen("ipconfig", shell=True, stdout = subprocess.PIPE)
out=child.communicate();#保存ipconfig中的所有信息
ipv6_pattern='(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})'
m=re.findall(ipv6_pattern,str(out))
address=m[1][0]
#获取本机电脑名
myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ipv4
myaddr =socket.gethostbyname(myname)

print("查询主机名称："+myname)
print( "查询主机本地IPv4地址："+myaddr)
print( "查询主机本地IPv6地址："+address)
print("------------------------------查询手机运营商------------------------------")
s= input("请输入查询手机号码：")
print("-------------------------------搜索中···-------------------------------")
try:
    #使用API调用手机查询数据库
    shuju= "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel="+s+"&_ksTS=1578624022274_222&callback=result"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # 使用urllib进行网页数据遍历 (json)
    url=shuju
    data = urllib.request.urlopen(url, context=ctx).read()
    newdata=data.decode("GBK")
    c = json.dumps(newdata)
    s1 = json.loads(str(c))
    try:
        print("\n")
        print("手机号码:"+s)
        result = s1[42]+s1[43]+s1[46]+s1[47]
        print("所属省份:"+result.replace("ce", "").replace("\n", ""))
        result2 = s1[60]+s1[61]+s1[62]+s1[63]+s1[64]+s1[65]+s1[66]+s1[67]
        print("通讯服务提供商（ISP):"+result2.replace("',", " ").replace("me:'", " ").replace("\n", ""))
    except IndexError:
        print("手机号码格式有误，请重新输入")
except urllib.error.URLError:
    print("\n")
    print("通讯异常请检查网络连接以及接口")
print("------------------------------CopyRight©GuJiaKai--------------------------\n")
os.system('pause')