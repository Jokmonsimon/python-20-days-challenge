# Conditional Statements

phone_balance = 400
bank_balance = 100000

print("You have UGX {} in your phone and UGX {} in your bank acount.".format(phone_balance, bank_balance))

if phone_balance < 500:
    phone_balance += 1000
    bank_balance -= 1000

print("Hello Customer, currently you have UGX {} in your phone and UGX {} in your bank acount.".format(phone_balance, bank_balance))