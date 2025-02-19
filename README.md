# eon-aramszunet-checker

Az E.ON áramszünet információk 1-2 hónapra előre, az egész ország területére elérhetőek itt:
https://www.eon.hu/hu/lakossagi/aram/aramszunet-informaciok.html

Innen letölthető egy xls is, ami tartalmazza az összes tervezett áramszünetet.

A read_excel.py script ezt a fájlt tölti le, és a megadott kifejezésre rákeres.

Csináltam hozzá egy docker image-t is, amivel egyszerűen használhatóvá válik a script:
docker run feriman25/eon-aramszunet-checker:latest "Keresendő kifejezés"

Településre vagy utcanévre célszerű rákeresni. Ha több kifejezésre is rá kell keresni, akkor grep-el bővíthető:
docker run feriman25/eon-aramszunet-checker:latest "Keresendő kifejezés" | grep "Szűkebb keresés"

Konkrét példák:
docker run feriman25/eon-aramszunet-checker:latest "Taksony"
docker run feriman25/eon-aramszunet-checker:latest "Budapest" | grep "Váci út"
