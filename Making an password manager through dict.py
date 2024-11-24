password={}
account1=(input("Enter your application you want to set password ,eg Facebook,Whatsapp,Instagram,twitter"))
password1=(int(input(f"Enter your {account1} password")))
password[account1]=password1
account2=(input("Enter your application you want to set password ,eg Facebook,Whatsapp,Instagram,twitter"))
password2=(int(input(f"Enter your {account2} password")))
password[account2]=password2
account3=(input("Enter your application you want to set password ,eg Facebook,Whatsapp"))
password3=(int(input(f"Enter your {account3} password")))
password[account3]=password3
print("Your all account with password is saved in dictionary:")
print(f"{account1}:{password[account1]}")
print(f"{account2}:{password[account2]}")
print(f"{account3}:{password[account3]}")