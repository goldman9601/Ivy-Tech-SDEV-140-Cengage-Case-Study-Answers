# base bill amount
basebill = float(input("Enter amount of bill: "))
# amount tip
tip = basebill*.18
# amount tax
tax = basebill*.07
# Totals mathed out
totalbill = basebill+tip+tax
# Printed Total
print ("Base Bill total %.2f" %basebill)
print ("Tip Amount %.2f" %tip )
print ("Tax total %.2f" %tax)
print ("Total Amount %.2f" %totalbill)