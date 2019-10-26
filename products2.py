import os #operating system
#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products			

#請使用者輸入
def user_input(products):
	while True:
		name = input('請輸入產品名稱: ')
		if name == 'q':
			break
		price = input('請輸入產品價格: ')	
		price = int(price)
		p = [name, price]
		products.append(p)
	print(products)
	return products

#印出所有購買紀錄
def print_product(products):
	for p in products:
		print(p[0], '的價格是', p[1])
	
#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')	

def main():
	products = []
	filename = 'product2.csv'
	if os.path.isfile(filename): #檢查檔案在不在
		print('Yeah! 找到檔案了')
		products = read_file(filename)
	else:
		print('找不到檔案')			
	products = user_input(products)
	print_product(products)
	products = write_file('product2.csv', products)
main()	