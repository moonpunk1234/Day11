from os import  system

students = [
	{'Id':1, 'Name': 'Chand','Marks':123.99},
	{'Id':2, 'Name': 'Nazmul','Marks':12.99},
	{'Id':3, 'Name': 'Munaz','Marks':23.99}
	]

for std in students:
	print("{} {} {}".format(std['Id'],std['Name'],std['Marks']))

system('cls')

n = int(input('How many employees : ')	)	
employees = []
for i in range(n):	
	id = int(input('Id : ')	)
	name = input('Name : ')	
	sal = int(input('Salary : ')	)

	dic = {'Id':id, 'Name': name,'Salary':sal}
	employees.append(dic)
	system('cls')

print("%-5s %-30s %-20s" % ("Id","Employee Name","Monthly Salary"))
print(60*"=")
for emp in employees:
	print("%-5s %-30s %-20s" %(emp['Id'],emp['Name'],emp['Salary']))