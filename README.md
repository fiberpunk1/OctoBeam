# OctoBeam

## 1. 概述

OctoBeam目标在创建一个专门针对[Beam](https://github.com/fiberpunk1/Beam-ESP32)模块管理的Octoprint Plugin. 通过OctoBeam，您可以在Octoprint上实现如下功能:

- 搜索到局域网内所有的Beam模块
- 给每个Beam发送Gcode文件
- 控制Beam模块进行SD卡打印
- 向Beam发送调试Gcode指令
- 从Beam获取打印机的打印日志
- 获取打印进度

他们之间的控制关系如下图所示:

![img](./images/final-framwork.png)


## 2. 实现方式

Beam已经实现了一些类的restfulAPI，OctoBeam通过request请求来控制Beam模块。同是OctoBeam还包含了一个用于实时打印日志的socket模块,通过这个模块可以获取到Beam收到的所有打印机的返回信息。

TodoList

- [ ] Octoprint Plugin UI

## 3. Python用例介绍

OctoBeam先实现了一系列封装好的python包。通过这个python用例，您可以实现:

- 寻找局域网内的所有Beam模块
- SD卡文件管理
    - 上传文件到SD卡
    - 删除SD卡内的文件
    - 获取SD卡所有文件列表
- 发送Gcode指令
- 虚拟打印机串口(Socket实现)
- 获得温度信息/获得进度信息