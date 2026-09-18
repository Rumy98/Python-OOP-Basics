class BankAccount:
    def __init__(self,owner):
        self.owner=owner
        self._balance=0

    @property#
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,new_balance):
        self._balance=new_balance


a=BankAccount("Rumy")
a.balance=50
print(a.balance)
        