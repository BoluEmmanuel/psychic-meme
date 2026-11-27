yoruba_dictionary = {
    "Bàbá": "Father",
    "Ìyá": "Mother",
    "Omi": "Water",
    "Oúnjẹ": "Food",
    "Ilé": "House",
    "Ọmọ": "Child",
    "Ọ̀rẹ́": "Friend",
    "Ìfẹ́": "Love",
    "Ayọ̀": "Happiness",
    "Owó": "Money",
    "Ìwé": "Book",
    "Ilé-ìwé": "School",
    "Ọjọ́": "Day",
    "Òru": "Night",
    "Orúkọ": "Name",
    "Ẹwà": "Beauty",
    "Àlàáfíà": "Peace",
    "Ọlọ́run": "God",
    "Ẹṣin": "Horse",
    "Ajá": "Dog"
}

print("YORUBA-ENGLISH DICTIONARY")

for yoruba, english in yoruba_dictionary.items():
    print(yoruba, "=", english)

word = input("\nEnter a Yoruba word: ")

if word in yoruba_dictionary:
    print("Translation:", yoruba_dictionary[word])
else:
    print("Word not found in dictionary.")
