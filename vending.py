# Author   : Xuan Thien Bui
# Email    : xuanthienbui@umass.edu
# Spire ID : 34750117
class VendingMachine:
    def __init__(self):
        self.inventory={}
        self.balance=0
        self.sales=0
        self.total_sales=[]
        self.lst={}
        self.lists=[]
    def add_item(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        if(self.name in self.inventory):
            self.inventory[self.name][1]+=self.quantity
        else:
            self.inventory[self.name]=[self.price,self.quantity]
        print(f"{self.quantity} {self.name}(s) added to inventory")
        if(self.name in self.inventory):
            self.inventory[self.name][0]=self.price
        else:
            self.inventory[self.name]=self.price
    def get_item_price(self,name):
        self.name=name
        if(self.name in self.inventory):
            return self.inventory[self.name][0]
        else:
            print("Invalid item")
            return None
    def get_item_quantity(self,name):
        self.name=name
        if(self.name in self.inventory):
            return self.inventory[self.name][1]
        else:
            print("Invalid item")
            return None
    def list_items(self):
        if(len(self.inventory)==0):
            print(f"No items in the vending machine")
        else:
            sorted_inventory=sorted(self.inventory)
            print("Available items:")
            for item in sorted_inventory:
                print(f"{item} (${self.inventory[item][0]}): {self.inventory[item][1]} available")
    def insert_money(self,dollar_amount):
        self.dollar_amount=dollar_amount
        if(dollar_amount==1.0 or dollar_amount==2.0 or dollar_amount==5.0):
            self.balance+=self.dollar_amount
            print(f"Balance: {round(self.balance,2)}")
        else:
            print(f"Invalid amount")
    def purchase(self,name):
        self.name=name
        if(self.name not in self.inventory):
            print(f"Invalid item")
        else:
            if(self.inventory[self.name][1]==0):
                print(f"Sorry {self.name} is out of stock")
            else:
                if(self.balance<self.inventory[self.name][0]):
                    print(f"Insufficient balance. Price of {self.name} is {self.inventory[self.name][0]}")
                else:
                    self.lists.append(self.name)
                    self.total_sales.append((self.name, self.inventory[self.name][0]))
                    self.inventory[self.name][1]-=1
                    self.balance-=self.inventory[self.name][0]
                    print(f"Purchased {self.name}")
                    print(f"Balance: {round(self.balance,2)}")
                    self.sales+=self.inventory[self.name][0]
                    self.sales=round(self.sales,2)
    def output_change(self):
        if(self.balance>0):
            print(f"Change: {self.balance}")
            self.balance=0.0
        elif(self.balance==0):
            print(f"No change")
    def remove_item(self,name):
        self.name=name
        if(self.name not in self.inventory):
            print(f"Invalid item")
        else:
            del self.inventory[self.name]
            print(f"{self.name} removed from inventory")
    def empty_inventory(self):
        self.inventory.clear()
        print(f"Inventory cleared")
    def get_total_sales(self):
        return self.sales
    def stats(self,N):
        if(len(self.lists)==0):
            print(f"No sale history in the vending machine")
        else:
            if(len(self.lists)<=N):
                print(f"Sale history for the most recent {len(self.lists)} purchase(s):")
                for i in range(len(self.total_sales)):
                    if(self.total_sales[i][0] not in self.lst):
                        self.lst[self.total_sales[i][0]]=self.total_sales[i][1]
                    else:
                        self.lst[self.total_sales[i][0]]+=self.total_sales[i][1]
                sorted_list=sorted(self.lst)
                for item in sorted_list:
                    print(f"{item}: ${self.lst[item]} for {self.lists.count(item)} purchase(s)")
            elif(len(self.lists)>N):
                print(f"Sale history for the most recent {N} purchase(s):")
                count=[]
                j=len(self.total_sales)-1
                while(j>0):
                    count.append(self.total_sales[j][0])
                    if(self.total_sales[j][0] not in self.lst):
                        self.lst[self.total_sales[j][0]]=self.total_sales[j][1]
                    else:
                        self.lst[self.total_sales[j][0]]+=self.total_sales[j][1]
                    if(len(count)==N):
                        break
                    j-=1
                sorted_list=sorted(self.lst)
                for item in sorted_list:
                    print(f"{item}: ${self.lst[item]} for {count.count(item)} purchase(s)")


            




        

