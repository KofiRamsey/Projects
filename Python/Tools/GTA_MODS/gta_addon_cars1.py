# Txt method
# put all the names of files in a gtacars.txt file

for item in open('gtacars.txt'):
	x = f'		<Item>dlcpacks:/{item.strip()}/</Item>'
	print(x)