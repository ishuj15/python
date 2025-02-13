# for i in range(0,5):
#     print("*")
# count=0
# while count<5:
#     print("**")
#     count+=1
# Pattern 1
i=0
for i in range(1,6):
    for j in range(0,i):
        print(f"{i}",  end='')
    print()

# Pattern 2
print('\n')
i=0
for i in range(1,6):
    for j in range(1,i+1):
        print(f"{j}",  end='')
    print()
#  Pattern 3
print('\n')
ch='A'
for i in range(1,6):
    for j in range(1,i+1):
        print(f"{ch}",  end='')
        ch=chr(ord(ch)+1)
    print()
    ch='A'
# Pattern 4
print('\n')
