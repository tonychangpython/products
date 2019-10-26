products = []
while True:
	name = input('請輸入產品名稱: ')
	if name == 'q':
		break
	price = input('請輸入產品價格: ')	
	p = [name, price]
	products.append(p)
print(products)
for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')