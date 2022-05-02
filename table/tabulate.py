from .models import instance

""" a function to change a csv file into a list that has the lines as sub-lists """


def listify(csv):
    with open(csv, 'r') as f:
        listt = []
        for line in f:
            line2 = line.split(',')
            line2[5] = line2[5].replace('\n', '')
            listt.append(line2)

    return listt


master_list = listify("I:\\Programmer's pack\\Files and Docs\\CSV files\\snip csv.txt")

atl = instance.objects.all()
# atl.delete()
# for line in master_list:
#     atl = Athletes(name=line[0], sport=line[1], nationality=line[2], age=line[3], weight=line[4], height=line[5])
#     atl.save()
