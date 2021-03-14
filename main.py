MENU = {
    "mochaccino": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "americano": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_recource_enough(order_composition):
  for item in order_composition:
    if order_composition[item] > resources[item]:
      print(f"Sorry there is not enough {item}")
      return False
    return True

def count_coins():
  print("Please insert the coins")
  total = int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.10
  total += int(input("How many nickles?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total

def is_transaction_success(money, cost):
  if money >= cost:
    change = round(money - cost, 2)
    print(f"Here is {change} in change")
    global profit
    profit += cost
    return True
  else:
    print("Sorry, not enough money")
    return False

def serve_coffe(name, composition):
  for item in composition:
    resources[item] -= composition[item]
  print(f"Here is your {name}")

is_machine_on = True

while is_machine_on:
  selected = input("What coffe you like? (mochaccino/latte/americano)")
  if selected == "off":
    is_machine_on = False
  elif selected == "report":
    print(f"Water = {resources['water']}")
    print(f"Milk = {resources['milk']}")
    print(f"Coffee ={resources['coffee']}")
    print(f"Money = ${profit}")
  else:
    ordered = MENU[selected]
    if is_recource_enough(ordered["ingredients"]):
      payment = count_coins()
      if is_transaction_success(payment, ordered['cost']):
        serve_coffe(selected, ordered['ingredients'])