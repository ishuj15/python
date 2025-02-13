import  json

# file=open('friends_json.txt','r')
# file_content=json.load(file) #turns to dictionary
# file.close()
# or open close file using context manager
with open('friends_json.txt','r') as file:
    file_content = json.load(file)

print(file_content['friends'][0])

cars =[
    {
        'make':'Ford', 'model': 'Fiesta'
    },
    {
        'make': 'Suzuki', 'model': 'Brezza'
    }
]

file=open('friends_json.txt','w')
json.dump(cars,file)
file.close()










