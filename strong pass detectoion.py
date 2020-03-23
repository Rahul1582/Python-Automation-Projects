import re

passwordChanged = False
while passwordChanged == False:
 	
	print('Please type a strong pasword')
	uInput = input()

	
	if len(uInput) < 8:
		print ('A strong password has at least 8 chracters')
	else: 
		pass
	#check for a capital
	capitalRegex = re.compile(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')
	mo = capitalRegex.findall(uInput)

	if mo == []:
		print('A strong password includes both capital and lowercase letters')
		
	else:
		pass
		

	#check for a digit
	digitRegex = re.compile(r'[0123456789]')
	mo = digitRegex.findall(uInput)
	
	if mo == []:
		print('A strong password includes at least one number')
		
	else: 
		passwordChanged = True

password = uInput



print('Please confirm the password to unlock a secret message.')
p= input()
u = False
while u == False:

	if p == password:
		print ('SECRET MESSAGE: My birth place is Chennai, and yes you have a strong password!!')
		u = True
	else:
		print('That is not the correct password that you have typed earlier..')
		u = False
