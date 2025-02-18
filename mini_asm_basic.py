# Viet 1 chuong trinh nhap ten + tuoi, in ra man hinh.
# Neu tuoi >= 18 thi in ra ban du tuoi.
# Neu tuoi < 18 thi in ra ban chua du tuoi.

print("Nhap ten cua ban: ")
name = input()
print("Nhap tuoi cua ban: ")
age = int(input())

print(f"Ten cua ban la: {name} va ban {age} tuoi")
if age >= 18:
    print("-> Ban da du tuoi")
else:
    print("Ban chua du tuoi")

