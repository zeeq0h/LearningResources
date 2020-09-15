cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("found faulty car, skipping...")
        continue #this skips the faulty car and goes to the next one, break would fully stop the loop at the faulty car
    print(f"this car is {status}")
    print("shipping new car to customer!")

    
