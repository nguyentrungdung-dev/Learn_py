spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

##########
if spam_amount > 5:
    print("But I don't want ANY spam!")

##############
viking_song = "Spam " * spam_amount
print(viking_song)

#Explain the code:
# First, we have spam_amount = 0, then we print it
# Then, we set spam_amount = spam_amount + 4 ---> spam_amount now is 4
# Then, we check spam_amount > 5, if true, print like that. 
# If not, do nothing!!! And like that result, the code do nothing
# Finally, we create a new variable name is viking_song, and set it equal to "Spam" * spam_amount
# It mean that we have 4 times "Spam" when we print viking_song.
