<h1 align="center" >Sunflower_get_Password</h1>

<h3 align="center" >一款针对向日葵的识别码和验证码提取工具</h3>




##  ♀️ 免责声明

由于传播、利用Sunflower_get_Password工具提供的功能而造成的**任何直接或者间接的后果及损失**，均由使用者本人负责，本人**不为此承担任何责任**。


##  安装环境

1. 本工具使用Python3语言开发

   ```bash
	pip3 install unicorn
   ```


##  使用流程介绍

第一步：读取向日葵配置文件路径，分别提取config.ini参数里面encry_pwd(本机验证码)，fastcode(本机识别码)[注意faskcode值第一个英文字母不要只需要后面数字即可]的值。

第二步：把ini参数里面encry_pwd值复制出来本机直接运行SunDecrypt.py输入需要解密encry_pwd值即可输出解密后的值。


向日葵默认配置文件路径:

安装版：C:\Program Files\Oray\SunLogin\SunloginClient\config.ini

便携版(绿色版)：C:\ProgramData\Oray\SunloginClient\config.ini

![1.png](/1.png)
![2.png](/2.png)
