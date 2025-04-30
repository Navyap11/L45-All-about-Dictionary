og_diction= {"hi":2,
             "my":4,
             "name":2,
             "is":1,
             "Navya":2}

print("The oG dictionary: "+ str(og_diction))

k=2

result=0
for key in og_diction:
    if og_diction[key]==k:
        result +=1

print("The frequency of 2 is: "+str (result))
