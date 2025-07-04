dict = {}

dict['item1'] = []
dict['item2'] = []
dict['item1'].append('item2')
dict['item2'].append('item1')

for i in dict.items():
    print(i)
