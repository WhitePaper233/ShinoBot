# -*- coding: utf-8 -*-
import re

import aiohttp

from nonebot import on_natural_language, NLPSession


@on_natural_language(keywords={'av', 'AV', 'BV', 'bv'}, only_to_me=False)
async def detailed_bili(bot_session: NLPSession):
    # 番号匹配
    pattern = re.compile(r'((av|AV)\d+|(bv|BV)1(\d|\w){2}4(\d|\w)1(\d|\w)7(\d|\w){2})')
    msg = bot_session.msg_text
    vid_list = [group[0] for group in pattern.findall(msg)]
    for vid in vid_list:
        if vid[:2].lower() == 'av':
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.bilibili.com/x/web-interface/view',
                                       params=[('aid', vid[2:])]) as resp:
                    result = await resp.json()
            if result['code'] == 0:
                message = f"{result['data']['title']}\n[CQ:image,file={result['data']['pic']}]\n" \
                          f"{result['data']['desc_v2'][0]['raw_text']}\nhttps://www.bilibili.com/video/av{vid[2:]}"
                await bot_session.send(message)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.bilibili.com/x/web-interface/view',
                                       params=[('bvid', vid[2:])]) as resp:
                    result = await resp.json()
            if result['code'] == 0:
                message = f"{result['data']['title']}\n[CQ:image,file={result['data']['pic']}]\n" \
                          f"{result['data']['desc_v2'][0]['raw_text']}\nhttps://www.bilibili.com/video/BV{vid[2:]}"
                await bot_session.send(message)
