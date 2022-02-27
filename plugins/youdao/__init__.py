# -*- coding: utf-8 -*-
import aiohttp

from nonebot import on_command, CommandSession


@on_command('有道', aliases=('yd', 'youdao', '查词', '查单词'))
async def youdao_query(bot_session: CommandSession):
    word = bot_session.current_arg_text.strip()
    if not word:
        word = (await bot_session.aget(prompt='你想查询哪个单词呢？')).strip()
        while not word:
            word = (await bot_session.aget(prompt='要查询的单词不能为空呢，请重新输入')).strip()
    msg = f'查询单词 {word} 的结果:\n'
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dict.youdao.com/suggest', params=[('q', word), ('doctype', 'json')]) as resp:
            result = await resp.json()
            if result['result']['code'] == 200:
                for entry in result['data']['entries']:
                    msg += (entry['entry'] + '\n')
                    msg += (entry['explain'])
                    if entry != result['data']['entries'][-1]:
                        msg += '\n\n'
                await bot_session.send(msg)
            else:
                await bot_session.send('没有找到你要查询的单词呢~')
