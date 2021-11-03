from os import replace
import re

with open('potential-contacts.txt') as file:
  file=file.read()

phone_numbers = re.findall(r'[(]+[0-9]+[)]?-?[0-9]{3}-?[0-9]{4}|[\d]{3}-[\d]{3}-[\d]{4}|[\d]{3}-[\d]{4}',file)

phone_numbers=set(phone_numbers)
cleaned_phone_numbers=[]

for i in phone_numbers:
  if len(i)<12:
    cleaned_phone_numbers.append('206-'+i)

for i in phone_numbers:
  if len(i)==12:
    cleaned_phone_numbers.append(i)
  
for i in phone_numbers:
  if i[0]=='(':
    cleaned_phone_numbers.append(i[1:4]+'-'+i[5:])

with open('phone_numbers.txt', 'w') as result_file:
  for i in cleaned_phone_numbers:
    result_file.write(f'{i}\n')




emails=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',file)
emails=set(emails)

with open('emails.txt', 'w') as emails_file:
  for i in emails:
    emails_file.write(f'{i}\n')