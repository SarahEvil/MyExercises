#ascribes the value 100 to the variable cars
cars = 100
#ascribes the value 4.0 to the variable space in a car
space_in_a_car = 4.0
#s.o.
drivers = 30
#s.o.
passangers = 90
#substracts 30 from 90 to acribe to the variable cars not driven
cars_not_driven = cars - drivers
#acribes the same value as drivers to cars driven
cars_driven = drivers
#multiplies cars driven with space in car
carpool_capacity = cars_driven * space_in_a_car
#s.o.
average_passengers_per_car = passangers/ cars_driven


#prints text, gives value of variable, prints text
print "There are", cars, "cars available."
#s.o.
print "There are only", drivers, "drivers available."
#so.o
print "There will be", cars_not_driven, "empty cars today."
#s.o.
print "We can transport", carpool_capacity, "people today."
#s.o.
print "We have", passangers, "to carpool today."
#s.o.
print "We need to put about", average_passengers_per_car, "in each car."


