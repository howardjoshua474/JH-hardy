import random
Persons=[]
file_path="C:\\Users\\HOWARD JOSHUA\\Desktop\\Users.txt"
Account_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21]
Person={
    "Full name":None,
    "Date of birth" : None,
    "Gender" : None,
    "ID No" : None,
    "Nationality" : None,
    "Email" : None,
    "Phone number" :None,
    "acc_num" :None
}
Person_balance=0
Person_transactions=[]
Person_withdrawals=[]
Person_deposits=[]
Person_transfer=[]
Person_loans=[]
Person_loan_repayments=[]
Person_loan_balance=0
Person_loan_status="No active loan"
Person_loan_limit=50000
Person_loan_interesr_rate=0.05
Person_loan_tenure=None
Person_loan_due_date=None
Person_loan_application_date=None
Person_copy=Person.copy()

def get_info():
    Person["Full name"]=input("Enter your full name:")
    Person["Date of birth"]=input("Enter date of birth(dd/mm/yyyy): ")
    Person["Gender"]=input("Sex(M/F): ")
    Person["ID No"]=input("Input NIN: ")
    Person["Nationality"]=input("Nationality: ")
    Person["Email"]=input("Email(name@gmail.com): ")
    Person["Phone number"]=input("Phone number: ")
    print("Analysing..........!!")
    print("")
    print("Cogratulations!! Your account has been created")
    print(f"Your account number is {get_random_number()}")
    with open(file_path,"a") as file:
        file.write(str(Person)+"\n")
    #Persons.append(Person.copy())
    
def get_random_number():
    selection=random.choice(Account_numbers)
    Person["acc_num"]=selection
    Account_numbers.remove(selection)
    return selection

def Menu():
    print("=====Main menu=====")
    menu=["Create Account","login","Deposit","Withdraw","Check balance","View personal information"]
    for i,num in enumerate(menu,start=1):
        print(f"{i}. {num}")

def login():
    print("welcome to the login page")
    acc_no=int(input("Enter your account number: "))
    if acc_no ==Persons["acc_num"]:
        print("Login successful")
        return True
    else:
        print("incorrect credentials")
        return False

def View_information():
    for key,value in Person.items():
        print(f"{key} : {value}")

def Deposit():
    global Person_balance
    amount=float(input("Enter amount to deposit: "))
    Person_balance +=amount
    Person_deposits.append(amount)
    print(f"Deposit of {amount} successful")
    print(f"Your new balance is {Person_balance}")

def Withdraw():
    global Person_balance
    amount=float(input("Enter amount to withdraw: "))
    if amount>Person_balance:
        print("Insufficient Balance")
    else:
        Person_balance -=amount
        Person_withdrawals.append(amount)
        print(f"Withdrawal of {amount} successful")
        print(f"Your new balance is {Person_balance}")

def Check_balance():
    print(f"Your current balance is {Person_balance}")

def dispense_cash(amount):
    print(f"Dispensing cash: {amount}")
    note_denominations=[50000,20000,10000,5000,2000,1000,500,200,100]
    notes_to_dispense={}
    for note in note_denominations:
        if amount>=note:
            num_notes=amount//note
            notes_to_dispense[note]=num_notes
            amount -=num_notes*note
    print("Please collect your cash .......")
    for note,qty in notes_to_dispense.items():
        print(f"{qty} x {note}")
get_info()








