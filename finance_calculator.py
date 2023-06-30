import math
#Program is to build intrest calcultor for both investments and loans
#INVESTMENT = "Intrest earned on the deopist "
#BOND = "Intrest to pay for the home loan"

print("Welcome! to the intrest calculator")
Response = input("To calculate the intrest on your deposit, please type 'Investment' OR type 'Bond' to calculate the intrest you will pay for the home loan : ")

#to ensure the input is readale irrespective of case in which input is given we will standesise the input 
res = Response.upper()
print ("your have selected " + res + ".")

# First to calculte the intrest on deposit
if res == "INVESTMENT":
    print ("To calculate the intrest on your deposit, please enter the below details.")
    invest_amt=int(input("Please enter the amount you would like to invest: "))
    invest_intrst=float(input("Please input the intrest rate (Note: Please enter numerical value only): ")) #float is used to get the values in decimals
    Actual_invest_intrst = invest_intrst/100 #As we nned to convert the percentage to decimal 
    invest_prd=int(input("Please enter the number of years you want to invest: "))
    
    #User has option to calculate both Simple and compound intrest
    interest_type= input("Please enter the type of intrest you want to clalculate 'Simple' or 'Compound': ")
    intrst_typ= interest_type.upper() #standerzing the input

    if intrst_typ == "SIMPLE":
        print("you have selected SIMPLE interest")
        total_si_amt = invest_amt*(1+Actual_invest_intrst*invest_prd) #formual to calculate total amount receivable including simple interest
        simple_intrst = total_si_amt - invest_amt #to calculate simple interst amount only  
        print("you will accumulate £ " + str(simple_intrst) + " as simple intrest during the invested period")
        print("With interest you will receive total amount of £ " + str(total_si_amt) + " , if you deposit £ " + str(invest_amt) + " for " + str(invest_prd) +  " years at the intrest rate " + str(invest_intrst) + "%.")
    elif intrst_typ == "COMPOUND":
        print("you have selected COMPOUND interest")
        total_ci_amt = invest_amt*math.pow((1+Actual_invest_intrst),invest_prd)#formual to calculate total amount receivable including compound interest
        compound_intrst = total_ci_amt - invest_amt #to calculate simple interst amount only 
        print("you will accumulate £ " + str(compound_intrst) + " as compound intrest during the invested period")
        print("With interest you will receive total amount of £ " + str(total_ci_amt) + " , if you deposit £ " + str(invest_amt) + " for " + str(invest_prd) +  " years at the rate of intrest " + str(invest_intrst) + "%.")
    else:
        print("Invalid input, Please enter either 'Simple' or 'Compound' to calculate the interest")
  
#To calculate the intrest on the loan
elif res == "BOND":
    print ("To calculate the intrest your bond, please enter the below details.")
    hom_Val = int(input("Please enter value of the home: "))
    loan_intrst = float(input("Please input the intrest rate (Note: Please enter numerical value only): "))
    actual_loan_intrst = (loan_intrst/100)/12 #to convert percentage to decimal and further to calculate for every month
    pay_period = int(input("Please enter the number of months in which you would like to repay:  "))
    total_payable = (actual_loan_intrst * hom_Val) / (1 - (1+actual_loan_intrst)** (-pay_period)) #formual to calculate total amount payable with interest
    print("Every month you will have to pay an amount of £ " + str(total_payable) + " , if you avali £ " + str(hom_Val) + " loan for " + str(pay_period) + " months at the intrest rate of " + str(loan_intrst) + "%.")

else: #ensure the right input is given
    print("Invalid input, please enter either 'INVESTMENT' or 'BOND'")