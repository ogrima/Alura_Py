# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

print("********************************")
print("     While com Contador         ")
print("********************************")

contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 2
    if(contador == 5):
        contador = contador + 2

print("********************************")
print("     FOR com Range de 2 em 2    ")
print("********************************")


for rodada in range(1,10,2):
    print(rodada)

print("********************************")
print("             Break              ")
print("********************************")
i = 1
while (i <= 7):
    print(i)
    i = i + 1
    if (i == 5):
        break

print("********************************")
print("          Continue              ")
print("********************************")

for i in range(1,8):
    if(i == 5):
        continue
    print(i)

print("********************************")
print("          Format                ")
print("********************************")

print("R$ {:f}".format(1.59))
print("R$ {:7.2f}".format(1234.50))
print("R$ {:07.2f}".format(1.5))
print("Data {:02d}/{:02d}".format(9, 4))
print("Data {:02d}/{:02d}".format(19, 11))

print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))