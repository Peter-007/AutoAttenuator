import RPi.GPIO as GPIO

'''
管脚定义：
            Raspberry
衰减器1   GPIO_Name   PIN
  1蓝 -----	GPIO.0	 11
  2橙 -----	GPIO.1	 12
  3绿 -----	GPIO.2	 13
  4棕 -----	GPIO.3	 15
  5灰 -----	GPIO.4	 16
  6白 -----	GPIO.5	 18
  7红 -----	GPIO.29	 40
  8黑 -----		
  9黄 -----	5V	    2
 10紫 -----  0V  	6
  
衰减器2   GPIO_Name  PIN
 1蓝 ----- GPIO.22  31
 2橙 ----- GPIO.23	33
 3绿 ----- GPIO.24	35
 4棕 ----- GPIO.25	37
 5灰 ----- GPIO.26	32
 6白 ----- GPIO.27	36
 7红 ----- GPIO.28	38
 8黑 -----
 9黄 ----- 5V    	4
10紫 ----- 0V    	39
'''

class ATT(object):

    # AttNumber: 可编程衰减器模块序号，本系统是有两个模块，分别为1和2
    def __init__(self,AttNumber):
        Pins=((40,18,16,15,13,12,11),(38,36,32,37,35,33,31))    #定义管脚列表，为了便于同二进制的高地位顺序匹配，按管脚序号有大到小进行定义
        self.listPin = Pins[AttNumber-1]    #获取指定可编程衰减器模块序号的管脚列表，用于SetAtt函数

        # 初始化树莓派gpio接口
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.listPin,GPIO.OUT)
        GPIO.output(self.listPin,0)     #将可编程衰减器的所有管脚电平设为低，得到最大衰减值63.5dB
    
    def __del__(self):
        GPIO.cleanup()

    # Val: 期望设置的衰减值，需要是0.5的倍数
    def SetAtt(self,Val):
        n=int(round(Val*2))     #可编程衰减器的步进是0.5dB,也即实现1dB的衰减，对应的管脚二进制值应该是2
        strBin='{:07b}'.format(n)   #转换程7个bit位的二进制字符串
        listVal = [not bool(int(x)) for x in strBin]  #可编程衰减器是低电平有效，故而对每个bit位取反
        GPIO.output(self.listPin,listVal)   #将转换后的二进制列表值同时配置给可编程衰减器所有7个管脚

if __name__ == '__main__':
    att1 = ATT(1)
    att1.SetAtt(10)

