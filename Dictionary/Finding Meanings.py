# Program for finding the longest and shortest meaning in a dictionary

dict1 = {'piece': 'portion of an object or material, produced by cutting',
         'patch': 'a piece of cloth or other material used to mend or strengthen a torn weak point',
         'area': 'a region or part of a town, a country, or the world',
         'visit': 'go to see and spend time with',
         'with': 'having or possessing',
         'small': 'less than usual'}

keys = list(dict1.keys())
values = list(dict1.values())
lengths = [len(x) for x in values]

max_len = max(lengths)
min_len = min(lengths)

max_index = lengths.index(max_len)
min_index = lengths.index(min_len)


print('Max = ', keys[max_index], ':', values[max_index])
print('Min = ', keys[min_index], ':', values[min_index])