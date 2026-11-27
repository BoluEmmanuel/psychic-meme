igbo_translation = {
     "Nna": "Father",
     "Nne": "Mother",
     "Bik": "Please",
     "Nri": "Food",
     "Ụlọ": "House",
     "Nwa": "Child",
     "Enyi": "Friend",
     "Ịhụnanya": "Love",
     "Añụrị": "Happiness",
     "Ego": "Money",
     "Akwụkwọ": "Book",
     "Ụlọ akwụkwọ": "School",
     "Ụbọchị": "Day",
     "Abalị": "Night",
     "Aha": "Name",
     "Mma": "Beauty",
     "Udo": "Peace",
     "Chukwu": "God",
     "Ịnyịnya": "Horse",
     "Nkịta": "Dog"
}   

 print("IGBO-ENGLISH DICTIONARY")

for igbo, english in igbo_dictionary.items():
    print(igbo, "=", english)

word = input("\nEnter a Igbo word: ")

if word in igbo_ dictionary:
    print("Translation:", igbo_dictionary[word])
else:
    print("Word not found in dictionary.")   
     
