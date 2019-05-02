def overlap(line1, line2):
    for i in line2:
        if i in range (line1[0],line1[1]+1):
            return 'overlap'
        else:
            return 'no overlap'


line1a,line1b=input('first line values:').split()
line2a,line2b=input('second line values:').split()

line1=[int(line1a),int(line1b)]
line2=[int(line2a),int(line2b)]

print(overlap(line1,line2))
