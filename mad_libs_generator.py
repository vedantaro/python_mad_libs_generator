#--------------------------------------------------------------------------------------------------------------------------------------
import os 
os.system('cls')
#--------------------------------------------------------------------------------------------------------------------------------------
class kavs_veds():
#--------------------------------------------------------------------------------------------------------------------------------------
    print('\n')

    def story1(self):
        print(f'''one day a boy went to __________ to meet his girlfriend.
But before going to meet her he went to _________ store to buy ______ for her.
Then he visited to her by train & they meet at ___________ station.
He gave ______ for her & hold her hands.
Then they both travelled to _____.''')

        print("\n")
#--------------------------------------------------------------------------------------------------------------------------------------
    def inputs(self):
#--------------------------------------------------------------------------------------------------------------------------------------        
        self.destination=input("enter destination name: ")
        self.store=input("enter food store name: ")
        self.chocolate=input("enter chocolate name: ")
        self.romantic_place=input("enter a romantic place: ")
        print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------        
    def story2(self):
#--------------------------------------------------------------------------------------------------------------------------------------        
        print(f'''one day a boy went to {self.destination} to meet his girlfriend.
But before going to meet her he went to {self.store} store to buy {self.chocolate} for her.
Then he visited to her by train & they meet at {self.destination} station.
He gave {self.chocolate} for her & hold her hands.
Then they both travelled to {self.romantic_place}.''')
#--------------------------------------------------------------------------------------------------------------------------------------
kv=kavs_veds()
kv.story1()
kv.inputs()
kv.story2()
#--------------------------------------------------------------------------------------------------------------------------------------