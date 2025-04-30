data_stu= {"id1":
           {"name":["potato"],
            "age":[21],
            "Subjects":["English Literature"]},

            "id2":
            {"name":["onion"],
             "age": [22],
             "Subjects": ["Drama, English Lit"]},

             "id3":
             {"name": ["potato"],
              "age": [21],
              "Subjects": ["English Literature"]},

              "id4":
              {"name": ["tomato"],
               "age": ["23"],
               "Subjects": ["Achitecture"]}
           }
result={}
for key,value in data_stu.items():
    if value not in result.values():
        result[key]= value

print(result)

