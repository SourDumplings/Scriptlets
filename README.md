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

- proc_files_recursively
递归处理目录的文件的小脚本

- shutdowntimer
制定定时关机计划的小脚本

- spectrumplot
根据光谱数据绘制光谱图线的小脚本

- qrcode
可以将连接转换为二维码，控制台运行命令：
```
java -jar qrcode.jar url directoryPath filename
```
例如：
```
java -jar qrcode.jar www.baidu.com D:/Azjc/test bb.jpg
```
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

- watermarker
为 PDF 添加水印的脚本，使用时需要仔细调整参数，直到达到满意的效果为止