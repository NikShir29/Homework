salary = int(input())
debtBank = int(input())
debtServices = int(input())

cleanMoney = (salary - debtBank - debtServices)
print(cleanMoney)