is_raining = input("Is it raining? ")

if is_raining.upper() == 'YES':

    have_umbrella = input("Have an umbrella? ")

    if have_umbrella.upper() not in "YES":
        is_raining = input("Is it still raining? ")
        while is_raining.upper() not in "NO":
            is_raining = input("Is it still raining? ")

print("Go outside")
