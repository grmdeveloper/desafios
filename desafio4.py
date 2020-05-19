blocks = []
water_block = 0

n = int(input('insira o número de quantidade de blocos no eixo X: '))

while len(blocks) < n:
    insert = input('número de blocos na casa {}: '.format(len(blocks)+1))
    if insert.isnumeric() and int(insert) >= 0:
        blocks.append(int(insert))
    else:
        print('Por favor, insira um número inteiro e não negativo')

for y_pos in range(1, len(blocks)+1):

    end_pointer = -1
    start_index = 0
    end_index = 0

    for value in blocks:
        if value >= y_pos:
            break
        start_index += 1

    for x in range(start_index, len(blocks)):
        if x == n:
            start_index = 0
            end_index = 0
            break
        elif blocks[end_pointer] >= y_pos:
            end_index = len(blocks)+end_pointer
            #print(end_pointer, end)
            break
        else:
            end_pointer -= 1

    for index in range(start_index, end_index):
        if blocks[index] < y_pos:
            water_block += 1

print(water_block)