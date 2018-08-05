
from GoogleSearch import GoogleSearch
gs=GoogleSearch()

class HelloWorld:



    def __init__(self):
        print("hello world class")


    def getHelloWorlds(self,key):
        sarchQuery=key+" Hello World program"
        helloWorlds=gs.search(sarchQuery,3)
        return helloWorlds




# hw=HelloWrold()
# print(hw.getHelloWorlds('java'))
