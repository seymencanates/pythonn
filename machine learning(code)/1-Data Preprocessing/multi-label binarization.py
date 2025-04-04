


from sklearn.preprocessing import MultiLabelBinarizer

habitsOfFeeding = {

    "owl" : ["chicks","mice"],
    "goat":["forage","hay","grass"],
    "cat":["chicken","mice"],
    "fox":["rabbit","chicken","martel"]
}

listes = list(habitsOfFeeding.values()) 

mlbb = MultiLabelBinarizer()


print(mlbb.fit_transform(listes))

print(mlbb.classes_)

