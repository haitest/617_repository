#_*_ coding:utf-8 _*_ 
# coding=utf-8
import os
import json
import hashlib
import base64
import crypto

from Crypto.Cipher import AES

__author__ = 'mayor'

aes_pad = lambda src: src + (16 - len(src) % 16) * chr(16 - len(src) % 16)
aes_unpad = lambda src: src[:-ord(src[-1])]


class InternalSecure(object):
    """
        �ڲ��ӿ�ǩ���ӽ�����
    """

    def __init__(self, secret_key):
        self.b64_key = secret_key

    @staticmethod
    def md5(src):
        m = hashlib.md5()
        m.update(src)
        return m.hexdigest()

    @staticmethod
    def get_b64iv():
        iv = os.urandom(16)
        return base64.b64encode(iv)

    def get_sign_src(self, params):
        if not isinstance(params, dict):
            raise TypeError('params must be a dict')
        src_list = list()
        for k in sorted(params.keys()):
            if isinstance(params[k], list):
                for item in params[k]:
                    if isinstance(item, dict):
                        src_list.append(self.get_sign_src(item))
            elif isinstance(params[k], dict):
                src_list.append(self.get_sign_src(params[k]))
            else:
                if isinstance(params[k], unicode):
                    params[k] = params[k].encode('utf-8')
                src_list.append('{key}={value}'.format(key=k, value=params[k]))

        return '&'.join(src_list)

    def check_sign(self, sign_str, params):
        sign_src = '{params_src}&key={key}'.format(
            params_src=self.get_sign_src(params),
            key=self.b64_key
        )

        return self.md5(sign_src) == sign_str

    def sign(self, params):
        sign_src = '{params_src}&key={key}'.format(
            params_src=self.get_sign_src(params),
            key=self.b64_key
        )

        return self.md5(sign_src)

    def encrypt(self, params, b64_iv):
        if isinstance(params, dict):
            for k, v in params.items():
                if isinstance(v, unicode):
                    params[k] = v.encode('utf-8')
        text = json.dumps(params, separators=(',', ':'))

        raw = aes_pad(text)
        iv = base64.b64decode(b64_iv)
        key = base64.b64decode(self.b64_key)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, encstr, b64_iv):
        key = base64.b64decode(self.b64_key)
        iv = base64.b64decode(b64_iv)

        enc = base64.b64decode(encstr)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        decrypt_str = aes_unpad(cipher.decrypt(enc).encode('utf-8'))

        return json.loads(decrypt_str)


if __name__ == '__main__':
    params = {
        "loan_no": "200201809040019002"
    }
    secret_key = 'aGZxX2NvbnRyYWN0X2Rvd25sb2FkX3JhbmRvbV9rZXk='
    auth = InternalSecure(secret_key)

    sign = auth.sign(params)  # ��ȡ����ǩ��
    print
    'sign = ', sign

    b64_iv = auth.get_b64iv()  # ��ȡ����iv
    print
    'b64_iv = ', b64_iv

    enc_str = auth.encrypt(params, b64_iv=b64_iv)  # ��ȡ��������
    print
    'enc_str = ', enc_str

    """
    {"iv":"/wIWJjLaeksorcpFoYNtjA==","sign":"d632bfd07e0224041b8420eada7fccee",
    "data":"VEMlf2IAlCKQF6e08qIWiMPn4Kmcs/TAwNRFpeJrJkbKFRD74lWg11leXrMr1C04"}
    """