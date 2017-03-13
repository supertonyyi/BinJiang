import logging
class UpdateData(object):
    def __init__(self,stock_id,high,low,date):
        self.myStockId=stock_id
        self.myHigh=high
        self.myLow=low
        self.myDate=date

    def updatePrice(self):
        self.myHigh=self.myHigh*10
        self.myLow=self.myLow*10
        stockDic={'Stock_id':self.myStockId,'High':self.myHigh,'Low':self.myLow,'Date':self.myDate}
        logging.error(stockDic)
        return  stockDic


if __name__=="__main__":
    thisData=UpdateData('60030',10.4,20.9,'20160415')
    print thisData.updatePrice()

