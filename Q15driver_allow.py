# A company insur it's driver under the following condition
# 1. If driver is married
# 2. If driver is unmarried male and age above 30 years
# 3. Driver is unmarried female and age is 25 years above

a= str(input ('Enter Married Status (Married/ Unmarried) : '))

if a== 'unmarried':
    b= str(input('male or female : '))
    c= int(input('Enter Age : '))
    if (b== 'male' and c >= 30) or ( b== 'female' and c >= 25):
         print('driver is allow')
    else:
         print('Not allow')
else :
    print('driver is allow')