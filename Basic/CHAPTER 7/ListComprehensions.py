list = [1,2,3,5,4,9];
# squareList = [];
# for item in list:
#     squareList.append(item*item) 
# print(squareList);

# easy way to do it
squareList = [item*item for item in list];
print(squareList)