list = ['programmer', 'truck driver', 'scientist', 'lawyer']
print('index of scientist: ' + str(list.index('scientist')))
print('scientist is in list: ' + str('scientist' in list))
list.append('teacher')
list.insert(0, 'journalist')
for occupation in list:
    print(occupation)