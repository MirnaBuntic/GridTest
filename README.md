# Risk Kluster analys – Python 

Risk Cluster Analysis er et Python-prosjekt som analyserer et rutenett med numeriske risikoverdier for å identifisere områder med høy risiko.

Programmet leser inn data fra en tekstfil, undersøker ulike kombinasjoner av verdier og identifiserer grupper som oppfyller bestemte kriterier.

Prosjektet er utviklet for å øve på **filbehandling, nøstede løkker, lister, dictionaries, funksjoner og algoritmisk problemløsning** i Python.

## Teknologier

- **Python** – Programmeringsspråket som brukes til å utvikle analyseverktøyet.
- **Tekstfiler (.txt)** – Brukes til å lagre risikoverdiene som skal analyseres.
- **Lister og dictionaries** – Brukes til å organisere rutenettet og lagre informasjon om identifiserte risikoklynger.

## Funksjonalitet

Programmet analyserer et rutenett med risikoverdier og inneholder følgende funksjonalitet:

- **Filinnlesing** – Leser risikoverdier fra en tekstfil og organiserer dem i en todimensjonal liste.
- **Identifisering av risikoklynger** – Søker etter grupper på fire sammenhengende verdier.
- **Flere søkeretninger** – Undersøker verdier horisontalt, vertikalt og diagonalt.
- **Beregning av gjennomsnitt** – Regner ut gjennomsnittlig risikoverdi for hver gruppe.
- **Filtrering av resultater** – Registrerer kun klynger med en gjennomsnittlig risikoverdi på minst 70.
- **Sortering av klynger** – Sorterer resultatene etter gjennomsnittlig risiko, høyeste enkeltverdi og posisjon.
- **Resultatvisning** – Skriver ut informasjon om alle identifiserte klynger og det totale antallet.

## Hvordan programmet fungerer

Programmet leser inn et rutenett fra filen `riskgrid.txt`, der hver linje representerer en rad med risikoverdier.

`read_grid_from_file()` åpner tekstfilen, leser innholdet og konverterer verdiene til heltall som lagres i en todimensjonal liste.

`find_risk_clusters()` går gjennom rutenettet ved hjelp av nøstede `for`-løkker. For hver posisjon undersøker funksjonen om det finnes fire sammenhengende verdier i følgende retninger:

- Horisontalt mot høyre.
- Vertikalt nedover.
- Diagonalt nedover mot høyre.
- Diagonalt oppover mot høyre.

`add_if_significant()` beregner gjennomsnittet av de fire verdiene. Dersom gjennomsnittet er minst 70, lagres klyngen som en dictionary med verdier, posisjoner, retning og gjennomsnitt.

`get_sort_key()` definerer kriteriene som brukes til å sammenligne klyngene.

`sort_clusters()` sorterer resultatene slik at klyngene med høyest gjennomsnittlig risikoverdi vises først. Ved likt gjennomsnitt brukes høyeste enkeltverdi og deretter posisjon som sorteringskriterier.

`print_significant_clusters()` skriver ut de sorterte klyngene i terminalen, og programmet viser til slutt hvor mange signifikante klynger som ble funnet.

## Hva jeg har lært

Gjennom dette prosjektet har jeg fått praktisk erfaring med flere sentrale konsepter innen Python:

- Lese og behandle data fra eksterne tekstfiler.
- Arbeide med todimensjonale lister.
- Bruke nøstede løkker for å analysere større datasett.
- Kontrollere indekser og grenser i et rutenett.
- Dele opp komplekse oppgaver i mindre, gjenbrukbare funksjoner.
- Bruke dictionaries til å strukturere analyseresultater.
- Sortere data med egendefinerte sorteringskriterier.
- Utvikle algoritmer for å identifisere mønstre i numeriske data.

## Videreutvikling

Prosjektet kan videreutvikles med en grafisk visualisering av rutenettet, der områder med høy risiko markeres med forskjellige farger.

Andre mulige forbedringer inkluderer støtte for ulike størrelser på risikoklynger, justerbare grenseverdier og eksport av analyseresultater til en fil.

Prosjektets hovedfokus har vært å utvikle en algoritme som kan analysere strukturerte data, identifisere mønstre og presentere resultatene på en oversiktlig måte.
