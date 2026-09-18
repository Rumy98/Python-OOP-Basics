class BankAccount:
    def __init__(self,owner,num):
        self.owner=owner
        self.num=num

    @staticmethod
    def is_num_valid(n):
        if len(n)==11:
            return True
        else:
            return False

print(BankAccount.is_num_valid("12345678902"))