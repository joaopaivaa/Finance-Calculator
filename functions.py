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
    
    # Calculate the fixed installment (PMT)
    payment = principal * rate / (1 - (1 + rate) ** -periods)
    balance = principal

    print(f"{'Period':<8}{'Payment':<12}{'Interest':<12}{'Principal':<12}{'Balance':<12}")
    
    for period in range(1, periods + 1):
        interest = balance * rate
        principal_payment = payment - interest
        balance -= principal_payment
        print(f"{period:<8}{payment:<12.2f}{interest:<12.2f}{principal_payment:<12.2f}{balance:<12.2f}")


def sac_amortization(principal, rate, periods):

    # Calculate constant amortization
    amortization = principal / periods
    balance = principal

    print(f"{'Period':<8}{'Payment':<12}{'Interest':<12}{'Amortization':<12}{'Balance':<12}")
    
    for period in range(1, periods + 1):
        interest = balance * rate
        payment = amortization + interest
        balance -= amortization
        print(f"{period:<8}{payment:<12.2f}{interest:<12.2f}{amortization:<12.2f}{balance:<12.2f}")
