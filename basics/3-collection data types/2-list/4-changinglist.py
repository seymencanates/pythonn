


listForchange = ["keras","numpy","tensorflow","scikit-learn"]

listForchange[1:3] = ["requests" , "irregular"]


print(listForchange)
#there is two chance to be with these way of writing.

#The first of them is
#What would happen if we add more items than we replace?

listForchange[1:2] = ["love","hate"]

print(listForchange)
#u are gonna see The length of the list will change when the number 
# of items inserted does not match the number of items replaced.

#what would happen if we add less value than we replace?


listForchange[1:5] = ["ai"]

# More items inserted than replaced: The list grows.

# Fewer items inserted than replaced: The list shrinks.