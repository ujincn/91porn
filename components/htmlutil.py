#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import logging


def get_all_a_link(raw_html):
    """
    提取网页中所有连接

    Args:
        raw_html (str): 网页内容
    Returns:
        list of str: 连接
    """

    links = []
    soup = BeautifulSoup(raw_html)
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
    soup = BeautifulSoup(raw_html)
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
    tag = BeautifulSoup(raw_html).find('source')
    return tag['src'] if tag else None


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
    tag = BeautifulSoup(raw_html).find('div', {'id': id})
    return tag.text if tag else None