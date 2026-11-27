igala_dictionary = {
                 "Father": "Atah",
                 "Mother": "Iye",
                 "Water": "Omi",
                 "Food": "Ujenwu", 
                 "House": "Unyi",
                 "Child": "Oma",
                 "Friend": "Onukwu",
                 "Love": "Ufedo",
                 "Happiness": "Edebo",
                 "Money": "Oko",
                 "Book": "Otakada",
                 "School": "Unyi Ukoche",
                 "Day": "Ojo",
                 "Night": "Ane",
                 "Name": "Odu",
                 "Beauty": "Unyo",
                 "Peace": "Uredo",
                 "God": "Ojo",
                 "Horse": "Anela",
                 "Dog": "Abija"
}

print("IGALA-ENGLISH DICTIONARY")

for igala, english in igala_dictionary.item():
    print(igala, "=", english

word = input("\nEnter an igala word: ")

if word in igala_dictionary:
    print("translation:", igala_dictionary[word])
else:
    print("word not found in dictionary.")
               
