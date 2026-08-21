weather = input("Enter weather (sunny/rainy/snowy): ").strip().lower()

if weather == "sunny":
    activity = "Go for a walk"

elif weather == "rainy":
    activity = "Read a book"

elif weather == "snowy":
    activity = "Build a snowman"

else:
    print("Invalid Input")
    exit()

print(activity)    


# Ek shortcut jo main hamesha use karta hoon:

# Apne aap se ek question pucho:

# "Kya is line se Python error (exception) aa sakta hai?"

# Haan → try-except use karne ke baare me socho.
# Nahi → Sirf if-elif-else kaafi hai.

# Ye rule tumhe 90% beginner cases me sahi direction de dega.