# -*- coding: utf-8 -*-
import nonebot

from utils.config import config


class Shino:
    @staticmethod
    def run():
        nonebot.init(config)
        nonebot.load_builtin_plugins()
        nonebot.load_plugins('./plugins', 'plugins')
        nonebot.run()
