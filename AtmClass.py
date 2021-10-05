class Atm:
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber=atmCardNumber
        self.pinNumber=pinNumber
   


    def BalanceEnquiry(self):
        print('Your Balance Is 207857')

    def cashWithdrawl(self,amount):
      newAmount = 207857 - amount
      print('This Is The Amount You Withdrawd'+str(amount)+'. Remaing Money In The Account Is '+str(newAmount))


def user():
        cardNumber=input('Insert Your Credit Card Number : ')
        pinNumber=input('Insert Your Credit Card Pin Number : ')

        user=Atm(cardNumber,pinNumber)

        print('Choose What You Want To do In The Atm Machine')
        print('eneter 1 for Balance Enquiry And 2 for Cash Withdrawl')

        action=int(input('Enter The Number From Above To Choose What You Want To Do : '))

        if(action==1):
            user.BalanceEnquiry()
        elif(action==2):
            amount=int(input('Enter The Amount You Want To Withdraw : '))
            user.cashWithdrawl(amount)
        else:
            print('Please Enter The Same Number From Above Message')


if __name__=="__main__":
      user()



    