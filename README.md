<!--
 * @Author: SourDumplings
 * @Date: 2017-10-06 09:43:09
 * @Link: https://github.com/SourDumplings/
 * @Email: changzheng300@foxmail.com
 * @Description: 脚本说明文件
 -->
# Scriptlets
----- 版权所有 酸饺子 -----

脚本说明：

- bizhidownload
通过网络爬虫下载壁纸的脚本

- codecalc
统计所写的代码量的脚本，为10万行代码而努力吧！

- downloadcatpic
利用爬虫下载猫图的小脚本

- file_renamer
批量修改文件名的小脚本

- shutdowntimer
制定定时关机计划的小脚本

- spectrumplot
根据光谱数据绘制光谱图线的小脚本

- BeanUtils
可以自动将map数据填到Java的Bean类，示例：
```java
BeanUtils.populate(user, map);
```

- Servlet
JavaWeb开发中的Servlet需要的Jar包

- IOUtils
可以很方便的进行输入输出流的对接，示例：
```java
IOUtils.copy(is, os);
IOUtils.closeQuietly(is);
IOUtils.closeQuietly(os);
```

- qrcode
可以将连接转换为二维码，控制台运行命令：
```
java -jar qrcode.jar url directoryPath filename
```
例如：
```
java -jar qrcode.jar www.baidu.com D:/Azjc/test bb.jpg
```

- UUIDUtils&UploadUtils
生成随机字符串（用于文件名等ID），UploadUtils用于将字符串转为多层目录（避免单目录下文件太多造成性能问题）

- CookieUtils
使用Cookie的工具类

- RegexpUtils
正则表达式工具类，可以匹配常用的字符串

- dateTime
时间处理工具，可以处理网页上的时间格式，用法示例：
```javascript
var date = DateTime.format(dateUnformatted, "yyyy-MM-dd HH:mm:ss");
```

- vultr_ss_on_demand
按需使用 vultr，使用前运行`create.py`，使用完运行`destroy.py`
使用前准备（~代指用户根目录）：
    - 建立`~/vultr/ssr`目录
    - 建立`~/vultr/apikey.txt`，存 API-KEY，并记得在 API-KEY 页面上打开访问
    - 建立`~/vultr/ssr/ssrPassword.txt`存 SSR 的访问密码
    - 修改脚本中`userPath`为用户根目录，结尾不带`/`
使用后在 `~/vultr/ssr` 目录下找到`local.json`文件，记录着 SSR 建立好的信息
    - 协议是：origin
    - 混淆：plain
