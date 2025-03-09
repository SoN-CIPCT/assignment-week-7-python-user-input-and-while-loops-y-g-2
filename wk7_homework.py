#for 4: once pizza is made, delete it from pizza_orders and add it to finished_pizzas

#new pizza orders:
pizza_orders = ['pepperoni', 'cheese', 'meat lover', 'veggie delight']

finished_pizzas = []

#loop
for pizza in pizza_orders[:]:
    print(f"Your {pizza} pie is finished!")
    finished_pizzas.append(pizza)
    pizza_orders.remove(pizza)

#all pizzas are done:
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")