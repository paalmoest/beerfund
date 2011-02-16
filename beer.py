import time,os
from beerfund.main.models  import BeerAccount, BeerFund
#export PYTHONPATH=/home/paal/workspace/IwantsBeer/src/
#export DJANGO_SETTINGS_MODULE=yoursite.settings
def chargeBeer(rfid):
    try: 
        account = BeerAccount.objects.get(rfid=rfid)
        fund = BeerFund.objects.get(pk=1)
        if account.credits <= 27:
            return "Du har ikke penger nok, skriv: load , i terminalen"      
        account.credits -= 27
        fund.beercount -= 1
        fund.save()
        account.save()
        time.sleep(1)
        return "I charged you 1 beer!  You has %s kronerz left" % account.credits
    except BeerAccount.DoesNotExist:
        return "NO BEER FOR YOU, not REGISTRED :(, type: reg , in terminal."
def deposit(rfid,amount):
    try: 
        account = BeerAccount.objects.get(rfid=rfid)
        account.credits += int(amount)
        account.save()
        time.sleep(1)
        return "You just deposited %s Norwegians kronerz" % amount
    except BeerAccount.DoesNotExist:
        return "NO BEER FOR YOU, not REGISTRED :(, type: reg , in terminal."

def regAccount(rfid,user):
    newAccount = BeerAccount(rfid=rfid,credits="0",user=user)
    newAccount.save()
    return "Gratz  with a beerAccount mr. %s " % user
def loadFund(input):
    fund =  BeerFund.objects.get(pk=1)
    fund.beercount += input
    fund.save()
    return ("You just loaded the beerfund with %s birras!" % input) 

while True:
    pass
    input = raw_input("Welcome to the Beer fund, do something: ")
    if input == "help":
        print "Type:  \n reg ,to register a user \n load to load \n Or swipe your tag/card to buy a beer "
    elif input =="reg":
        rfid = raw_input("Swipe your tag: ")
        user = raw_input("Choose a user name: ")
        print regAccount(rfid,user)
    elif input =="load":
        amount = raw_input("How many $$$ ?: ")
        if amount > "1000":
            print "really? Me don`t like big shots"
        rfid = raw_input("Swipe your tag !: ")  
        print deposit(rfid,amount)
    elif input =="lol":
        os.system('chromium-browser http://www.youtube.com/watch?v=dQw4w9WgXcQ')  
    else:
        try:
            print chargeBeer(input)
        except ValueError:
            print "your argument is invalid !" 