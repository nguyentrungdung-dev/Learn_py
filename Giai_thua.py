num = int(input("Nhap mot so: "))

giai_thua = 1
for i in range(1, num + 1):
    giai_thua *= i

print(f"Giai thua cua {num} la: {giai_thua}")