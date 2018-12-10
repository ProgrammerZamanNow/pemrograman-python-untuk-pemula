# Belajar Tipe Data Dictionary

daftar_customer = []
eko = { "Name":"Eko", "Age":30, "Address":"Subang" , "Company":"X"}
budi = { "Name":"Budi", "Age":25, "Address":"Surabaya" , "Company":"Y"}
joko = { "Name":"Joko", "Age":31, "Address":"Cirebon" , "Company":"Z"}

daftar_customer.append(eko)
daftar_customer.append(budi)
daftar_customer.append(joko)

for customer in daftar_customer:
    print("====================")
    for key,value in customer.items():
        print(f"{key}:{value}")