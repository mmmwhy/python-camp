> [参考代码](https://github.com/mmmwhy/python-camp)一同附上，分析过程见[李飞阳](https://mmmxcc.cn/tags/Python%E7%BB%83%E4%B9%A0%E9%A2%98/)，请多指教。

---
<!--more-->
# 一、基础问题

**题目1.1：**[图片加水印](https://mmmxcc.cn/2016/12/16/%E7%AC%AC%E4%B8%80%E9%A2%98%EF%BC%9APython%E5%9B%BE%E7%89%87%E6%B7%BB%E5%8A%A0%E6%B0%B4%E5%8D%B0/)，类似于微信未读信息数量那种提示效果

![头像](http://cdn.mmmxcc.cn/blog/20161216/115246388.jpg?imageMogr2/thumbnail/!80p)


**题目1.2：**[使用 Python 如何生成 200 个激活码（或者优惠券）](https://mmmxcc.cn/2017/02/07/%E7%AC%AC%E4%BA%8C%E9%A2%98%EF%BC%9A%E4%BD%BF%E7%94%A8-Python-%E5%A6%82%E4%BD%95%E7%94%9F%E6%88%90-200-%E4%B8%AA%E6%BF%80%E6%B4%BB%E7%A0%81/)

**题目1.3**：[将 0002 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。 ](https://mmmxcc.cn/2017/02/10/%E7%AC%AC%E4%B8%89%E9%A2%98%EF%BC%9A%E5%B0%86200%E4%B8%AA%E6%BF%80%E6%B4%BB%E7%A0%81%E4%BF%9D%E5%AD%98%E5%88%B0-MySQL/)


**题目1.4：**任一个英文的纯文本文件，统计其中的单词出现的个数。

**题目1.5：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

**题目1.6：**使用 Python 生成类似于下图中的**字母验证码图片**

![字母验证码](http://i.imgur.com/aVhbegV.jpg)

- [阅读资料](http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python) 

**题目1.7：** 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

    北京
    程序员
    公务员
    领导
    牛比
    牛逼
    你娘
    你妈
    love
    sex
    jiangge

**题目1.8：** 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

    {
        "1":["张三",150,120,100],
        "2":["李四",90,99,95],
        "3":["王五",60,66,68]
    }

请将上述内容写到 student.xls 文件中，如下图所示：

![student.xls](http://i.imgur.com/nPDlpme.jpg)

- [阅读资料](http://www.cnblogs.com/skynet/archive/2013/05/06/3063245.html) 腾讯游戏开发 XML 和 Excel 内容相互转换

**题目1.9：** 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

- 阅读资料 [用户密码的存储与 Python 示例](http://zhuoqiang.me/password-storage-and-python-example.html)

- 阅读资料 [Hashing Strings with Python](http://www.pythoncentral.io/hashing-strings-with-python/)

- 阅读资料 [Python's safest method to store and retrieve passwords from a database](http://stackoverflow.com/questions/2572099/pythons-safest-method-to-store-and-retrieve-passwords-from-a-database)

---
# 二、数据分析

**题目2.1：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

**题目2.2：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

**题目2.3：** [登陆中国联通网上营业厅](http://iservice.10010.com/index_.html) 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。

---
# 三、爬虫方面

**题目3.1：**一个HTML文件，找出里面的**正文**。

**题目3.2：**[一个HTML文件，找出里面的**链接**。](https://mmmxcc.cn/2016/12/13/%E6%8F%90%E5%8F%96%E7%BD%91%E9%A1%B5%E4%BF%A1%E6%81%AF/)

**题目3.3：** 用 Python 写一个爬图片的程序，可以参考[Python爬取图片（使用urllib2）](https://mmmxcc.cn/2016/12/15/Python%E7%88%AC%E5%8F%96%E5%9B%BE%E7%89%87%EF%BC%88%E4%BD%BF%E7%94%A8urllib2%EF%BC%89/)，如果出现难题，可以尝试[selenium自动化测试工具](https://mmmxcc.cn/2016/12/29/%E4%BD%BF%E7%94%A8Python-selenium%E5%A4%84%E7%90%86%E9%A1%B5%E9%9D%A2%E5%BB%B6%E8%BF%9F%E5%8A%A0%E8%BD%BD%E9%97%AE%E9%A2%98/)



---
#  四、Web问题

**题目4.1：** 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

[阅读资料：Python 有哪些 Web 框架](http://v2ex.com/t/151643#reply53)

- ![留言簿参考](http://i.imgur.com/VIyCZ0i.jpg)


**题目4.2：** 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

- ![SpringSide 版TodoList](http://i.imgur.com/NEf7zHp.jpg)



**题目来自 [易枭寒的Github](https://github.com/Yixiaohan)**
