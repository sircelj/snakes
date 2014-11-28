# Snakes

A tutorial on how to use Git (in Slovene).

Od zdaj najprej govorimo po slovensko. To je gradivo za računalniško delavnico o Git, ki
je potekala 28. novembra 2014 na Fakulteti za matematiko in fiziko, Univerza v Ljubljani.

## Kaj je git?

To bomo v živo izvedeli na delavnici.

## Kaj potrebujem za delo z git?

### Programska oprema

Na računalnikih v laboratoriju sta že nameščena msysgit in TortoiseGit. Za delo doma pa si
namestite naslednjo opremo:

* OSX: `git` je že nameščen
* Windows: [msysgit](http://msysgit.github.io), za bolj udobno uporabo pa [TortoiseGit](https://code.google.com/p/tortoisegit/)
* Linux: namestite si paket `git-client` ali kakorkoli se mu že reče na vaši distribuciji

Dodatno GitHub ponuja tudi svoj grafični vmesnik za delo z git, ki deluje kar dobro. Na voljo je [različica za Windows](http://windows.github.com) in [različica za OSX](https://mac.github.com).

Če uporabljate Eclipse, si namestite plugin [EGit](http://eclipse.org/egit/). Ta je
nameščen tudi na Eclipse v računalniških laboratorijih.

### Uporabniški račun na GitHub

Na delavnici bomo delali z repozitoriji na [GitHub](https://github.com), zato si tam
ustvarite uporabniški račun, če ga še nimate.

GitHub brezplačno omogoča neomejeno število repozitorijev, vendar so vsi javno dostopni.
Če želite uporabljati privatne repozitorije, lahko na [GitHub Student
Pack](https://education.github.com/pack), ali pa uporabite
[BitBucket](https://bitbucket.org), ki vam brezplačno omogoča privatne repozitorije z do
petimi sodelavci. Zaposleni na FMF imajo dostop do [privatnega FMF
strežnika](http://git.fmf.uni-lj.si/), ki ne postavlja nobenih omejitev (in zunanji
sodelavci ga lahko uporabljajo, če imajo Google account).

### Namestitev ključev SSH

Git uporablja varnostni protokol Secure Shell (ssh) za avtentikacijo. To pomeni, da morate
pred uporabo strežnika namestiti SSH ključe na GitHub. To je najbolj zoprn del
instalacije, ko pa je enkrat narejena, deluje dobro.

Navodila, kako se namesti SSH ključe najdete
[v dokumentaciji za GitHub](https://help.github.com/articles/generating-ssh-keys/). Na
delavnici se bomo skupaj prebili čez postopek.

## Delo z git

### Mini demo

1. Prijavite se na GitHub.

2. Ustvarite [nov repozitorij](https://github.com/new).
   * Izberite ustrezen jezik.
   * Izberite ustrezno licenco.

3. Ustvarjeni repozitorij klonirajte na svoj računalnik. Pazite, da boste uporabili
   protokol SSH, se pravi, naslov repozitorija mora biti oblike
   `git@github.com:uporabnik/repo.git` in ne `https://github.com/uporabnik/repo.git`.

4. V repozitorij dodajte datoteko in vanj nekaj napišite.

5. Naredite `commit`.

6. Naredite `push`.

7. Datoteka bi se morala pojaviti na strežniku.

8. Pobrišite repozitorij na svojem računalniku.

9. Še enkrat ga klonirajte. Ničesar niste izgubili!

### Igrica Snake

#### Fork

Naredite *fork* repozitorija [`andrejbauer/snakes`](https://github.com/andrejbauer/snakes)
(gumbek "Fork" zgoraj desno). S tem boste dobili svojo različico repozitorija.

#### Clone

Klonirajte **svojo različico** repozitorija k sebi, se pravi ustrezni naslov repozitorija
bo `git@github.com:uporabnik/snakes.git` kjer `uporabnik` **ni** `andrejbauer`.

#### Dodajte svojo kačo

Igrici dodajte svojo kačo:

1. Izberite ime svoje kače (pomagajte si s [tem
   spiskom](http://en.wikipedia.org/wiki/List_of_snakes_by_common_name)), recimo da ste
   izbrali "Black Adder".

2. Datoteko `bolivianAnaconda.py` prekopirajte v `blackAdder.py` (oziroma kakorkoli je že
   ime vaši kači).

3. Popravite `blackAdder.py` in jo ne pozabite dodati v git repozitorij z

       git add blackAdder.py

4. Svojo kačo dodajte v spisek kač `SNAKES` v datoteki `game.py`.

5. Preizkusite igrico, tako da poženete `game.py`.

#### Commit

Ko ste zadovoljni s spremembami, jih dodajte v repozitorij:

    git commit -m "opis sprememb" -a

#### Push

Spremembe pošljite na GitHub:

    git push
    
#### Pull

Izberite različico enega od udeležencev delavnice (glej [spisek](https://github.com/andrejbauer/snakes/network)) in njegove spremembe prenesite k sebi. Denimo, da ste izbrali udeleženca z uporabniškim imenom `lolek`:

    git remote add lolek git@github.com:lolek/snakes.git
    git pull lolek master
    
Sedaj imate tudi `lolek`ove kače!

#### Pull request

Svoje spremembe predlagajte za vključitev v glavno različico, ki jo ima uporabnik
`andrejbauer`. Na svoji različici naredite *pull request* (izbira "pull requests" na
menuju na desni, nato gumb "new pull request"). Z nekaj sreče bo Andrej Bauer sprejel vaše
spremembe.

#### Pull iz `upstream`

Spremembe, ki jih je naredil Andrej Bauer (sprejel je kopico pull requestov) prenesite v
svojo različico:

    git remote add upstream git@github.com:HoTT/HoTT.git
    git pull upstream master

Sedaj imate kače vseh udeležencev!


