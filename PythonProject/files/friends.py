# name1=input("Enter first friend name")
# name2=input("Enter first friend name")
# name3=input("Enter first friend name")
# or
friends=input("Enter friends name seperated by commas ").split(',')

people=open('people.txt','r')
people_nearby= [  line.strip() for line in  people.readlines()]
print(people_nearby)
people.close()

friends_set=set(friends)
people_nearby_set=set(people_nearby)

nearby_file= open('nearby.txt','w')
for list in friends:
    if not  list in people_nearby:
        nearby_file.writelines(list + '\n')

nearby_file.close()

