import pandas as pd
import random as rd
name = ["John Marston", "Arthur Morgan", "Dutch van der Linde", "Sadie Adler", "Bill Williamson", "Micah Bell", "Charles Smith", "Javier Escuella", "Lenny Summers", "Abigail Roberts"]
templates = ["A5A1{}", "B2B3{}", "C3C4{}", "D4D5{}", "E5E6{}", "F6F7{}", "G7G8{}", "H8H9{}", "I9I0{}", "J0J1{}"]
Customer_Acc_id = [template.format(i) for template, i in zip(templates, range(1, 11))]
Customer_Acc_Branch = ["New Austin", "West Elizabeth", "Lemoyne", "New Hanover", "Ambarino", "New Austin", "West Elizabeth", "Lemoyne", "New Hanover", "Ambarino"]
Loan_Amount = [rd.randint(1000, 10000) for _ in range(10)]
Intrest = [rd.uniform(0.05, 0.15) for _ in range(10)]
Amount_Cleared = [Loan_Amount[i] * (1 + Intrest[i]) for i in range(10)]

de = pd.DataFrame(
    {
        "Name": name,
        "Customer_Acc_id": Customer_Acc_id,
        "Customer_Acc_Branch": Customer_Acc_Branch,
        "Loan Details" : Loan_Amount,
        "Intrest": Intrest,
        "Amount_Cleared": Amount_Cleared
    }
)

print(de)