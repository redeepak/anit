from datetime import datetime

cars_in, cars_out = 0, 0
i = 0
while True:
    gate_in = int(input("enter 0 or 1 for entry gate: "))
    if gate_in == 1:
        cars_in += 1
        print("cars in= ", cars_in, "on", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    else:
        pass

    if cars_in > cars_out:
        gate_out = int(input("enter 0 or 1 for exit gate: "))

        if gate_out == 1 and cars_out >= 0:
            cars_out += 1
            print("cars out = ", cars_out, "on", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        else:
            pass

    print("total no of cars is:", cars_in - cars_out)
    i += 1

