#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import logging
import execjs
import re


def get_all_a_link(raw_html):
    """
    提取网页中所有连接

    Args:
        raw_html (str): 网页内容
    Returns:
        list of str: 连接
    """

    links = []
    soup = BeautifulSoup(raw_html, "html.parser")
    for link in soup.findAll('a', href=True):
        links.append(link['href'])
    return links


def get_all_video_link(raw_html):
    """
    提取网页中所有视频页连接
        http://91porn.com/view_video.php?viewkey=5f9735d3550e4055a6be"
    Args:
        raw_html (str): 网页内容
    Returns:
        list of str: 视频详情页连接
    """

    links = []
    soup = BeautifulSoup(raw_html, "html.parser")
    for link in soup.findAll('a', href=True):
        if link['href'].find('viewkey=') > -1:
            # logging.debug("link %s" % link['href'])
            links.append(link['href'])
    return links


def get_srouce_tag_src(raw_html):
    """
    获取页面中source标签的src属性
        <source src="http://192.240.120.35//mp43/232306.mp4?st=3_OK5Y0RRH-pHNGVdkWckg&e=1503546759" type="video/mp4">
    Args:
        raw_html (str): 网页内容
    Returns:
        str: src值
    """
    soup = BeautifulSoup(raw_html, 'html.parser')
    src = re.search(r'document.write\(strencode\("(.+)","(.+)",.+\)\);', str(soup.find_all('script')))

    ctx = execjs.compile("""
    ;
    var encode_version = 'sojson.v5',
        lbbpm = '__0x33ad7',
        __0x33ad7 = ['QMOTw6XDtVE=', 'w5XDgsORw5LCuQ==', 'wojDrWTChFU=', 'dkdJACw=', 'w6zDpXDDvsKVwqA=', 'ZifCsh85fsKaXsOOWg==', 'RcOvw47DghzDuA==', 'w7siYTLCnw=='];
    (function(_0x94dee0, _0x4a3b74) {
        var _0x588ae7 = function(_0x32b32e) {
            while (--_0x32b32e) {
                _0x94dee0['push'](_0x94dee0['shift']());
            }
        };
        _0x588ae7(++_0x4a3b74);
    }(__0x33ad7, 0x8f));
    var _0x5b60 = function(_0x4d4456, _0x5a24e3) {
        _0x4d4456 = _0x4d4456 - 0x0;
        var _0xa82079 = __0x33ad7[_0x4d4456];
        if (_0x5b60['initialized'] === undefined) {
            (function() {
                var _0xef6e0 = typeof window !== 'undefined' ? window : typeof process === 'object' && typeof require === 'function' && typeof global === 'object' ? global : this;
                var _0x221728 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
                _0xef6e0['atob'] || (_0xef6e0['atob'] = function(_0x4bb81e) {
                    var _0x1c1b59 = String(_0x4bb81e)['replace'](/=+$/, '');
                    for (var _0x5e3437 = 0x0, _0x2da204, _0x1f23f4, _0x3f19c1 = 0x0, _0x3fb8a7 = ''; _0x1f23f4 = _0x1c1b59['charAt'](_0x3f19c1++); ~_0x1f23f4 && (_0x2da204 = _0x5e3437 % 0x4 ? _0x2da204 * 0x40 + _0x1f23f4 : _0x1f23f4, _0x5e3437++ % 0x4) ? _0x3fb8a7 += String['fromCharCode'](0xff & _0x2da204 >> (-0x2 * _0x5e3437 & 0x6)) : 0x0) {
                        _0x1f23f4 = _0x221728['indexOf'](_0x1f23f4);
                    }
                    return _0x3fb8a7;
                });
            }());
            var _0x43712e = function(_0x2e9442, _0x305a3a) {
                var _0x3702d8 = [],
                    _0x234ad1 = 0x0,
                    _0xd45a92,
                    _0x5a1bee = '',
                    _0x4a894e = '';
                _0x2e9442 = atob(_0x2e9442);
                for (var _0x67ab0e = 0x0, _0x1753b1 = _0x2e9442['length']; _0x67ab0e < _0x1753b1; _0x67ab0e++) {
                    _0x4a894e += '%' + ('00' + _0x2e9442['charCodeAt'](_0x67ab0e)['toString'](0x10))['slice'](-0x2);
                }
                _0x2e9442 = decodeURIComponent(_0x4a894e);
                for (var _0x246dd5 = 0x0; _0x246dd5 < 0x100; _0x246dd5++) {
                    _0x3702d8[_0x246dd5] = _0x246dd5;
                }
                for (_0x246dd5 = 0x0; _0x246dd5 < 0x100; _0x246dd5++) {
                    _0x234ad1 = (_0x234ad1 + _0x3702d8[_0x246dd5] + _0x305a3a['charCodeAt'](_0x246dd5 % _0x305a3a['length'])) % 0x100;
                    _0xd45a92 = _0x3702d8[_0x246dd5];
                    _0x3702d8[_0x246dd5] = _0x3702d8[_0x234ad1];
                    _0x3702d8[_0x234ad1] = _0xd45a92;
                }
                _0x246dd5 = 0x0;
                _0x234ad1 = 0x0;
                for (var _0x39e824 = 0x0; _0x39e824 < _0x2e9442['length']; _0x39e824++) {
                    _0x246dd5 = (_0x246dd5 + 0x1) % 0x100;
                    _0x234ad1 = (_0x234ad1 + _0x3702d8[_0x246dd5]) % 0x100;
                    _0xd45a92 = _0x3702d8[_0x246dd5];
                    _0x3702d8[_0x246dd5] = _0x3702d8[_0x234ad1];
                    _0x3702d8[_0x234ad1] = _0xd45a92;
                    _0x5a1bee += String['fromCharCode'](_0x2e9442['charCodeAt'](_0x39e824) ^ _0x3702d8[(_0x3702d8[_0x246dd5] + _0x3702d8[_0x234ad1]) % 0x100]);
                }
                return _0x5a1bee;
            };
            _0x5b60['rc4'] = _0x43712e;
            _0x5b60['data'] = {};
            _0x5b60['initialized'] = !![];
        }
        var _0x4be5de = _0x5b60['data'][_0x4d4456];
        if (_0x4be5de === undefined) {
            if (_0x5b60['once'] === undefined) {
                _0x5b60['once'] = !![];
            }
            _0xa82079 = _0x5b60['rc4'](_0xa82079, _0x5a24e3);
            _0x5b60['data'][_0x4d4456] = _0xa82079;
        } else {
            _0xa82079 = _0x4be5de;
        }
        return _0xa82079;
    };
    if (typeof encode_version !== 'undefined' && encode_version === 'sojson.v5') {
        function strencode(_0x50cb35, _0x1e821d) {
            var _0x59f053 = {
                'MDWYS': '0|4|1|3|2',
                'uyGXL': function _0x3726b1(_0x2b01e8, _0x53b357) {
                    return _0x2b01e8(_0x53b357);
                },
                'otDTt': function _0x4f6396(_0x33a2eb, _0x5aa7c9) {
                    return _0x33a2eb < _0x5aa7c9;
                },
                'tPPtN': function _0x3a63ea(_0x1546a9, _0x3fa992) {
                    return _0x1546a9 % _0x3fa992;
                }
            };
            var _0xd6483c = _0x59f053[_0x5b60('0x0', 'cEiQ')][_0x5b60('0x1', '&]Gi')]('|'),
                _0x1a3127 = 0x0;
            while (!![]) {
                switch (_0xd6483c[_0x1a3127++]) {
                case '0':
                    _0x50cb35 = _0x59f053[_0x5b60('0x2', 'ofbL')](atob, _0x50cb35);
                    continue;
                case '1':
                    code = '';
                    continue;
                case '2':
                    return _0x59f053[_0x5b60('0x3', 'mLzQ')](atob, code);
                case '3':
                    for (i = 0x0; _0x59f053[_0x5b60('0x4', 'J2rX')](i, _0x50cb35[_0x5b60('0x5', 'Z(CX')]); i++) {
                        k = _0x59f053['tPPtN'](i, len);
                        code += String['fromCharCode'](_0x50cb35[_0x5b60('0x6', 's4(u')](i) ^ _0x1e821d['charCodeAt'](k));
                    }
                    continue;
                case '4':
                    len = _0x1e821d[_0x5b60('0x7', '!Mys')];
                    continue;
                }
                break;
            }
        }
    } else {
        alert('');
    }
    ;
    """)

    realsrc = ctx.call('strencode', src.group(1), src.group(2))
    tag = BeautifulSoup(realsrc, 'html.parser').find('source')
    return tag['src'] if realsrc else None


def get_text_by_id(raw_html, id):
    """
    获取指定id标签的内容
        <div id="viewvideo-title">
            中午下班去公司洗手间玩一下、115云盘精品国产片看简介、自用补肾产品看简介、全球领先类爱情平台看简介
        </div>
    args:
        raw_html (str): 网页内容
        id (str): 标签id
    returns:
        str: 标签文本
    """
    tag = BeautifulSoup(raw_html, "html.parser").find('div', {'id': id})
    return tag.text if tag else None
