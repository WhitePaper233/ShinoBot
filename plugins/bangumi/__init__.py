# -*- coding: utf-8 -*-
import aiohttp

from nonebot import on_command, CommandSession


@on_command('番剧查询', aliases=('查番', '找番', '查询番剧'))
async def find_bangumi(session: CommandSession):
    bangumi_name = session.current_arg_text.strip()
    if not bangumi_name:
        bangumi_name = (await session.aget(prompt='你想查询哪个番剧的信息呢？')).strip()
        while not bangumi_name:
            bangumi_name = (await session.aget(prompt='要查询的番剧名称不能为空呢，请重新输入')).strip()
    bangumi_info = await get_bangumi_info(bangumi_name)
    await session.send(bangumi_info)


async def get_bangumi_info(bangumi_name: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.bgm.tv/search/subject/{bangumi_name}',
                               params=[('type', 2), ('responseGroup', 'medium'), ('max_results', 1)]) as resp:
            result = await resp.json()
            if result['results'] == 0 or result['list'] is None:
                return '没有找到相关番剧呢~'
            else:
                return f"[CQ:image,file={result['list'][0]['images']['large']}]\n" \
                       f"{result['list'][0]['name_cn']}\n" \
                       f"{result['list'][0]['name']}\n" \
                       f"{result['list'][0]['summary']}\n" \
                       f"{(result['list'][0]['url']).replace('http://bgm.tv/', 'https://bangumi.tv/')}"
