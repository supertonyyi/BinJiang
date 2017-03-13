class MyClass(object):
    def __init__(self,nm,ph):
        self.name=nm
        self.phone=ph

    def FakePrint(self):
        print 'You invoked Fakeprint()!'

    def showInfor(self):
        print ('My name is:%s,My phone number is:%s'%(self.name,self.phone))

    def UpdatePhone(self,newph):
        self.phone=newph
        print 'Phone number updated for:%s'%self.name

class SonOfMyClass(MyClass):
    def __init__(self,nm,ph,id,mail):
        MyClass.__init__(self,nm,ph)
        self.Eid=id
        self.Email=mail

    def UpdateMail(self,newMail):
        self.Email=newMail

    def showInfor(self):
        print self.name,self.phone,self.Eid,self.Email

    def __str__(self):
        return str(self.__dict__)

if __name__=="__main__":
    thisClass=MyClass('Jack','123')
    thisClass.showInfor()
    thisClass.UpdatePhone('456')
    thisClass.showInfor()

    sonClass=SonOfMyClass('Herry','456','1111','herry@163.com')
    sonClass.showInfor()

    print dir(MyClass)
    print MyClass.__dict__
    print'----------------------------'
    print sonClass.__str__()


