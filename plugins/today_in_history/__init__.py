# -*- coding: utf-8 -*-
import aiohttp

from nonebot import on_command, CommandSession


@on_command('历史上的今天')
async def today_in_history(bot_session: CommandSession):
    msg = ''
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.oick.cn/lishi/api.php') as resp:
            data = await resp.json()
            for item in data['result']:
                msg += f'{item["date"]}: {item["title"]}\n'
    await bot_session.send(msg)
