# -*- coding: utf-8 -*-
import random

import aiohttp

from nonebot import on_natural_language, NLPSession


@on_natural_language(keywords={'风景'}, only_to_me=True)
async def pix_great(bot_session: NLPSession):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://gitee.com/whitepaper233/PixGreat/raw/main/indexs/%23%E9%A2%A8%E6%99%AF.json'
                               ) as resp:
            index = await resp.json(content_type='text/plain')
            key_list = list(index.keys())
            key = key_list[random.randint(0, (len(key_list) - 1))]
            pic_id = index[key][random.randint(0, (len(index[key]) - 1))]
        async with session.get(f'https://gitee.com/whitepaper233/PixGreat/raw/main/database/{pic_id}.json') as r:
            pic_info = await r.json(content_type='text/plain')

    await bot_session.send(f'[CQ:image,file={pic_info["title"]},url={pic_info["url"]}]')
