import json
x = '{"name":"jonh"}'
y = json.loads(x)
print(y)
# print(y.keys())
for key, value in y.items():
    print(key)
# for key, value in y.iterrows():
#     print (key)
# # print(y)