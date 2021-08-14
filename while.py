

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

def lists2dict(keys, values):
    for i in keys:
        for j in values:
            i = 0
            j = 0
            dict_want = {}
            dict_want[keys] = [keys]

print(lists2dict(keys, values))
    
