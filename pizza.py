# pizza.py

no_of_pizza = eval(input("how much pizza you want?  ") )
cost_of_pizza = eval(input("cost for each pizza?  ") )
total_cost_of_each_pizza = no_of_pizza * cost_of_pizza
tax = total_cost_of_each_pizza * 8 /100
print("Total cost of pizza = ", tax + total_cost_of_each_pizza)

