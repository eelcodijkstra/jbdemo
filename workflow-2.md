# Workflow: bestaand materiaal aanpassen

In de vorige workflow heb je gezien hoe je bestaand materiaal kunt publiceren.
In deze workflow gaan je bestaand materiaal aanpassen, dit publiceren, en opslaan in GitHub.
Eventueel kun je de wijzigingen ook weer terugmelden naar de oorspronkelijke versie.

We gebruiken in dit geval een variant van de *GitHub flow*: je brengt je wijzigingen aan in een eigen branch.
Als het eenmalige wijzigingen zijn kun je deze branch daarna ook weer opruimen.
Zie: https://docs.github.com/en/get-started/quickstart/github-flow

We gaan ervan uit dat je in de vorige workflow al een GitHub *fork* gemaakt hebt van het origineel,
en een lokale *clone* op de Jupyter Hub van je kopie-repository.

Stappen:

1. maak een branch aan voor de wijzigingen.
2. breng de wijzigingen aan, en publiceer deze (herhaal eventueel deze stap)
3. "commit" en "push" je veranderingen naar je repository op GitHub
4. (eventueel) maak een pull-request op GitHub naar de originele repository
5. (eventueel) ruim je branch op, als het pull-request verwerkt is.

## Maak een eigen branch voor de wijzigingen

Zorg dat je in Jupyter Lab, in het bestanden-overzicht links, het bestand *jbdemo* geselelcteerd hebt; je ziet dan bovenin 
`/jbdemo/` en daaronder de bestanden van *jbdemo*.
Selecteer nu helemaal links de Git-plugin. Je ziet dan de toestand van de lokale jbdemo repository.
Kies bij het klein selectie-driehoekje in de regel "Current Branch": New Branch. En kies voor de naam van de branch je eigen naam. Je ziet dat dan ook de naam van de Current Branch verandert.

Je ziet ook bovenin bij het "upstream wolkje" een oranje stip. Als je de cursor daaroverheen beweegt, zie je "publish branch" staan. Daar komen we later op terug.

Ga nu terug naar het bestandsoverzicht.

## Breng de wijzigingen aan

Open het bestand "intro.md" in een editor, en pas (bijvoorbeeld) de eerste regel aan.
Bewaar je wijzigingen.

Genereer de HTML bestanden en publiceer deze:

```
jb build jbdemo
jbpublish jbdemo
```

## "commit" en "push" de veranderingen naar GitHub

Selecteer links de Git-plugin. Je ziet nu bij "Changed" het gewijzigde bestand staan. (Dit kunnen er meerdere zijn.)
Je moet nu de bestanden van de wijziging klaarzetten voor de *commit*, in de "Staging Area". Klik per ""Changed" bestand dat je wilt bewaren in de bijbehorende regel op de "+": "Stage this change".

> Je hebt misschien bestanden veranderd die geen onderdeel van deze wijziging zijn, maar die je veranderd hebt om te testen, of alvast voor een andere wijziging. Deze laat je onder "Changed" staan.

In dit stadium kun je bestanden vrijelijk verplaatsen tussen "Changed" en "Staged".

Je maakt nu de "Staged" bestanden definitief (in je lokale clone-repository) door een "Commit": geef een korte beschriving in de "Summary" regel, en vul deze eventueel aan in het "Description" blok.

Nu moet je de wijziging nog "pushen" naar je GitHub repository. Klik daarvoor op het rechter "upstream" wolkje met de oranje stip (in de linker kolom bovenin).
Nu wordt je naam/wachtwoord gevraagd. Vul in plaats van je wachtwoord de *key* in die je eerder aangemaakt hebt.

Als alles goed werkt is nu je GitHub repository bijgewerkt, met (i) een eigen branch; (ii) met een gewijzigd bestand *intro.md*. Controleer op de GitHub website of dit het geval is:

* ga naar je *jbdemo* repository.
* selecteer links (bover het overzicht van de bestanden, "Code" tab) je eigen branch, in plaats van *main*.
* controleer of het bestand *intro.md* eruit ziet zoals je verwacht. (Selecteer eventueel de "raw" view.)
* je ziet op de Code pagina, boven de bestanden, een regel met de naam van je laatste *commit*. Als je daar op klikt, zie je welke wijzigingen je aangebracht hebt, in de vorm van een "diff" tussen de oude en nieuwe versie.
    * een commit wordt geïdentificeerd door de beschrijving, maar ook door een getal (hash waarde): deze zie je rechts staan.
* bekijk ook eens onder "Insights" de "Network" graph

## doe een "pull request"

Je kunt nu je wijziging(en) voorstellen aan de editors van de originele repository, in de vorm van een "pull request".
Klik op "Compare en Pull Request"; of gebruik de knop "Pull Reuests" bovenin om een nieuw pull request voor te stellen.
Selecteer in de regel "If you need to, you can also compare across forks" dat je inderdaad tussen forks wilt vergelijken.
Vervolgens moet je onder "Open een Pull Reuqest" opgeven "naar welke fork/branch" en "van welke fork/branch" deze pull request gaat.
Geef links op: keuzethemas/main en rechts: (jouw fork)/(jouw branch)
Je krijgt dan daaronder een vergelijking tussen deze versies te zien, en een melding of een automatische merge mogelijk is.
(Als een bestand in beide versies gewijzigd is, heb je een *merge conflict*. Dat is voorlopig voor gevorderden.)

* geef een korte beschrijving in de bovenste regel;
* en een toelichting in het "Leave a comment" blok;
* en klik op "Create Pull Request".

De editors van keuzethemas/jbdemo kunnen nu je pull request verwerken, of eventueel afwijzen. Vaak is er een discussie rond een pull request op de GitHub website. Bekijk eens de pull requests van een repository zoals https://github.com/executablebooks/jupyter-book/pulls. (Via het pull-request menu bovenin.)

## eventueel: opruimen van de branch

Als het om een eenmalige wijziging ging, en het pull-request is overgenomen (gemerged) of gesloten, dan kan de branch opgeruimd worden. Dit kun je in GitHub doen:

* in de Code tab (van je *jbdemo* repository) zie je naast de selectie van de huidige branch, een vorkje met het aantal branches. Klik daarop: je krijgt de aanwezige branches te zien. Helemaal rechts in de regel van een branch staat een prullenbak: daarmee ruim je de branch op.
* je kunt nu in Jupyter Hub de *jbdemo* (clone) bestanden opruimen. (`rm -rf jbdemo`).
* als je een volgende keer een *clone* maakt is de betreffende branch niet meer aanwezig.

## alternatief: branch laten bestaan

Je kunt er ook voor kiezen om een branch met je eigen wijzigingen te laten bestaan, bijvoorbeeld omdat je een eigen versie wilt bewaren - met een selectie van de hoofdstukken, en een eigen hoofdstuk, bijvoorbeeld.
Je kunt wijzigingen in de oorspronkelijke versie "mergen" met je eigen branch, door een pull-request te maken van het origineel naar je branch (dus net omgekeerd als hierboven). Deze pull-request kun je zelf verwerken en mergen (als er geen merge-conflicten zijn).

Er is geen beperking aan het aantal branches dat je kunt gebruiken - maar meer dan een paar wordt al snel onoverzichtelijk.

Het is handig om in je fork de "main" branch zo goed mogelijk up-to-date te houden met het origineel. Je kunt daarmee je eigen branch(es) selectief updaten. Je kunt daarvan dan ook een branch maken als je een verandering in het origineel wilt voorstellen (een tijdelijke branch per voorgesteld pull-request.)







