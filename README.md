# ShinoBot —— 一个高可用的QQ机器人实现
## 0.项目介绍

ShinoBot是一个基于NoneBot框架构建的QQ机器人项目，目的是实现一个高可用且高性能的QQ聊天机器人，让完全不懂代码的小白也能够轻松部署和使用。目前ShinoBot已实现一些基础功能，如单词查询、历史上的今天、自动向群员打招呼的功能。未来我们计划实现的功能包括但不限于统一的权限和插件管理、插件市场、甚至管理面板。

## 1.快速入门

ShinoBot可以通过以下几个简单的步骤进行部署：

### 安装Python

ShinoBot需要Python3作为运行时的环境，尽管理论上任意Python 3.8以上的版本都可以运行，我们仍然推荐您使用最新的Python 3.10版本，因为ShinoBot基于Python 3.10的进行开发。您可以从[Python组织官网](https://python.org/)获取最新的Python下载。

### 部署go-cqhttp

> Note: 可以参照 [go-cqhttp 帮助中心](https://docs.go-cqhttp.org/)的使用教程。

1. 从[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)的官方仓库获取最新的[Release](https://github.com/Mrs4s/go-cqhttp/releases/latest)

2. 解压并进入解压后的文件夹

3. 在此文件夹打开终端，并键入

   `Windows:`

   ```powershell
   ./go-cqhttp.exe
   ```

   `Linux:`

   ```bash
   ./go-cqhttp
   ```

4. 您将会得到以下信息

   ```bash
   未找到配置文件，正在为您生成配置文件中！
   请选择你需要的通信方式:
   > 1: HTTP通信
   > 2: 正向 Websocket 通信
   > 3: 反向 Websocket 通信
   > 4: pprof 性能分析服务器
   > 5: 云函数服务
   请输入你需要的编号，可输入多个，同一编号也可输入多个(如: 233)
   您的选择是:
   ```

   这里输入"3"后回车

   ```bash
   默认配置文件已生成，请修改 config.yml 后重新启动!
   ```

   再次回车退出程序

5. 打开同目录下的`config.yml`文件

   首先我们在此设置QQ账号信息，按照注释进行相应配置即可

   ```yaml
   account: # 账号相关
     uin: 1233456 # QQ账号
     password: '' # 密码为空时使用扫码登录
     encrypt: false  # 是否开启密码加密
   ```

   如果您是在公网环境下进行使用，我们强烈推荐您设置token

   ```yaml
   # 默认中间件锚点
   default-middlewares: &default
     # 访问密钥, 强烈推荐在公网的服务器设置
     access-token: ''
   ```

   最后在此设置服务器IP和端口信息

   ```yaml
   servers:
     - ws-reverse:
         universal: ws://127.0.0.1:8080/ws/
   ```

6. 我们再次使用终端启动go-cqhttp(详见[第一步](https://botmashiro.github.io/MashiroDocs/#/quick-start/?id=部署go-cqhttp))，若提示成功登录，则go-cqhttp的部署完成。若您在部署过程中遇到其他问题，欢迎前去[go-cqhttp帮助中心](https://docs.go-cqhttp.org/)查询。

> Note: 如果出现发送信息失败的的情况（如账号被风控等），请删除go-cqhttp目录下的session.token文件并重启go-cqhttp

### 部署ShinoBot

1. 打开终端，键入以下命令：

```bash
git clone https://github.com/WhitePaper233/ShinoBot.git
```

如果因网络问题导致无法下载或下载过慢，请使用镜像源：

```bash
git clone https://github.91chi.fun/https://github.com/WhitePaper233/ShinoBot.git
```

2. 使用以下命令安装依赖

```bash
cd ShinoBot
pip install -r requirements.txt
```

同样，如果因网络问题导致无法下载或下载过慢，请使用镜像源：

```bash
cd ShinoBot
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

3. 用编辑器打开`config.yaml`，并配置超级用户QQ，配置完成后保存关闭

```yaml
host: '127.0.0.1'
port: 8080

nicknames: ['Bot', 'Shino', 'shino']

# 将“1234567890”替换为您的QQ
super_users: [1234567890]

no_prefix: true
command_prefix: ['/', '!!', '！！']
```

4. 使用以下命令启动ShinoBot

```bash
python Shino.py
```

5. 向机器人QQ号发送命令：`历史上的今天`，顺利的话，您应该获得相应信息

> Note: 如需要在QQ群中使用，命令前须@机器人

## 2.简单功能介绍

### 2.1.番剧查询

从 https://bangumi.tv/ 查询动画番剧信息

使用`查番 <番剧名>`获取番剧信息

例子：`查番 那年那兔那些事`

![番剧查询](https://pic.imgdb.cn/item/621b4b722ab3f51d91cd5273.png)

### 2.2 B站直播推送

当B站主播开播时，向特定群内发送一条提醒信息

打开`/plugins/blive_pusher/__init__.py`，将变量`target_group_id`的值改为需要推送开播信息群的群号，将变量`room_id`改为需要推送主播的房间号

例子：无命令，系统自动检测

### 2.3 B站视频详情信息

发送任何带有B站视频番号的消息后，机器人将发送一条有关视频信息的消息

例子：无命令，能够检测到的消息如`大家快来看看BV1bF411q7ue这个做的好棒`

![B站视频详情信息](https://pic.imgdb.cn/item/621b4b722ab3f51d91cd5270.png)

### 2.4 一言

让机器人说一句名言

例子：`一言`

![一言](https://pic.imgdb.cn/item/621b4b722ab3f51d91cd5292.png)

### 2.5 给我一张风景画！（此功能需要配置go-cqhttp的http代理）

从PixGreat仓库获取一张让人赏心悦目的风景图

例子：`我想要一张风景图`

![风景画](https://pic.imgdb.cn/item/621b4b722ab3f51d91cd5277.png)

### 2.6 历史上的今天

让机器人告诉你历史上的今天发生了什么

例子：`历史上的今天`

![历史上的今天](https://pic.imgdb.cn/item/621b4b722ab3f51d91cd5281.png)

### 2.7 欢迎信息

当新人入群时机器人会发送一条欢迎信息

例子：无命令，机器人入群时自动触发

### 2.8 有道翻译查词

使用`查词 <单词>`从有道翻译查询单词意思

例子：`查词 code`

![有道翻译查词](https://pic.imgdb.cn/item/621b4b742ab3f51d91cd579d.png)

更多功能开发中...

