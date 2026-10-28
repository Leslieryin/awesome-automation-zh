# awesome-automation-zh · 自动化专业开源资源导航

![CI](https://github.com/Leslieryin/awesome-automation-zh/actions/workflows/ci.yml/badge.svg)

> **EN** — A curated Chinese-language resource list for automation students — control theory, embedded, robotics and competitions. Every entry carries a one-line verdict, followed by a four-year learning path.

为自动化（及其近亲：电气、测控、机器人工程）专业学生整理的开源资源导航。不是链接堆砌——每条都有**一句话点评**告诉你它解决什么问题、什么时候用，最后附一条从大一到大四的**学习路径**。

> 收录标准：开源、可实际拿来用、社区活跃或经过时间检验。想补充或纠错，先看 [贡献指南](CONTRIBUTING.md)——里面有格式要求（CI 会校验）和点评该写什么。

## 一、控制理论与仿真

不装 MATLAB 也能学自控——这些开源工具覆盖了课程与课程设计的绝大部分需求。

- [python-control](https://github.com/python-control/python-control) —— Python 版 Control System Toolbox：传递函数、阶跃响应、Bode/Nyquist、LQR/LQR 全都有，配合 Jupyter 做实验报告体验极好
- [GNU Octave](https://octave.org/) —— 最接近 MATLAB 的开源替代，语法基本兼容，课程里的 MATLAB 作业大多能直接跑
- [Scilab / Xcos](https://www.scilab.org/) —— 开源「MATLAB+Simulink」组合，Xcos 拖块仿真可作为 Simulink 平替
- [OpenModelica](https://github.com/OpenModelica/OpenModelica) —— 基于 Modelica 语言的物理系统建模，多领域（电/机械/热/液）联合仿真利器
- [ControlSystems.jl](https://github.com/JuliaControl/ControlSystems.jl) —— Julia 生态的控制工具箱，速度极快，适合大规模/实时场景研究
- [control-lab](https://github.com/Leslieryin/control-lab) —— 单文件网页版自控原理实验台（本作者出品）：拖滑块看 ζ/Kp/Ki/Kd 对曲线的影响，预习复习神器

## 二、嵌入式与单片机

自动化的另一半物理世界。从裸机到 RTOS 到 GUI。

- [STM32Cube 系列仓库](https://github.com/STMicroelectronics) —— ST 官方 HAL/例程/中间件源码，STM32 开发绕不开的第一手资料
- [FreeRTOS](https://github.com/FreeRTOS/FreeRTOS) —— 事实标准的嵌入式 RTOS，源码即教材（任务调度/队列/信号量的工业级实现）
- [RT-Thread](https://github.com/RT-Thread/rt-thread) —— 国产 RTOS 之光，中文文档完善，国内面试提到它是加分项
- [PlatformIO](https://github.com/platformio/platformio-core) —— 一套工具链管所有板子（STM32/ESP32/Arduino...），告别 Keil 只能开一个工程的痛苦
- [Arduino](https://github.com/arduino/Arduino) —— 快速原型之王，验证传感器/执行器想法时比 STM32 快十倍
- [LVGL](https://github.com/lvgl/lvgl) —— 嵌入式 GUI 事实标准，做带屏幕的作品（竞赛/课设）直接上
- [Wokwi](https://wokwi.com/) —— 浏览器里仿真 ESP32/Arduino/STM32，没板子也能写作业调试

## 三、机器人与 ROS2

- [ROS 2 官方文档](https://docs.ros.org/) —— 机器人领域的通用中间件，从 tutorial 开始学，毕设/实验室项目大概率会用到
- [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) —— 机器人算法图解百科：路径规划、SLAM、MPC、卡尔曼滤波全有动画演示，看懂一个算法胜过读十篇博客
- [PX4 Autopilot](https://github.com/PX4/PX4-Autopilot) —— 工业级开源飞控，无人机方向入门/深入的标配
- [rmoss_gazebo](https://github.com/robomaster-oss/rmoss_gazebo) —— RoboMaster OSS 的 Gazebo 仿真栈，没机器人也能跑算法

## 四、学科竞赛开源

竞赛是自动化专业最好的实践路径。以下仓库都经过实赛检验。

### 电子设计竞赛（电赛 / TI 杯）

- [NUEDC_TOPIC](https://github.com/zuoliangyu/NUEDC_TOPIC) —— 1994 年至今全部电赛赛题文档（更新到 2026），备赛第一站：先把历年题目过一遍
- [CCBP/NUEDC_Topic](https://github.com/CCBP/NUEDC_Topic) —— 同类赛题合集，与上一条互补查漏
- [nuedc_template](https://github.com/chenboshuo/nuedc_template) —— 电赛设计报告 LaTeX 模板，省下排版时间做硬件
- [官方培训网](https://www.nuedc-training.com.cn/) —— 组委会授权的唯一官方培训平台，有权威培训资源

### 全国大学生智能汽车竞赛（恩智浦杯）

- [Awesome-IntelligentCarRace](https://github.com/ittuann/Awesome-IntelligentCarRace) —— 历届智能车开源项目总索引，按届/组别整理，找往届优秀方案先来这
- [逐飞科技开源库](https://github.com/seekfree) —— 智能车圈事实标准的底层库（STC/STM32/i.MX RT/英飞凌 TC 全系主控），配套摄像头/屏幕驱动开箱即用

### RoboMaster 机甲大师

- [awesome-robomaster](https://github.com/robomaster-oss/awesome-robomaster) —— RM 大赛与机器人开发开源项目总入口
- [HNUYueLuRM/basic_framework](https://github.com/HNUYueLuRM/basic_framework) —— 湖南大学跃鹿战队的通用嵌入式控制框架，学习「工程级嵌入式代码怎么组织」的好范本
- [Development-Board-C-Examples](https://github.com/RoboMaster/Development-Board-C-Examples) —— RoboMaster 官方 C 型开发板例程，入队第一份参考代码
- [SJTU-RoboMaster-Team](https://github.com/SJTU-RoboMaster-Team) —— 上海交大交龙战队（33+ 仓库），看顶级战队怎么开源整个体系
- [RoboMaster 社区 BBS](https://bbs.robomaster.com/) —— 各战队赛季开源（电控/视觉/机械）的主要发布地

## 五、电子设计工具

- [KiCad](https://github.com/KiCad/KiCad) —— 开源 EDA，画原理图/PCB 够用且免费，本科到研究生阶段全覆盖

## 六、给自动化专业的一条学习路径

**大一**：C 语言 + 单片机入门（Arduino 快速起兴趣 → STM32 裸机），装好 [PlatformIO](https://github.com/platformio/platformio-core)。数学课认真学——后面全是回响。

**大二**：模电数电 + [STM32Cube](https://github.com/STMicroelectronics) HAL 库实战；接触 [FreeRTOS](https://github.com/FreeRTOS/FreeRTOS) 理解多任务；开始打比赛（智能车/电赛，用上面第四节的资源）。

**大三**：自控原理配 [control-lab](https://github.com/Leslieryin/control-lab) + [python-control](https://github.com/python-control/python-control) 做仿真作业；学 [ROS 2](https://docs.ros.org/)；用 [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) 补机器人算法。确定方向（控制/嵌入式/机器人/视觉）。

**大四**：选定一个开源项目**深入读源码并提交 PR**（比再刷十个教程有用）；毕设尽量贴近真实工程（如基于 PX4 或 ROS 2 做完整系统）。

> 通用心法：**手里要有板子，代码要能跑通，简历上的每个项目都要经得起追问。**

## License

MIT
