﻿# OUCWIFI

可用于pc自动登录中国海洋大学校园网，其他类似学校也可以用，具体教程在https://www.bilibili.com/read/cv16042718/?spm_id_from=333.1007.0.0

## 先安装依赖

安装python

然后

```shell
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

pip install requests

pip install win10toast 
```



## 得到自己的url

![image-20240403011755497](https://github.com/tt1bt/OUCWIFI/assets/128199547/2799386b-1e5d-4066-aa58-361a86e00fb9)

先在上网登录页按F12

再点击网络，勾选保留日志

然后直接登录
![image-20240403011957326](https://github.com/tt1bt/OUCWIFI/assets/128199547/f06dd78c-7147-4e59-974a-8900ef3caddf)


找到右边第一个

双击打开，复制请求URL

![image-20240403012115723](https://github.com/tt1bt/OUCWIFI/assets/128199547/86ee17ac-30bb-4cf2-b3a5-bbbf494c215b)

替换sign_parameter中的参数
![image-20240403012244021](https://github.com/tt1bt/OUCWIFI/assets/128199547/950082e3-fe38-49f6-a282-cabbdac0c060)

然后写个bat放在C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup

开机自运行就行


![image-20240403012406481](https://github.com/tt1bt/OUCWIFI/assets/128199547/149f5276-6fb5-4a56-aab1-a3b88b9c7eb3)

