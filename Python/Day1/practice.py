response = raw_input("Hello Welcome!! Please enter your phone number so I may stalk you?")
response = str(response)
placement_of_dash = response.index("-")
placement_of_para = response.index("(")
placement_of_othpara = response.index(")")
counter = true
while true:
    if (len(response) == 13) and (placement_of_dash == 8) and (placement_of_para == 0) and (placement_of_othpara == 4):
        print "I can hear you"
        counter=false
    else:
        print "Don't you know how to put in a phonenumber.Put it in this form"
