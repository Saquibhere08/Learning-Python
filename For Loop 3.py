#Print all the key value-pairs in the dictionary
capitals={"USA":"New York","France":"Paris","Japan":"Tokoyo","India":"New Delhi"}
for country,city in capitals.items():
    print("The Capitals of {} is {}.".format(country,city))
    