# -*- coding: utf-8 -*-
import re

import yaml

from nonebot.default_config import *

# 读取配置文件
with open('./config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# 地址端口
HOST = config['host']
PORT = config['port']

# 别名
NICKNAME = config['nicknames']

# 超级管理员
SUPERUSERS = config['super_users']

# 命令匹配
command_prefix = ''
for i in config['command_prefix']:
    command_prefix += i
if config['no_prefix']:
    COMMAND_START = ['', re.compile(rf'[{command_prefix}]+')]
else:
    COMMAND_START = [re.compile(rf'[{command_prefix}]+')]
