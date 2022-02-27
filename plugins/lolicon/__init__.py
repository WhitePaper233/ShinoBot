# -*- coding: utf-8 -*-
import aiohttp

from nonebot import on_natural_language, NLPSession


@on_natural_language(keywords={'色色', '瑟瑟', '涩涩', '色图', '涩图', '瑟图'}, only_to_me=True)
async def pix_great(bot_session: NLPSession):
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get('https://api.lolicon.app/setu/v2') as resp:
                response_dict = await resp.json()
                if not response_dict['data'][0]['r18']:
                    break
                else:
                    continue

        await bot_session.send(f'[CQ:image,file={response_dict["data"][0]["title"]},'
                               f'url={response_dict["data"][0]["urls"]["original"]}]')
