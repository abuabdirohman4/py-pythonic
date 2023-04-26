nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
# for index in range(len(nim)):
    # print(f'{nim[index]}--{nama[index]}')

# Pythonic
for index, data_nim in enumerate(nim):
    print(f'{data_nim}=={nama[index]}')