import string
import random

length = int(input('enter the length og the password : '))

select = int(input('''enter type of password
                   1.easy
                   2.medium
                   3.complex \n'''))
password = ''
if select == 1:
    for i in range(length):
        password += random.choice(string.digits)
elif select == 2:
    #Digits and Letters
    divide = random.randint(1,length)
    temp_password=''
    for i in range(divide):
        temp_password += random.choice(string.digits)
    for i in range(length - divide):
        temp_password += random.choice(string.ascii_letters)
    temp_password_ = list(temp_password)
    random.shuffle(temp_password_)
    password = ''.join(temp_password_)
elif select == 3:
    #digits and letters and special characters
    #Divide the interval
    pt1 = random.randint(1, length)
    pt2 = pt1
    while (pt2 == pt1):
        pt2 = random.randint(1, length)
    
    lower = pt1
    higher = pt2
    if(pt2 < pt1):
        lower = pt2
        higher = pt1

    #print("Intervals", lower, higher)
    # Given number can be divided into 3 parts 
    # [1, lower] [lower, higher] [higher, length]
    temp_password=''
    for i in range(lower):
        temp_password += random.choice(string.digits)
    for j in range(higher - lower):
        temp_password += random.choice(string.ascii_letters)
    for k in range(length - higher):
        temp_password += random.choice(string.punctuation)

    #Shuffle
    temp_password_ = list(temp_password)
    random.shuffle(temp_password_)
    password = ''.join(temp_password_)

print(f"Password generated: {password}")







                    



                   