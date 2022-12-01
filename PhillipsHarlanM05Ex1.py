# Show individually the 5 purchases amounts, compute the state and county sales
# tax on those combined  purchases and calculate the total of taxes
# and purchases
def calculateCountyTax(price):
    county_sales_tax =  .025
    return price * county_sales_tax
def calculateStateTax(price):
    state_sales_tax = .05
    return price * state_sales_tax
# Enter the purchase price
def main():
    price = float(input('Enter the price of the purchase: '))
    displayTotals(price)
# Calculate the purchase price with the coounty and state sales tax
def calculate_totals(purchase):
  county_sales_tax = purchase * .025 
  state_sales_tax = purchase * .05
  total_sales_tax = county_sales_tax + state_sales_tax
  total_price = purchase + state_sales_tax + county_sales_tax
# display the amount of the purchases, county and state sales
# taxes, combined amount of the both taxes and total sale with taxes
def displayTotals(price):
    print('Original price', price)
    state_tax = calculateStateTax(price)
    print('State tax', state_tax)
    county_tax = calculateCountyTax(price)
    print('County tax', county_tax)
    print('Total', price + state_tax + county_tax)
# Call the main function
main()