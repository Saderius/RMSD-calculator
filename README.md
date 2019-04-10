# RMSD-calculator
Skrypt liczący wartości RMSD dla dowolnych ligandów po zadokowaniu do białek.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
UWAGA UWAGA UWAGA UWAGA UWAGA UWAGA UWAGA UWAGA UWAGA UWAGA UWAGA UWAGA UWAGA UWAGA 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
Skrypt działa jedynie z plikami ligandów o rozszerzeniu mol2. W przypadku innych
plików rozszerzeń sugerowane jest przepisanie ich na do formatu mol2. Operację
można z sukcesem wykonać przy użyciu programu OpenBabel. Również najlepiej 
współpracuje z plikami outputowymi z programu gold. BUT FEAR NOTHING MY CHILD
zawsze można w skrypcie zmienić frazy po jakich szuka i ustawić dowolne. 

Pamiętaj tylko że ORIGIN to ten, którego nie liczysz, a SOLN to zadokowane!
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

Użycie:
1. Umieść skrypt w folderze nadrzędnym.
2. Uruchom skrypt. 
3. Brak printów w konsoli, huh? To zajrzyj do folderu gdzie jest skrypt. Powinien
być tam plik output.txt (chyba zmienię na .log żeby było bardziej PRO, ale to jak 
mi się będzie chciało). W tym pliku jest wszystko czego potrzebujesz. Jeśli czegoś
brakuje to zrobiłeś coś źle. Zacznij od sprawdzenia rozszerzeń plików i struktury
folderów. Jak nie będzie śmigać to zakomentuj 

#outputuje wszelkie printu
import sys
sys.stdout = open('output.txt','wt')

i szukaj problwmu na własną rękę. Stawiam na rozszerzenia lub problem z frazą.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

All Star
Smash Mouth
Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead
Well the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go
You'll never shine if you don't glow
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold
It's a cool place and they say it gets colder
You're bundled up now, wait till you get older
But the meteor men beg to differ
Judging by the hole in the satellite picture
The ice we skate is getting pretty thin
The water's getting warm so you might as well swim
My world's on fire, how about yours?
That's the way I like it and I never get bored
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
All that glitters is gold
Only shooting stars break the mold
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show, on get paid
And all that glitters is gold
Only shooting stars
Somebody once asked could I spare some change for gas?
I need to get myself away from this place
I said yep what a concept
I could use a little fuel myself
And we could all use a little change
Well, the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go (go!)
You'll never shine if you don't glow
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold
And all that glitters is gold
Only shooting stars break the mold
Autorzy utworu: Gregory Camp
Lyrics All Star © Spirit Music Group
