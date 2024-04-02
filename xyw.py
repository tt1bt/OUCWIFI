from win10toast import ToastNotifier
import requests
import os

#以下5个变量，需要根据自己的情况进行修改，
#与MacroDroid中的几乎保持一致,
#仅对中文作修改，其他的字符（特别是前后的单引号）均不要修改！
login_IP = 'https://xha.ouc.edu.cn/a79.htm'
not_sign_in_title = '上网登录页'
result_return = 'result":0'
sign_parameter = 'https://xha.ouc.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=22020007038&user_password=20040331lzl&wlan_user_ip=0.0.0.0&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1&terminal_type=1&lang=zh-cn&v=8622&lang=zh'
signed_in_title = '用户信息页'

#以下4个变量，可根据自己的需要，决定是否修改
already_icon = None
success_icon = None
false_icon = None
unknown_icon = None

try:
    r = requests.get(login_IP,
                    timeout = 1)
    req = r.text
except:
    req = 'False'

if signed_in_title in req:
    ToastNotifier().show_toast(title = "该设备已经登录",
               msg = "校园网状态",
               icon_path = already_icon,
               duration = 5,
               threaded = False)
    os._exit(0)

elif not_sign_in_title in req:
    r = requests.get(sign_parameter, timeout=1)
    req = r.text
    if result_return in req:
        ToastNotifier().show_toast(title = "登录成功",
               msg = "校园网状态",
               icon_path = success_icon,
               duration = 5,
               threaded = False)
    else:
        ToastNotifier().show_toast(title = "登录失败",
               msg = "校园网状态",
               icon_path = false_icon,
               duration = 5,
               threaded = False)

    os._exit(0)

else:
    ToastNotifier().show_toast(title = "未连接到校园网",
               msg = "校园网状态",
               icon_path = unknown_icon,
               duration = 5,
               threaded = False)
    os._exit(0)

