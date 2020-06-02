# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

# If wish to speed up payments by paying extra
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    # Pay extra if months is in extra payments period
    if extra_payment_start_month <= months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        if not principal > 0:
            break
        total_paid += payment + extra_payment
    else:
        principal = principal * (1 + rate / 12) - payment
        if not principal > 0:
            break
        total_paid += payment
    months += 1
    print(f"{months} {round(total_paid, 2)} {round(principal, 2)}")

print(f"Total paid: {round(total_paid, 2)}")
print(f"Months {months}")
