name= input("Ievadi savu vardu:")
age= input("Ievadi savu vecumu:")
print("Čau,", name,", tev ir", age + "!")

a= int(input("Ievadi pirmo skaitli:"))
b= int(input("Ievadi otro skaili:"))
print(a+b)



x= int(input("Ievadi skaitli:"))
if x > 0:
    print("Pozitivs")
elif x < 0:
    print("Negativs")
else:
    print("Nulle")

vecums= int(input("Ievadi savu vecumu:"))
if vecums >= 18:
    print("Pilngadīgs")
else:
    print("Nepilngadīgs")

sk = int(input("Ievadi skaitli:"))
if 10 <= sk <= 20:
    print("Skaitlis ir starp 10 un 20")
else:
    print("Skaitlis nav starp 10 un 20")

for i in range(1,11):
    print(i)


