class fireAlerm:                                #Defining a Class

    def fireDetect(self):                       #Function for Detect Fire
        pinFlameGPIO=7
        pinGreenLed=11
        pinRedLed=13
        GPIO.setup(pinGreenLed,GPIO.OUT)
        GPIO.setup(pinRedLed,GPIO.OUT)
        GPIO.setup(pinFlameGPIO,GPIO.IN)
        GPIO.output(pinRedLed,0)
        while True:

            GPIO.output(pinRedLed,1)
            if (GPIO.input(7))==0:              #For Red  LED Light Turns on doing an Operation
                print "Fire detected"
                print "Mail sending.....\n"
                GPIO.output(pinGreenLed,1)
                GPIO.output(pinRedLed,0)
                self.mailSend()


            else:                               #For Green  LED Light Turns on doing an Operation 
                print "Fire not detected"
                time.sleep(1)
                GPIO.output(pinGreenLed,1)
                time.sleep(1)
                GPIO.output(pinGreenLed,0)



    #This Function sends alert mail
    #Reference: http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
    def mailSend(self):

        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mailFrom='remotefireservice@gmail.com'
        mailPassword='AOS01712918315'
        mail.login(mailFrom,mailPassword)
        mailTo='abid.bgd@gmail.com'
        mailBody="Fire detected"
        mail.sendmail(mailFrom,mailTo,mailBody)
        mail.close()
        time.sleep(10)



#Loading Library
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
import time
import smtplib



_fireAlerm=fireAlerm()
_fireAlerm.fireDetect()
