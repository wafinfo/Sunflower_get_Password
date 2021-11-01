<h1 align="center" >Sunflower_get_Password</h1>

<h3 align="center" >一款针对向日葵的识别码和验证码提取工具</h3>




##  👮🏻‍♀️ 免责声明

由于传播、利用Sunflower_get_Password工具提供的功能而造成的**任何直接或者间接的后果及损失**，均由使用者本人负责，本人**不为此承担任何责任**。


##  安装环境

1. 本工具使用Python3语言开发

   ```bash
	pip3 install unicorn
   ```


##  使用流程介绍

~~第一步：读取向日葵配置文件路径，分别提取config.ini参数里面encry_pwd(本机验证码)。~~

~~fastcode(本机识别码)[注意faskcode值第一个英文字母不要只需要后面数字即可]的值为明文保存所以不需要解密~~

~~第二步：把ini参数里面encry_pwd值复制出来本机直接运行SunDecrypt.py输入需要解密encry_pwd值即可输出解密后的值。~~

或者直接通过运行[AutoGetPassword.py](./AutoGetPassword.py)来获取解密后的数据

### AutoGetPassword通过注册表获取向日葵安装地址：
1. 相较低版本：尝试读取config.ini配置文件中的数据</br>
2. 相较高版本：尝试通过读取注册表获取数据</br>
3. 解密并未改动</br>


向日葵默认配置文件路径:

安装版：C:\Program Files\Oray\SunLogin\SunloginClient\config.ini

便携版(绿色版)：C:\ProgramData\Oray\SunloginClient\config.ini

![1.png](/1.png)
![2.png](/2.png)

## 👑 更新记录
- v2.1 2021/11/1

感谢kid提醒，目前最新版密码已经不在配置文件中但是可以通过注册表进行查询,目前解密脚本仍可以用

   ```bash
reg query HKEY_USERS\.DEFAULT\Software\Oray\SunLogin\SunloginClient\SunloginInfo

reg query HKEY_USERS\.DEFAULT\Software\Oray\SunLogin\SunloginClient\SunloginGreenInfo
   ```

![4.png](/4.png)


- v2.0 2021/03/17

更新了用户在登录状态下密钥不对导致无法解密。

如果用户登录了会在本地配置文件config.ini中生成一个sunlogincode把复制出来(没有直接回车跳过)。

![3.png](/3.png)
