def account_number_validation(account_number):
    if account_number:

        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False


def withdrawal_check(withdrawal_amount):
    if withdrawal_amount:

        try:
            int(withdrawal_amount)

        except ValueError:
            return False
        except TypeError:
            return False

    return False
