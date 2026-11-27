ibibio_dictionary = {
       "Étè": "Father" ,
       "Ékà": "Mother" ,
       "M̀mọ́n": "Water" ,
       "Udọn": "Food" ,
       "Ùfọ̀k": "House" ,
       "Eyen": "Child" ,
       "Ùfàn": "Friend" ,
       "Ùfọ̀n": "Love" ,
       "Idem": "Happiness" ,
       "Akụ̀": "Money" ,
       "Ìkọ̀": "Book" ,
       "Ụkọ̀": "School" ,
       "Ùsèn": "Day" ,
       "Ìkọ̀rọ̀": "Night" ,
       "Àfọ̀": "Name" ,
       "Ìfọ̀n": "Beauty" ,
       "Ùkọ̀bọ̀": "Peace" ,
       "Àbàsì": "God" ,
       "Ịnyịnya": "Horse" ,
       "Nkịta": "Dog"
}
print("IBIBIO-ENGLISH DICTIONARY")

for yoruba, english in ibibio_dictionary.items():
  print(ibibio, "=", english)

  word = input("\nEnter a Ibibio word: ")

if word in ibibio_dictionary:
  print("Translation:", ibibio_dictionary[word])
else:
    print("Word not found in dictionary.")
  
