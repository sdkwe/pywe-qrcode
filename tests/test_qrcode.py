# -*- coding: utf-8 -*-

import requests

from local_wecfg_example import WECHAT
from pywe_qrcode import (QRCode, qrcode_create, qrcode_download, qrcode_limit_scene, qrcode_limit_str_scene,
                         qrcode_scene, qrcode_show, qrcode_str_scene, qrcode_url)


class TestQRCodeCommands(object):

    def test_qrcode_create(self):
        """
        {
            "ticket":"gQH47joAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL2taZ2Z3TVRtNzJXV1Brb3ZhYmJJAAIEZ23sUwMEmm3sUw==",
            "expire_seconds":60,
            "url":"http://weixin.qq.com/q/kZgfwMTm72WWPkovabbI"
        }
        """
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')
        qrcode = QRCode(appid=appid, secret=appsecret)
        data = qrcode.create_scene(scene_id=0, expire_seconds=2592000)
        assert isinstance(data, dict)
        assert data.get('ticket', '')

        data = qrcode_str_scene(scene_str='pywe_qrcode', expire_seconds=2592000, appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data.get('ticket', '')

        data = qrcode.create_limit_scene(scene_id=0)
        assert isinstance(data, dict)
        assert data.get('ticket', '')

        data = qrcode_limit_str_scene(scene_str='pywe_qrcode', appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data.get('ticket', '')

    def test_qrcode_download(self):
        data = qrcode_download(ticket='gQH47joAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL2taZ2Z3TVRtNzJXV1Brb3ZhYmJJAAIEZ23sUwMEmm3sUw==')
        assert isinstance(data, requests.Response)
        assert data.status_code == 200

    def test_showurl(self):
        qrurl = qrcode_url(ticket='gQH47joAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL2taZ2Z3TVRtNzJXV1Brb3ZhYmJJAAIEZ23sUwMEmm3sUw==')
        assert isinstance(qrurl, basestring)
