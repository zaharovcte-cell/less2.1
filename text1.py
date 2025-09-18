from transliterate import translit
from num2words import num2words

print(translit("Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. \nPeople have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. \nNeither will happen.", 'ru'))
print()
print(translit("More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...", 'ru'))
print()
[print(f"{n} - {translit(num2words(n, lang='en'), 'ru')}") for n in [78, 15, 3, 40, 8]]

 
     
 
       
        
         
           
           
