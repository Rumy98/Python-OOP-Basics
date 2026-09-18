class BankAccount:
    send_fee=10
    @classmethod
    def update_sf(cls,sf):
        cls.send_fee=sf

a=BankAccount()
print(a.send_fee)
a.update_sf(20)
print(a.send_fee)