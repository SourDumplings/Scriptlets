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
