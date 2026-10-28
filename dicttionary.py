sales_reps = [
    {"name": "Alice", "revenue": 142000.0},
    {"name": "Bob", "revenue": 68000.0},  
    {"name": "Charlie", "revenue": 35000.0}
    ]

for s in sales_reps:
    if s["revenue"] >= 100000.0: 
        commission_payouts= s["revenue"] *0.12
    elif s["revenue"] >= 50000.0:
        commission_payouts = s["revenue"] * 0.08
    else:
        commission_payouts = s["revenue"] * 0.05

    print("commission_payout", commission_payouts)
