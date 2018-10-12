from books import Books
import quicksort as qs

BB = Books('Benjamin Blümchen Gutenacht-Geschichtenbuch','383322746X',48)
BB.add_author(['Panini']) 
MB = Books('Ein Tag im Leben von Marlon Bundo','9783742307644',40)
MB.add_author(['Marlon Bundo','Jill Twiss','E. G. Keller']) 
JR = Books('Der Junge im Rock','3865663281',32)
JR.add_author(['Kerstin Brichzin','Igor Kuprin']) 
BT = Books('Bibi und Tina - Pferde-Abenteuer am Meer','9783129493342',34)
BT.add_author(['Matthias von Bornstädt']) 

lib = [BB,MB,JR,BT]
lib = qs.quicksort(lib)
for book in lib:
	print(book)
	print('\n')