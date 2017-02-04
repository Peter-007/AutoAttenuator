# AutoAttenuator
Auto set two attenuators
# 简介
* 使用树莓派软硬件，控制上海华湘的可编程衰减器(型号：GTKS1-7-63.5-6-HD）。
* 本软件设计了一个简洁的界面，用户通过GUI可实时改变衰减值，并可配置合适的参数，按照一定的步骤自动步进式改变衰减值。

#软件配置
* PyQt5 (sudo apt-get install python3-PyQt5  or sudo apt-get install python-PyQt5)
* Rpi.GPIO

# 硬件配置
* 树莓派3 有40pin GPIO
* 管脚定义：

|Attenuator-1|Raspberry GPIO|
|------------|--------------|
|1|11|
|2|12|
|3|13|
|4|15|
|5|16|
|6|18|
|7|40|
|8|empty|
|9|2|
|10|6|

|Attenuator-2|Raspberry GPIO|
|------------|--------------|
|1|31|
|2|33|
|3|35|
|4|37|
|5|32|
|6|36|
|7|38|
|8|empty|
|9|4|
|10|39|
