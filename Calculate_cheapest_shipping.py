def ground_shipping(weight):
  if weight <= 2 :
    cost = 1.5* weight + 20
    return cost
  elif weight > 2 and weight <= 6 :
    cost = 3.00 * weight + 20
    return cost
  elif weight >6 and weight <= 10 :
    cost = 4.00  * weight + 20
    return cost
  elif weight > 10 :
    cost = 4.75 * weight + 20
    return cost
  
def drone_shipping(weight):
  if weight <= 2 :
    cost = 4.5 * weight 
    return cost
  elif weight > 2 and weight <= 6 :
    cost = 9.00 * weight 
    return cost
  elif weight >6 and weight <= 10 :
    cost = 12.00  * weight 
    return cost
  elif weight > 10 :
    cost = 14.25 * weight 
    return cost

def cheaper():
  weight = float(input ("Enter weight in lbs"))
  gc = ground_shipping(weight)
  dc = drone_shipping(weight)
  if gc < dc and gc < 145 :
    return "Ground Shipping is cheapest. The cost is $" + str(gc)
  elif dc < gc and dc < 145:
    return "Drone Shipping is cheapest. The cost is $" + str (dc)
  else:
    return "Premium Ground Shipping is cheapest. The cost is $" + str(125)
print(cheaper())


