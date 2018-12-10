# Belajar Set

# list => []
# tuple => ()
# set => {}

nama = {"Eko", "Joko", "Eko", "Joko", "Andi"}

nama.add("Kurniawan")
nama.add("Kurniawan")
nama.add("Kurniawan")

for data in nama:
    print(data)

nama.remove("Eko")
nama.remove("Andi")

print(nama)