
hour, mr = '00', []
for i in range(1, 49):
    minute = '00'
    if i % 2 == 0:
        hour = '0' + str(int(hour) + 1) if int(hour) < 9 else int(hour) + 1
    else:
        minute = '30'
    mr.append((i, '%s:%s' % (hour, minute)))


print(mr)
