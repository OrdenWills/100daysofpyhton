cars=100#number of drivers are hundred
space_in_car=4.0
drivers=30
passengers=90
cars_not_driven= cars - drivers
cars_driven= drivers
carpool_capacity=cars_driven * space_in_car
average_passengers_per_car=passengers / cars_driven
drivers=passengers#here number of drivers is equal to number of passangers
print("there are cars", cars, "cars available.")
print("there are only", drivers, "drivers available.")
print("there will be", cars_not_driven,"empty cars today.")
print("we can transport", carpool_capacity, "people today.")
print("we have", passengers, "to carpool today.")
print("we need to put about",average_passengers_per_car,"in each car")
print("is it true that drivers < passengers ?")
print(" it's ", drivers < passengers)
print("what is 30 - 5 * 3? ")
print(30 - 5 * 3)