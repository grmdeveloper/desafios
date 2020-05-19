#Dado um array de números inteiros, retorne os índices dos dois números de forma que eles se somem a um alvo específico.
#Você pode assumir que cada entrada teria exatamente uma solução, e você não pode usar o mesmo elemento duas vezes.


nums = []
target = 0
results = []
success = False

while True:
    num = input('Input a number in the list (0 to finish)')
    if num.isnumeric() == True:
        if num == '0':
            break
        nums.append(int(num))
    else:
        print('Please, insert a valid number')

nums.sort()

target = input("Set target:")
while not target.isnumeric():
    target = input("Please, insert a numeric value: ")
target = int(target)

for v in nums:
    if success:
        break

    index = nums.index(v)
    pointer = nums.index(v)+1

    while pointer < len(nums):
        results.append(v + nums[pointer])
        if target in results:
            success = True
            print(index, pointer)
            break
        pointer += 1

if not success:
    print('No Occurrency')