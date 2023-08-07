Number=int(input("Enter the number of units = "))
Amount=0
if Number<=50:
    Amount="number*2"
    surcharge=20

if Number>50<=150:
    Amount="number*2"+"number*3"
    surcharge=20

if Number<150<=250:
    Amount="number*2"+"number*3"+"number*5"
    surcharge=20

elif Number<250:
    Amount="Number*2"+"Number*3"+"Number*5"+"Number*8"
    surcharge=20

    print("Amount to pay+surcharge")





