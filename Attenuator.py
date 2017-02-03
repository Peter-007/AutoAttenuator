import RPi.GPIO as GPIO
import time

class ATT(object):
    
    def __init__(self,AttNumber):
        Pins=((40,18,16,15,13,12,11),(38,36,32,37,35,33,31))
        self.listPin = Pins[AttNumber-1]
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.listPin,GPIO.OUT)
        GPIO.output(self.listPin,0)
        GPIO.setup(22,GPIO.IN)
        GPIO.setup(29,GPIO.OUT)
        GPIO.output(29,1)
    
    def __del__(self):
        GPIO.cleanup()

    def SetAtt(self,Val):
        n=int(round(Val*2))
        strBin='{:07b}'.format(n)
        listVal = [not bool(int(x)) for x in strBin]
        #print Val,n,listVal
        GPIO.output(self.listPin,listVal)
        
    def AutoAtt(self,start=0,stop=30,step=3,delay=1,repeattimes=1):
        bStop = False
        for j in range(repeattimes):
            print('Repeat times: %d/%d' % (j+1,repeattimes))
            for i in range(int(start),int(stop+step),int(step)):
                bStop = self.IsStart()
                if bStop:
                    return
                self.SetAtt(i)
                time.sleep(delay)   #Unit:second
                
    def Blink(self,pin):
        GPIO.setup(pin,GPIO.OUT)
        for i in range(10):
            GPIO.output(pin,not GPIO.input(pin))
            time.sleep(0.5)
            
    def IsStart(self):
        return GPIO.input(22)
        


if __name__ == '__main__':
    
    print('AutoAtt Start ' + time.strftime('%H:%M:%S',time.localtime()))

    att1 = ATT(1)
    print(att1.IsStart())
    att1.AutoAtt(63,0,-1,0.05,1000)
    del att1    

    print('AutoAtt End ' + time.strftime('%H:%M:%S',time.localtime()))


