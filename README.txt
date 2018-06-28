天眼查 字体反爬~


需要配置secure.py 配置文件  前三项为百度API 参数  第四个为REDIS数据库配置  调用run 下的run函数 即可获取正确映射

由于生成的 字体文件 可复用率 极高 所以hash后存表 提高效率 

woff文件可在css里找到 即用 <link rel="stylesheet" href="https://static.tianyancha.com/fonts-styles/css/8a/8a7e2df0/font.css">
'''
@font-face {
  font-family: "tyc-num";
  src: url('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.eot'); /* IE9*/
  src: url('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.eot#iefix') format('embedded-opentype'), /* IE6-IE8 */
  url('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.woff') format('woff'), /* chrome, firefox */
  url('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.ttf') format('truetype'), /* chrome, firefox, opera, Safari, Android, iOS 4.2+*/
  url('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.svg#tic') format('svg'); /* iOS 4.1- */
}

.font-8a7e2df0 .tyc-num {
  font-family: "tyc-num" !important;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
'''
提取 woff地址即可  --也可以直接构造  目前可行  font_key = '8a7e2df0' font_url = 'https://static.tianyancha.com/fonts-styles/fonts/%s/%s/tyc-num.woff' % (font_key[:2],font_key)

word = '8973-78-88'
run.run('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.woff',word)
>> 2014-12-22


word = '开必、销售计问乐网络应度软件；中计、制江、加工计问乐网络难待十动其相受技术服务和咨询服务；服务：传有位业租赁，翻译，成越人的整证书劳们职业技社培训，成越人的整文承举育培训（涉及置提证的达外）。'
run.run('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.woff',word)
>>开发、销售计算机网络应用软件；设计、制作、加工计算机网络产品并提供相关技术服务和咨询服务；服务：自有物业租赁，翻译，成年人的非证书劳动职业技能培训，成年人的非文化教育培训（涉及许可证的除外）。

word = '服务：企业管理，计问乐系统服务，空脑们画中计，况济可息咨询服务（达办待两介），成越人的整证书劳们职业技社培训和成越人的整文承举育培训（涉及前如审批的项王达外）；方难：计问乐软件；销售传难难待。（再家禁武和限制的达外，凡涉及置提证制卷的凭证况门）'

run.run('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.woff',word)
>>服务：企业管理，计算机系统服务，电脑动画设计，经济信息咨询服务（除商品中介），成年人的非证书劳动职业技能培训和成年人的非文化教育培训（涉及前置审批的项自除外）；生产：计算机软件；销售自产产品。（国家禁止和限制的除外，凡涉及许可证制度的凭证经营）