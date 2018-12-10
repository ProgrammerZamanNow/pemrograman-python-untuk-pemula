# Belajar Default Argument Value

def say_hello(first_name="Budi", last_name=""):
    print(f"Hello {first_name} - {last_name}")

say_hello("Eko")
say_hello(last_name="Kurniawan", first_name="Eko")