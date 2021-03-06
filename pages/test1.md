title: 抓取网页的含义和URL基本构成
date: 2017-03-29
id: 1


一、网络爬虫的定义
网络爬虫，即Web Spider，是一个很形象的名字。
把互联网比喻成一个蜘蛛网，那么Spider就是在网上爬来爬去的蜘蛛。
网络蜘蛛是通过网页的链接地址来寻找网页的。
从网站某一个页面（通常是首页）开始，读取网页的内容，找到在网页中的其它链接地址，
然后通过这些链接地址寻找下一个网页，这样一直循环下去，直到把这个网站所有的网页都抓取完为止。
如果把整个互联网当成一个网站，那么网络蜘蛛就可以用这个原理把互联网上所有的网页都抓取下来。
这样看来，网络爬虫就是一个爬行程序，一个抓取网页的程序。
网络爬虫的基本操作是抓取网页。
那么如何才能随心所欲地获得自己想要的页面？
我们先从URL开始。

二、浏览网页的过程
抓取网页的过程其实和读者平时使用IE浏览器浏览网页的道理是一样的。
比如说你在浏览器的地址栏中输入    www.baidu.com    这个地址。
打开网页的过程其实就是浏览器作为一个浏览的“客户端”，向服务器端发送了 一次请求，把服务器端的文件“抓”到本地，再进行解释、展现。
HTML是一种标记语言，用标签标记内容并加以解析和区分。
浏览器的功能是将获取到的HTML代码进行解析，然后将原始的代码转变成我们直接看到的网站页面。

三、URI和URL的概念和举例
简单的来讲，URL就是在浏览器端输入的    http://www.baidu.com    这个字符串。
在理解URL之前，首先要理解URI的概念。
什么是URI？
Web上每种可用的资源，如 HTML文档、图像、视频片段、程序等都由一个通用资源标志符(Universal Resource Identifier， URI)进行定位。 
URI通常由三部分组成：
①访问资源的命名机制；
②存放资源的主机名；
③资源自身 的名称，由路径表示。
如下面的URI：
http://www.why.com.cn/myhtml/html1223/
我们可以这样解释它：
①这是一个可以通过HTTP协议访问的资源，
②位于主机 www.webmonkey.com.cn上，
③通过路径“/html/html40”访问。 

四、URL的理解和举例
URL是URI的一个子集。它是Uniform Resource Locator的缩写，译为“统一资源定位 符”。
通俗地说，URL是Internet上描述信息资源的字符串，主要用在各种WWW客户程序和服务器程序上。
采用URL可以用一种统一的格式来描述各种信息资源，包括文件、服务器的地址和目录等。
URL的一般格式为(带方括号[]的为可选项)：
protocol :// hostname[:port] / path / [;parameters][?query]#fragment

URL的格式由三部分组成： 
①第一部分是协议(或称为服务方式)。
②第二部分是存有该资源的主机IP地址(有时也包括端口号)。
③第三部分是主机资源的具体地址，如目录和文件名等。
第一部分和第二部分用“://”符号隔开，
第二部分和第三部分用“/”符号隔开。
第一部分和第二部分是不可缺少的，第三部分有时可以省略。 

五、URL和URI简单比较
URI属于URL更低层次的抽象，一种字符串文本标准。
换句话说，URI属于父类，而URL属于URI的子类。URL是URI的一个子集。
URI的定义是：统一资源标识符；
URL的定义是：统一资源定位符。
二者的区别在于，URI表示请求服务器的路径，定义这么一个资源。
而URL同时说明要如何访问这个资源（http://）。




下面来看看两个URL的小例子。

1.HTTP协议的URL示例：
使用超级文本传输协议HTTP，提供超级文本信息服务的资源。 
例：http://www.peopledaily.com.cn/channel/welcome.htm 
其计算机域名为www.peopledaily.com.cn。
超级文本文件(文件类型为.html)是在目录 /channel下的welcome.htm。
这是中国人民日报的一台计算机。 
例：http://www.rol.cn.NET/talk/talk1.htm 
其计算机域名为www.rol.cn.Net。
超级文本文件(文件类型为.html)是在目录/talk下的talk1.htm。
这是瑞得聊天室的地址，可由此进入瑞得聊天室的第1室。

2．文件的URL
用URL表示文件时，服务器方式用file表示，后面要有主机IP地址、文件的存取路 径(即目录)和文件名等信息。
有时可以省略目录和文件名，但“/”符号不能省略。 
例：file://ftp.yoyodyne.com/pub/files/foobar.txt 
上面这个URL代表存放在主机ftp.yoyodyne.com上的pub/files/目录下的一个文件，文件名是foobar.txt。
例：file://ftp.yoyodyne.com/pub 
代表主机ftp.yoyodyne.com上的目录/pub。 
例：file://ftp.yoyodyne.com/ 
代表主机ftp.yoyodyne.com的根目录。 

爬虫最主要的处理对象就是URL，它根据URL地址取得所需要的文件内容，然后对它 进行进一步的处理。
因此，准确地理解URL对理解网络爬虫至关重要。
