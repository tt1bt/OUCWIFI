# OUCWIFI

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

![image-20240403011755497](C:\Users\79913\AppData\Roaming\Typora\typora-user-images\image-20240403011755497.png)

先在上网登录页按F12

再点击网络，勾选保留日志

然后直接登录

![image-20240403011957326](C:\Users\79913\AppData\Roaming\Typora\typora-user-images\image-20240403011957326.png)

找到右边第一个

双击打开，复制请求URL

![image-20240403012115723](C:\Users\79913\AppData\Roaming\Typora\typora-user-images\image-20240403012115723.png)

替换sign_parameter中的参数

![image-20240403012244021](C:\Users\79913\AppData\Roaming\Typora\typora-user-images\image-20240403012244021.png)

然后写个bat放在C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup

开机自运行就行

![image-20240403012406481](C:\Users\79913\AppData\Roaming\Typora\typora-user-images\image-20240403012406481.png)

