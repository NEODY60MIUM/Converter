first_no = float(input("Please type the value you want to convert: "))
convertion = input("Convert from minutes to hours or hours to minutes? (Input min-hr or hr-min): ")
if convertion == "min-hr":
    hr = int(first_no/60) 
    min = int(first_no%60)
    print (str(hr) + " hours")
    print (str(min) + " minutes")
elif "hr-min":
    min = float(first_no*60)
    print (str(min))
else :
    print("Invalid")