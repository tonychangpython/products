product = []
while True:
	name = input('請輸入產品名稱: ')
	if name == 'q':
		break
	price = input('請輸入產品價格: ')	
	p = [name, price]
	product.append(p)
print(product)
for p in product:
	print(p[0], '的價格是', p[1])