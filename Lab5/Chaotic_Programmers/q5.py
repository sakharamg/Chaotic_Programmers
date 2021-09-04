class BlackMoneyHolder:
    ## write your code here
    def __init__(self,name,accounts_info):
        """
	name-a string - the name of the corrupt person (must throw an exception if the name is not a string is None, or is an empty string) 
        accounts_info - a dictionary with key=bank name and value=amount of black money
	"""
        if(type(name) != str):
            raise Exception('Should pass a string')
        if(type(accounts_info) != dict):
            raise Exception('Should pass a dictionary')
        self.name = name
        self.accounts = accounts_info
    
    def update_amount(self,bank_name,amount):

        """
	input
	    bank_name-This will take the name of the account as input
	    amount-This will take the amount as input
        """
        self.accounts[bank_name] = amount
        # if(bank_name in self.accounts):
        #     self.accounts[bank_name] = amount
        # else:
        #     self.accounts

    def total_black_money(self):
        """
	returns the total amount of black money a person currently has in all his accounts combined.

        """
        sum = 0
        for amount in self.accounts.values():
            sum += amount
        return sum

    def __lt__(self, other_black_money_holder):
        return self.total_black_money() < other_black_money_holder.total_black_money()

    def __eq__(self, other_black_money_holder):
        return self.total_black_money() == other_black_money_holder.total_black_money()

    def __len__(self):
        return len(self.accounts)

    def __getitem__(self, key):
        if( key >= 0 and key < len(self) ):
            sorted_acts = sorted(self.accounts)
            bank_name = sorted_acts[key]
            amount = self.accounts[bank_name]
            return (bank_name, amount)
            # return tuple(self.accounts.items())[key]
        else:
            raise IndexError

    def __str__(self):
        sorted_acts = sorted(self.accounts)
        s =''
        for bank_name in sorted_acts:
            curr_detail = bank_name + ': '+ str(self.accounts[bank_name]) + '\n'
            s += curr_detail
        return s[:-1]


if __name__ == "__main__":
    """Main function
    """
    
