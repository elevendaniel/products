products = []
while True:
	name = input ('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	price = int(price)# 价格，所以转化成整数
	products.append([name,price])

print(products)
for p in products:
	print(p[0] ,'的价格是：' , p[1])

with open ('products.csv' , 'w') as f:
	for p in products:
		f.write(p[0]+ ','+str(p[1]) + '\n')
		#用str将p[1]转化成字串是因为p[1]是整数无法和字串p[0]进行合并，只有相同性质的才可以用+ - */进行合并