def simple_interest(amount: float = None, principal: float = None, rate: float = None, time: int = None):

    if amount is None:
        amount = principal + (principal * rate * time)
        return amount
    
    elif principal is None:
        principal = (amount - principal) / (rate * time)
        return principal
    
    elif rate is None:
        rate = (amount - principal) / (principal * time)
        return rate
    
    elif time is None:
        time = (amount - principal) / (rate * principal)
        return time


def compound_interest(amount: float = None, principal: float = None, rate: float = None, time: int = None):
    
    import math

    if amount is None:
        amount = principal * ((1 + rate) ** time)
        return amount

    if principal is None:
        principal = amount / ((1 + rate) ** time)
        return principal

    if rate is None:
        rate = (amount / principal) ** (1 / time) - 1
        return rate

    if time is None:
        time = math.log(amount / principal) / math.log(1 + rate)
        return time
    

def present_value(future_value: float = None, projected_inflation_rate: float = None, time: float = None):

    present_value = future_value / ((1 + projected_inflation_rate) ** time)
    return present_value


def french_amortization(principal, rate, periods):
    
    import pandas as pd 

    # Calculate the fixed installment (PMT)
    payment = principal * rate / (1 - (1 + rate) ** -periods)
    balance = principal

    df = pd.DataFrame(columns=['Period','Payment','Interest','Principal','Balance'])
    new_line = pd.DataFrame({'Period': [0],
                         'Payment': [''],
                         'Interest': [''],
                         'Principal': [''],
                         'Balance': ['']})
    df = pd.concat([df, new_line], ignore_index=True)

    # print(f"{'Period':<8}{'Payment':<12}{'Interest':<12}{'Principal':<15}{'Balance':<12}")
    # print(f"{0:<8}{'-':<12}{'-':<12}{'-':<12}{balance:<15.2f}")

    for period in range(1, periods + 1):
        interest = balance * rate
        principal_payment = payment - interest
        balance -= principal_payment
        new_line = pd.DataFrame({'Period': [round(period, 2)],
                                 'Payment': [round(payment, 2)],
                                 'Interest': [round(interest, 2)],
                                 'Principal': [round(principal_payment, 2)],
                                 'Balance': [round(balance, 2)]})
        df = pd.concat([df, new_line], ignore_index=True)

        # print(f"{period:<8}{payment:<12.2f}{interest:<12.2f}{principal_payment:<15.2f}{balance:<12.2f}")
    
    print(df)


def sac_amortization(principal, rate, periods):

    import pandas as pd

    # Calculate constant amortization
    amortization = principal / periods
    balance = principal

    df = pd.DataFrame(columns=['Period','Payment','Interest','Principal','Balance'])
    new_line = pd.DataFrame({'Period': [0],
                         'Payment': [''],
                         'Interest': [''],
                         'Principal': [''],
                         'Balance': ['']})
    df = pd.concat([df, new_line], ignore_index=True)

    # print(f"{'Period':<8}{'Payment':<12}{'Interest':<12}{'Amortization':<15}{'Balance':<12}")
    # print(f"{0:<8}{'-':<12}{'-':<12}{'-':<15}{balance:<12.2f}")

    for period in range(1, periods + 1):
        interest = balance * rate
        payment = amortization + interest
        balance -= amortization
        new_line = pd.DataFrame({'Period': [round(period, 2)],
                                 'Payment': [round(payment, 2)],
                                 'Interest': [round(interest, 2)],
                                 'Principal': [round(amortization, 2)],
                                 'Balance': [round(balance, 2)]})
        df = pd.concat([df, new_line], ignore_index=True)

        # print(f"{period:<8}{payment:<12.2f}{interest:<12.2f}{amortization:<15.2f}{balance:<12.2f}")

    print(df)