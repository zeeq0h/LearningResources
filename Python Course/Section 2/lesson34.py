cars = ["ok", "ok", "ok", "ok", "ok"]
#insert a false into the dict and it will not print the final message

for status in cars:
    if status == "faulty":
        print("stopping the production line")
        break
    print(f"this car is {status}")
    print("shipping new car to customer")
else:
    print("All cars built successfully. no faulty cars!")