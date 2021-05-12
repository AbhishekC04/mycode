fruitbowl = ["carrot", "tomato", "beans"]
for fruit in fruitbowl:
        print(fruit)
fruitfile = open("fruitfile.txt","a")
for fruit in fruitbowl:
	    print(fruit, file=fruitfile)
fruitfile.close()

fruitbowl = ["cherry", "orange", "apple"]
for fruit in fruitbowl:
        print(fruit)
fruitfile = open("fruitfile.txt","w")
for fruit in fruitbowl:
            print(fruit, file=fruitfile)
fruitfile.close()
