# EgneProsjekt
Egne prosjekter jeg lager på Fritiden som ikke er relatert til jobb eller skole


Prosjekt nr 1:
Sjakk.


Åpne filen i Python IDLE (Eller ditt favoritt koderedigeringsprogram) og kjør den, eller kjør filen direkte fra Python-terminalen

Formål:
Formålet med å lage dette prosjektet var å forbedre programmeringskunnskapene mine ved å programmere et spill uten en spillmotor, kun ved hjelp av spillbiblioteket pygame.

Krav:
Kravene til dette prosjektet er å ha et fungerende sjakkbrett med en kunstig intelligens som kan komme med mottrekk. og samt følge ordinære regler for sjakk, sjakkmatt og patt.

Erfaring og tanker:
For meg som en it-interressert høres dette ut som et gøy lite prosjekt. Etter å ha programmert det ferdig, har jeg fått følelsen av nøyaktig hvor mye arbeid det faktisk er å lage software.
Det er fort gjort å tenke at en bare trenger å flytte brikker med noen linjer kode og så er en ferdig, men i skrivende stund har prosjektet 1413 linjer kode! selvfølgelig regnes da tomme linjer inn, men det er allikevel mye.
I tillegg bemerker jeg hvordan en enkelt snarvei tidlig på veien førte til voldsom spaghettikode senere. Jeg tenker da på initialiseringen av brettet, hvor i og j er reversert i forhold til et vanlig koordinatsystem (i er x, j er y, så formatet blir j,i)
Jeg kunne nok ha omgått dette ved å bruke det mer etablertet forsyth-edwards-notation. Men for dette eventyret ville jeg ha så mange av mine egne ideer formulert i koden som mulig, som er mindre effektivt;
men som jeg personlig mener fører til en bedre induktiv tankegang mtp selve kodingen. Med andre ord gjør det meg etter min mening bedre på å oversette ideene mine til kode i fremtiden på å tenke skikkelig gjennom det selv og dermed ikke alltid følge etablert beste praksis.

Bemerkninger:
Det forekommer av og til bugs ol i koden, jeg har prøvd å programmere rundt det, og fikse så mange som mulig, men av og til får en en bug eller liknende som er vanskelig å replisere og dermed vanskelig å fikse

I tillegg har jeg også brukt chatpgt under deler av Debuggingen, dette gjelder når jeg slitt lenge med en del av koden som bare ikke ville funger. Dvs selve koden er min, chatgpt bla brukt hvis jeg satt fast på noe kode og det var en feil som var vanskelig å se

Kjøre spillet:
Windows:
Du kan enten dobbeltklikke på Sjakk_Win.exe filen i dist mappen(Hvis den ikke vises i den filen kan det være at du må skru av aktiv scanning for virus i windows defender) eller så kan du kjøre kildefilen som forklares under.

Linux:
Du kan enten høyreklikke på Sjakk_Linux excecutable filen og tillate den å kjøre fult av å dobbeltklikke på Sjakk_Linux excecutable filen i dist mappen, eller så kan du kjøre kildefilen som forklares under.

MacOS:
Har ikke mac, så kan ikke pakke en excecutable for for systemet, kjør det fra kiledkode som forklart under

Kjøring fra kildekoden:
Sjakk krever at du har installert pygame på en python-installasjon for å kjøre fra kildefil, men jeg har inkludert en ompakting i dist-filen som jeg mener skal kunne kjøres med dobbeltklikk
Python kan installeres herfra:
https://www.python.org/downloads/

Pygame kan installeres med følgende kommando i terminalen(powershell på windows, bash på MacOS og Linux):

pip install pygame-ce

Her er mer dokumentasjon for pygame:
https://pypi.org/project/pygame-ce/

Åpne filen i Python IDLE (Eller ditt favoritt koderedigeringsprogram) og kjør den, eller kjør filen direkte fra Python-terminalen


Prosjekt nr 2(WIP):
Arbeid Pågår