#dictionary = A changeable, unordered collection of uniqua key: value pairs
#             Fast because thay use hashing, allow us to access a value quickly

caplitals = {'USA':'Washington DC',
             'VietNam':'Ha Noi',
             'China':'Beijing',
             'Russia':'Moscow'}
# print(caplitals['VietNam'])
# print(caplitals.get('Germany')) #safer way to print
#print(capitals.items())
for key,value in caplitals.items():
    print(key,value)