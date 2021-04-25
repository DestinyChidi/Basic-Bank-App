# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

# Initializing the system
import random
import validation
import database
from getpass import getpass


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password);

        if user:
            bank_operation(user)

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation(user)
    elif selected_option == 2:

        withdrawal_operation(user)
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    print("Withdrawal")

    print("Your current Balance is: %s" % str(get_current_balance(user)))
    withdrawal_amount = int(input("How much do you want to withdraw? \n"))

    if withdrawal_amount <= int(get_current_balance(user)):
        balance_after_withdrawal = int(get_current_balance(user)) - int(withdrawal_amount)
        print("You Successfully Withdrawn %s" % str(withdrawal_amount))
        print("And your Balance is %s" % str(balance_after_withdrawal))
    else:
        print("Sorry, Insufficient Balance")
        bank_operation(user)


def deposit_operation(user):
    print("Deposit Operations")

    print("Your current Balance is: %s" % str(get_current_balance(user)))
    deposit_amount = int(input("How much do you want to deposit? \n"))

    balance_after_deposit = int(get_current_balance(user)) + int(deposit_amount)
    print("You Successfully Deposited %s" % str(deposit_amount))
    print("And your Balance is %s" % str(balance_after_deposit))

    bank_operation(user)


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()
