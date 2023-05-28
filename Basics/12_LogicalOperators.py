high_Income=True
good_CreditScore=True
if high_Income and good_CreditScore:
    print('Applicant is eligible for loan')

high_Income=True
good_CreditScore=False
if high_Income or good_CreditScore:
    print('Applicant is eligible for loan')

good_CreditScore=True
has_CriminalRecord=False
if good_CreditScore and not has_CriminalRecord:
    print('Applicant is eligible for loan')


temperature=30
if temperature > 30:
    print('Hot day')
elif temperature<10:
    print('Cold day')
elif temperature==30:
    print('Perfect weather')
else:
    print('Neither cold nor hot day')

name = 'am'
if len(name)<3:
    print('Name must be 3 chars long')
elif len(name)>50:
    print('Name cannot be more than 50 chars long')
else:
    print('Name looks good')

weight= int(input('Enter your weight >> '))
unit=input('Enter unit of your weight >> ')
if unit.upper() == 'KGS':
     weight=weight*0.45
     print(f'Weight in Lbs is {weight}')
elif unit.upper() == 'LBS':
     weight = weight / 0.45
     print(f'Weight in Kgs is {weight}')

