# def bio_data(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# bio_data(name='surya', sapid=590015171)
# dict1={"name" : "surya", 
#        "sapid" : "590015171"}
# take values form a list and store them in a dictionary using functions
d1={
    "name":"suryansh",
    "sapid":"590015171"
}
list1=["badri", "590017525"]
j=0
def listodict(*list):
    for i, val in enumerate(d1):
        print(i,val)
        # d1[j]=list1[0]
        # j+=1
# print(d1)
listodict()