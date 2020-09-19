# 写在最前
这个项目完全是为了学习python，学习了原AutoXue的项目，项目地址 https://github.com/kessil/AutoXue
因为原作者没有更新，因此拿来作为研究学习之用，请遵守开源许可协议。严禁用于商业用途，禁止使用进行任何盈利活动。对一切非法使用所产生的后果，本人概不负责。
# 2020年9月19日
1.增加了多用户支持，如果是新设备第一次登录，必须提前登录用一次，把各种提示刷没了，否则app提示操作会导致程序崩溃

2.我没有将用户名做配置项，需要修改在main函数里修改用户名列表

3.适配最新版本的学习强国APP，挑战答题的地址也修改了。

4.删除了每周答题和专项答题，这块不是高频应用，且容易出问题，所以暂时屏蔽

5.增加了本地题库，采用题目模糊比对的方式查询答案，因为题库不全以及个别题目不准，不过循环几次就可以了。

6.学习强国用户名密码在main文件里，自行修改。

7.用之前安装fuzzywuzzy，          pip install fuzzywuzzy

另外，不写代码10多年了，对python也是不熟悉，很多句式和函数都是现学现用，代码质量不高，bug在所难免，各位多提意见。反馈错误带图加最后几段log，在logs文件夹里。

## 免责申明
`AutoXue`为本人`Python`学习交流的开源非营利项目，仅作为`Python`学习交流之用，使用需严格遵守开源许可协议。严禁用于商业用途，禁止使用`AutoXue`进行任何盈利活动。对一切非法使用所产生的后果，本人概不负责。

## 环境准备[下载](http://49.235.90.76:5000/downloads)
0. 如果之前添加过环境变量`ADB1.0.40`请确保删除之

1. 安装`JDK`，本文使用JDK1.8
    + 在环境变量中新建`JAVA_HOME`变量，值为JDK安装路径，如`C:\Program Files\Java\jdk1.8.0_05`
    + 新建`CLASSPATH`变量，值为`.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar;`
    + `Path`变量中添加：`%JAVA_HOME%\bin和%JAVA_HOME%\jre\bin`
    
2. 安装`SDK`，本文使用SDK r24.4.1
    + 在环境变量中新建`ANDROID_HOME`，值为SDK安装路径，如`C:\Program Files (x86)\Android\android-sdk`
    + 在Path变量中添加项：`%ANDROID_HOME%\platform-tools` 和 `%ANDROID_HOME%\tools`
    + 打开`SDK Manager.exe` 安装对应的工具和包,根据安卓版本进行安装，**Tools**和**Build-tools**别漏
+ ![image-20200601204634969](./image-20200601204634969.png)
    
3. 安装`Appium-desktop`，为了使用`UiAutomator2`，请将`Appium`设为以管理员权限启动，并赋予JDK和SDK所有权限

    ![image-20200601204913532](./image-20200601204913532.png)

4. 安装一个模拟器，就选夜神Nox吧，如用其他模拟器或真机出现问题请自救。

5. 安装`Python`，请至少使用3.7+版本，推荐3.8

## 使用方法(windows)
0. 克隆项目 `git clone https://github.com/kessil/AutoXue.git --depth 1`
1. 双击运行`setup.cmd`
2. 启动 `Appium` 和 `Nox`
3. 双击运行 `start.cmd`

## 写在最后
+ 在[这里](http://49.235.90.76:5000/downloads)可能有您需要的安装包，你可以官方网站下载使用最新版本，也可在[这里](http://49.235.90.76:5000/downloads)下载（未必最新版）
+ 强烈建议需要自定义配置文件的用户下载使用vscode编辑器,[why vscode?](https://hacpai.com/article/1569745141957)，请一定不要使用系统自带记事本修改配置文件。

