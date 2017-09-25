customer_name = raw_input("Customer's full name:")
num_nights = input("Enter Number of Nights:")
room_service = input("Total room service charge:")
telephone_charge = input("Total telephone charge:")
room_charge = float((num_nights) * 55.0)
entertainment_tax = float((room_charge) * .1)
total = float((room_charge) + (room_service) + (telephone_charge) + (entertainment_tax))
print "River Bend Hotel bill:" , customer_name
print "Total Room Charge:" , num_nights
print "Entertainment Tax:" , entertainment_tax
print "Total Bill:" , total


