
amount = float(input("Enter order amount: ₹"))
membership = input("Are you a member? (yes/no): ").lower()

if amount < 0 or amount > 100000:
    print("Invalid order amount.")
else:
 
    if amount >= 5000:
        discount_percentage = 15
        eligibility = "Eligible for 15% discount"

    elif membership == "yes" and amount >= 2000 and amount < 5000:
        discount_percentage = 10
        eligibility = "Eligible for 10% discount"

    else:
        discount_percentage = 0
        eligibility = "Not eligible for discount"


    discount_amount = amount * discount_percentage / 100
    final_amount = amount - discount_amount


    print("\n----- Shopping Discount Details -----")
    print("Original Amount: ₹", amount)
    print("Membership:", membership)
    print("Discount Percentage:", discount_percentage, "%")
    print("Discount Amount: ₹", discount_amount)
    print("Final Payable Amount: ₹", final_amount)
    print("Eligibility Status:", eligibility)