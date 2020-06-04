""" file = open("newfile.txt","w")
file.write("This is my new file")
file.close()

file = open("newfile.txt","r")
print(file.read())
file.close() """

"""msg = "Hello World"
file = open("newfile.txt","w")
amount_written = file.write(msg)
print(amount_written)
file.close() """

'''try:
    f = open("newfile.txt")
    print(f.read())
finally:
    f.close()'''

'''def ground_shipping(weight):
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
  
print(ground_shipping(8.4))'''


def ground_shipping(weight):
  if int(weight) <= 2 :
    cost = 1.5* weight + 20
    return cost
  elif int(weight)> 2 and int(weight) <= 6 :
    cost = 3.00 * weight + 20
    return cost
  elif int(weight) >6 and int(weight) <= 10 :
    cost = 4.00  * weight + 20
    return cost
  elif int(weight) > 10 :
    cost = 4.75 * weight + 20
    return cost
  
def drone_shipping(weight):
  if int(weight) <= 2 :
    cost = 4.5 * weight 
    return cost
  elif int(weight) > 2 and  int(weight) <= 6 :
    cost = 9.00 * weight 
    return cost
  elif  int(weight) and  int(weight) <= 10 :
    cost = 12.00  * weight 
    return cost
  elif  int(weight) > 10 :
    cost = 14.25 * weight 
    return cost

def input_shipping():
  premium_ground_shipping = 145
  value = input("Enter the weight in lbs : ")
  ground_cost = ground_shipping(value)
  drone_cost = drone_shipping(value)
  if ground_cost < drone_cost and ground_cost <  premium_ground_shipping :
    return "The ground shipping is the cheapest"
  elif drone_cost < ground_cost and drone_cost < premium_ground_shipping:
    return "The drone shipping is the cheapest"
  else:
    return "The premium ground shipping is the cheapest"


input_shipping()


