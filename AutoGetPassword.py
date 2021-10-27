import winreg
from SunDecrypt import *
import os


class AutoGetSunLoginPath:

    def __new__(cls, *args, **kwargs):
        reg_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Oray SunLogin RemoteClient"

        try:
            client_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
            path, _ = winreg.QueryValueEx(client_key, "InstallLocation")
            path = os.path.join(path, "config.ini")
            winreg.CloseKey(client_key)
        except FileNotFoundError:
            path = r"C:\ProgramData\Oray\SunloginClient\config.ini"
            if not os.path.exists(path):
                path = None

        return path


class AutoGetSunLoginAllInfo:

    def __new__(cls, *args, **kwargs):
        reg_path = r".DEFAULT\Software\Oray\SunLogin\SunloginClient\SunloginInfo"
        key = None
        try:
            key = winreg.OpenKey(winreg.HKEY_USERS, reg_path)
        except FileNotFoundError:
            exit("Perhaps the current version is no longer available for this program")
        encry_pwd, _ = winreg.QueryValueEx(key, "base_encry_pwd")
        fastcode, _ = winreg.QueryValueEx(key, "base_fastcode")

        try:
            sunlogincode, _ = winreg.QueryValueEx(key, "base_sunlogincode")
        except FileNotFoundError:
            sunlogincode = ""
        winreg.CloseKey(key)

        return encry_pwd, fastcode, sunlogincode


def get_value(key: str, info_list: list):
    _temp: tuple = tuple(filter(lambda x: key in x, info_list))
    if _temp.__len__() == 0:
        return ""
    return _temp[0].split(key)[1][:-1]


def read_config_and_get_value(config_path: str):
    with open(os.path.join(config_path), "r", encoding='utf-8') as f:
        init_info = f.readlines()

    return get_value("encry_pwd=", init_info), get_value("fastcode=", init_info), get_value("sunlogincode=", init_info)


if __name__ == '__main__':
    # If the program cannot get the address of the sunflower, please fill in
    sunlogin_path = None # such as：C:\ProgramData\Oray\SunloginClient\config.ini
    # Under normal circumstances, the program can obtain the address through the registry

    sunlogin_path = AutoGetSunLoginPath() if sunlogin_path is None else sunlogin_path

    assert sunlogin_path is not None, "Can't seem to find the sunflower on your computer"

    encry_pwd, fastcode, sunlogincode = read_config_and_get_value(sunlogin_path)

    if encry_pwd == '':
        encry_pwd, fastcode, sunlogincode = AutoGetSunLoginAllInfo()

    print("向日葵\n识别码 ", fastcode[1:])
    print("验证码 ", Decrypt(base64.b64decode(encry_pwd), Init(KeyBlock.new_block(sunlogincode)).start()).start().decode())

