import time

print ("Welkom. Mijn naam is J.O.B. deze naam staat voor Joint Objective Barricade. Mijn doel als programma is de mensen laten weten over de gevaren over de buitenwereld. Daarom ben jij nu hier. Om te weten over de gevaren over wat zich tot op de dag van vandaag afspeelt. Oorlog. In deze simulatie stap jij in de schoenen van een vluchteling versie van jezelf. In deze simulatie heb je streeds twee of drie keuzes om door te gaan. Andere keuzes geven een error in het system aan. Kies dus alleen de opties die jouw worden aangeboden. Sommige keuzes sturen jou naar jouw dood. Er zijn vier eindes in deze simulatie. De vierde is het beste einde. Zoek de weg naar dat einde. In deze simulatie ga je niet dood in het echte leven. Maar andere mensen hebben hun leven helaas door dingen zoals dit verloren. Neem dit dus serieus.")
print ("Om te beginnen moet ik jouw naam weten. Typ hier je naam in.")

naam = input("typ hier je naam...> ")
print("Welkom," + naam)
time.sleep(5)

print("Bij elke keuze krijg je opties A en B of A, B en C. Tijd om een testvraag te doen.")

print("Vraag Ex1: Als jij zou vluchten, wat zou jij dan het meeste missen?")
print("A: Jouw familie")
print("B: Jouw huis")
print("C: Jouw spullen")

antwoord1 = input("Wat is je antwoord?")

if antwoord1 == 'A':
    print("Hmmm")
    print("Natuurlijk. De warmte van de mensen die jou hebben opgevoed en hielpen totdat je eindelijk voor jezelf kon zorgen en hier kon staan.")
if antwoord1 == 'B':
    print("Natuurlijk")
    print("De plek waar je naartoe kan gaan wanneer je je niet goed voelt of even weg wil van de luide geluiden van de wereld. Mijn maker zou het met jou eens zijn.")
if antwoord1 == 'C':
    print("Goed")
    print("Er is geen schaamte hierin. De dingen waar jij voor heb gespaard of misschien heb gekregen van jouw ouders toen je klein was. Kleine herrineringen. Maar gemaakt van goud.")

print("Het ziet er naar uit dat je klaar bent voor de simulatie. Neem nog even diep adem. Alles voelt echt. Maar maak je geen zorgen. Zoals ik eerder zij, je kan niet doodgaan in het echte leven, maar de simulatie stopt meteen als dat gebeurt. Neem deze situaties serieus. De simulatie geeft je altijd een paar seconden om de situatie te verkennen en de juiste keuzes te maken. De opties staan precies zoals je ze uit moet typen. Gebruik dus de Hoofdletters. Het system kan typfouten helaas nog niet aan. Dan moet het automatisch afsluiten.")
print("Alles staat gereed. Succes, " + naam)
print("Simulatie start in 3... 2... 1...")

print("Welkom in Syrië. Jij bent een rijk mens. Je leeft een vrolijk leven samen met jouw ouders, broer en zus. Je bent misschien de jongste en heb niet veel vrienden maar je ziet je leven als geweldig. Het is Maandag. Pech pech weekend weg. Je staat voor het schoolgebouw niet klaar om de dag te beginnen. Ja gaapt en een vreemd geluid begint te piepen. Je denkt dat het van jou komt maar na het gapen blijkt het dat het van de school komt.")
print(" ")

def DOOD():
    print("DOOD")
    print("Je bent doodgegaan en je hebt geen einde bereikt. Wil je het opnieuw proberen?")
    print("Ja of nee?")

    antwoordE = input("Wat is jouw antwoord?")

    if antwoordE == 'Ja':
        vraag1()
    elif antwoordE == 'Nee':
        print("SIMULATIE UITSCHAKELEN")

def eindeverhaal():
    print("EINDE BEHAALD. GEGEVENS OPGESLAGEN")
    print("TERUG NAAR DE JOINT OBJECTIVE BARRICADE. SIMULATIE UITSCHAKELEN.")
    print("“Welkom terug”" + naam)
    print("Dit was jouw verhaal naar vrijheid. Ik hoop dat je meer heb geleerd over de gevaren van haat, oorlog en bedrog. Als je meer wilt weten of als je denkt dat je niet genoeg hebt geleerd over de simulatie kan je altijd terugkomen. Dank je wel voor het meedoen. Nog een prettige dag en leef je beste leven hier in vrijheid en vrede," + naam)

def einde4():
    print("De weken daarna waren zwaar. Van krappe vluchtelingenkampen tot niets te eten te kunnen krijgen tot horen van mensen van andere landen dat we niet in hun land horen. Je zit te rusten in een tent totdat een soldaat de tent in komt. “Wakker worden, vriend.” Wat wil zij nou? “We hebben een plan voor jou en je groep. Een eindbestemming waar jij hopelijk een nieuw leven kan opbouwen. We zijn in contact gekomen met wat geweldige mensen van Nederland. Zij willen jou opvangen en alles leren wat je moet weten over het land” Een veilige plek? Het voelde alsof het jaren heeft geduurd. Maar het is eindelijk zover.")
    print("Rust. Dat is wat dit land je gegeven heeft. Je hebt een baantje goede buren… en een familie. Terwijl je op het balkon staat en geniet van het ochtend luchtje voel je dat er handen om je heen worden gedaan. Fatima staat gelukkig achter je. Het gaat steeds beter met haar. Ze weet eindelijk meer over hoe ze van haarzelf kan houden. Je draait je om en ziet ook dat Rayan zijn ogen rolt. Je kan een lach niet inhouden. Rayan heeft vlug Nederlands geleerd en is een van de beste van zijn klas. Je denkt nog steeds terug aan je eigen land en hoe graag je weer jouw eigen mensen en gebieden weer wilt zien. Maar dit is een goede plek voor nu. Hier kan je zijn wie je wil zijn. Hier is het rustig…")
    time.sleep(5)
    print("Einde 4/4: Ontsnapt!")
    print("Je hebt het gehaald. Jij, Fatima, Rayan en Amyr zijn veilig aangekomen in Nederland en bouwen nu een nieuw leven op. Het was zwaar werk om hier te kunnen wonen maar het is gelukt. Blijf hier zolang als je wilt.")
    time.sleep(5)
    eindeverhaal()

def einde3():
    print("Einde 3/4: Stuk gelopen")
    print("Je bent doodgegaan met jouw ogen gericht op iemand die je probeerde te redden. En je hebt gefaald. Je was maar een paar stappen van de kust. Maar een verkeerde beslissing kan iemands leven in stukken scheuren.")
    time.sleep(5)
    eindeverhaal()

def einde2():
    print("Twee weken later...")
    print("Jij en je broer zijn op zoek naar mensen en deze dode wildernis. Jullie lopen door de gebroken stukken van jullie huis. Hij kijkt naar een oude foto dat nog is overgebleven. Terwijl hij niet oplet pak jij jouw pistool uit jouw zak en richt het op zijn hoofd")
    time.sleep(5)
    print("Einde 2/4: Mis-leid")
    print("Je dacht dat je klaar was met dode lichamen zien. Je gaf je over, maar een keuze was niet gegeven om wel of niet mee te vechten. Dus jij geeft hun ook geen keuzes. Het grootste monster op de wereld is iemand die niets te verliezen heeft.")
    time.sleep(5)
    eindeverhaal()

def einde1():
    print("Einde 1/4: Lot")
    print("Je bent niet gevlucht. Jij blijft hier. Deze mensen hebben alles van je afgepakt. Deze harteloze mensen mogen dit land niet hebben. Jouw woude heeft jouw geest overgenomen. Het is tijd om terug te vechten.")
    time.sleep(5)
    eindeverhaal()

def vraag24():
    print("Vraag 24: Wat is jouw laatste vraag?")
    print("A: Wat ga jij nu doen?")
    print("B: Waar moet ik nu naartoe?")

    antwoord25 = input("Wat is jouw antwoord?")

    if antwoord25 == 'A':
        print("Mensen begeleiden naar veilige plekken. Kelders, kampen en ik heb net woord binnen gekregen dat een bootje bij de kust is. “Mensen begeleiden naar veilige plekken. Kelders, kampen en ik heb net woord binnen gekregen dat een bootje bij de kust is.” Plotseling hoor je geschreeuw. De meneer zegt tegen jou: “Je moet vluchten, tenminste totdat het weer veilig is. Je leven is belangrijk en waardevol. Laat deze mensen dat niet afpakken! Ga naar de kust voordat het bootje vertrekt!” Dat waren alle woorden die je nodig had. Je rent uit het huis. Na een tijdje rennen weet je niet eens meer waar je bent. Je loopt door totdat je bij een station komt. Je ziet een twee mannen op de grond liggen. Eentje heeft een kogelgat in zijn hoofd. De andere een mes in zijn hart. Je moet bijna overgeven.")
        time.sleep(5)
        vraag6()
    elif antwoord25 == 'B':
        print("“De kust is de beste optie die je hebt. Misschien is er nog plek op een bootje. De grens is te gevaarlijk.” Plotseling hoor je geschreeuw. De meneer zegt tegen jou: “Je moet vluchten, tenminste totdat het weer veilig is. Je leven is belangrijk en waardevol. Laat deze mensen dat niet afpakken! Ga naar de kust voordat het bootje vertrekt!” Dat waren alle woorden die je nodig had. Je rent uit het huis. Na een tijdje rennen weet je niet eens meer waar je bent. Je loopt door totdat je bij een station komt. Je ziet een twee mannen op de grond liggen. Eentje heeft een kogelgat in zijn hoofd. De andere een mes in zijn hart. Je moet bijna overgeven.")
        time.sleep(5)
        vraag6()

def vraag23():
    print("Vraag 23: Wat wil je nog meer vragen?")
    print("A: Wat deed mijn broer daar?")
    print("B: Ben je alleen?")

    antwoord24 = input("Wat is jouw antwoord?")

    if antwoord24 == 'A':
        print("“Broer? Shit… het spijt me om dit te zeggen maar jouw broer is verantwoordelijk voor deze aanval. Hij heeft een hoop gedaan voor zijn zogenaamde god.”")
        time.sleep(5)
        vraag24()
    elif antwoord24 == 'B':
        print("“Er zijn meer van mijn mannen nu mensen aan het helpen en terugvechten. De grenzen zijn slagvelden. Niet daar naar toe gaan.”")
        time.sleep(5)
        vraag24()

def vraag22():
    print("Vraag 22: Wat wil je vragen?")
    print("A: Wie ben jij?")
    print("B: Wat is er aan de hand?")

    antwoord23 = input("Wat is jouw antwoord?")

    if antwoord23 == 'A':
        print("“Mijn naam is Aiden. Undercover agent. Ik was op zoek naar een terrorist. En ik denk dat ik hem heb gevonden. Te laat, helaas. Het spijt me.”")
        time.sleep(5)
        vraag23()
    elif antwoord23 == 'B':
        print("“Dit is een aanval van mensen die in iemand geloven tot het punt dat ze anderen met geweld willen overhalen. Ben je tegen, ben je dood.”")
        time.sleep(5)
        vraag23()

def vraag21():
    print("Vraag 21: Nog een laatste aanval! Waar val je nu aan?")
    print("A: In zijn maag")
    print("B: In zijn benen")

    antwoord22 = input("Wat is jouw antwoord?")

    if antwoord22 == 'A':
        print("Een trap in de maag was iets waar hij op voorbereid was. Hij staat stil, pakt jouw hoofd en het enige wat je nog hoord is een KRAK.")
        time.sleep
        DOOD()
    elif antwoord22 == 'B':
        print("Je veegt hem op de grond. Nog een sterke knal op zijn gezicht en alle beweging is gestopt. Je weet niet zeker of hij nog leeft of niet. Maakt niet uit. Rayan is nog veilig. Je draait je om en ziet Rayan vol in angst. Misschien ging je overboard. Je pakt Rayan op en rent naar de kust. Soldaten wachten daar al, deze zien er een stuk vriendelijker uit. De soldaten helpen Rayan op de boot. Een soldaat roept plotseling: “jullie moeten gaan! Nu!”. De boot vertrekt en jij staat nog op de kust. Rayan kijkt naar jou. Je beweegt niet. Je gaat niet mee. Je weet niet eens of je die rit wel overleeft. Je draait je om en loopt naar de soldaten.")
        time.sleep
        einde1()

def vraag20():
    print("Vraag 20: Wil je blijven aanvallen?")
    print("A: Ja")
    print("B: Nee")

    antwoord21 = input("Wat is jouw antwoord?")

    if antwoord21 == 'A':
        print("Je blijft aanvallen totdat je vuisten rood met bloed worden worden.")
        time.sleep(5)
        vraag21()
    elif antwoord21 == 'B':
        print("Hij komt snel weer bij en pakt een mes uit zijn zak. Een slash bij je nek en je weet het zeker: je bent dood")
        time.sleep(5)
        DOOD()

def vraag19():
    print("Vraag 19: Wat nu?")
    print("A: Aanvallen")
    print("B: Verdedigen")

    antwoord20 = input("Wat is jouw antwoord?")

    if antwoord20 == 'A':
        print("Je probeert hem te slaan. Hij heeft veel meer ervaring met dit soort dingen en vangt jouw vuist. Met een knie in jouw maag val je omver. Hij pakt zijn pistool en schiet je neer.")
        time.sleep(5)
        DOOD()
    elif antwoord20 == 'B':
        print("Je weet dat hij boos is. Laat hem. Je ontwijkt zijn vuist en schiet jouw eigen vuist in zijn gezicht.")
        time.sleep(5)
        vraag20()

def vraag18():
    print("Vraag 18: Je moet vechten. Wat is jouw eerste move?")
    print("A: Schuil achter een auto")
    print("B: Gebruik een gebroken autodeur")

    antwoord19 = input("Wat is jouw antwoord?")

    if antwoord19 == 'A':
        print("Je probeert te schuilen maar Rayan wordt geraakt. Een paar meer schoten van het pistool op de auto en een explosie ontstaat en de flamen zuigen jou in het tweede leven.")
        time.sleep(5)
        DOOD()
    elif antwoord19 == 'B':
        print("Je denkt snel na en pakt een gebroken autodeur. Sommige kogels vliegen door het raam. Je rent naar voren en raakt je broer. Zijn pistool valt uit zijn handen. Je valt op je snuit en staat snel op.")
        time.sleep(5)
        vraag19()

def vraag17():
    print("Vraag 17: Neem je hem op? Dit ding verstuurd locaties door, toch?")
    print("A: Maakt niet uit. Opnemen")
    print("B: Niet opnemen en doorlopen")

    antwoord18 = input("Wat is jouw antwoord?")

    if antwoord18 == 'A':
        print("Je neemt de telefoon op. Ondanks het slechte bereik en de wegvallende stem weet je het zeker. Dit is jouw vader. Je kan maar een woord opmaken: “Ren!”. Er is een explosie geluid en het is weg. Tranen verlaten jouw ogen. Hoe kon dit gebeuren… je voelt een hand op jouw been. Rayan. Hij heeft nog een toekomst. Hij gaat voor. Met een hart met niets anders dan verbazing verdriet en woede loop je door. De kust is bijna in zicht. Jij en Rayan blijven lopen totdat je in een spiegel iemand ziet met een pistool je duwt jezelf en Rayan omver en ontwijkt een kogel. Je staat oog in oog met je broer.")
        time.sleep(5)
        vraag18()
    elif antwoord18 == 'B':
        print("Je loopt door. Je weet niet eens wat dat ding is. Plotseling hoor je een schot en een plof achter je. Rayan licht op de grond en jouw broer staat voor je. Jouw broer richt zijn pistool op je. Je houdt jouw handen omhoog en loopt langzaam naar hem toe. “Accepteer het lot dat de heer voor jou heeft gekozen, broeder.” Alle kracht verlaat jouw benen. Je vertelt jouw broer dat je hebt opgegeven. Genoeg dode lichamen heb je gezien. Je wilt rust. Je broer vangt je op en zwart heet je harte welkom.")
        time.sleep(5)
        einde2()

def vraag16():
    print("Vraag 16: Wat wil je nu doen?")
    print("A: Vraag hem meer over wie hij is.")
    print("B: Zeg dat alles goed komt")
    print("C: Zeg niets")

    antwoord17 = input("Wat is jouw antwoord?")

    if antwoord17 == 'A':
        print("Je probeert hem te overtuigen om een gesprekje met jou te voeren. Dat is geruststellend. Hij vertelt dat hij pas net 10 is geworden. Hij heeft een oudere broer, geadopteerd. Hoogstwaarschijnlijk waren zijn ouders van het westen. Een jaar geleden is hij met het leger meegegaan. Hij hoopt dat alles goed met hem komt. Je ziet een telefoon die afgaat. Deze komt bekent voor... hij van jouw zus!")
        time.sleep(5)
        vraag17()
    elif antwoord17 == 'B':
        print("Je probeert hem gerust te stellen. Er zijn vast mensen onderweg die jullie gaan helpen. “Het duurt te lang”. Hij heeft wel een punt… Je ziet een telefoon die afgaat. Deze komt bekent voor... hij van jouw zus!")
        time.sleep(5)
        vraag17()
    elif antwoord17 == 'C':
        print("Je zit nog steeds te denken over die arme man. Je kan geen woorden vormen. Je ziet een telefoon die afgaat. Deze komt bekent voor... hij van jouw zus!")
        time.sleep(5)
        vraag17()

def vraag15():
    print("15: Denk snel!")
    print("A: Pak het pistool")

    antwoord16 = input("Nu!")

    if antwoord16 == 'A':
        print("Voordat je goed kan nadenken pak je zijn pistool af. Tenminste dat probeer jij. Hij wil het verdomde wapen niet loslaten. Je blijft maar worstelen. Je hoort een schot maar je voelt niets. Mustafar valt langzaam achterover. Je bent net op tijd om hem op te vangen. Je hebt niets om hem te helpen. Je hebt hem vermoord. Mustafar grijpt jouw hand. “Het spijt me zo erg. Zij zouden mij vermoorden als ik mijn loyaliteit niet liet zien”. Hij wijst naar zijn broekzak. Je steekt je hand erin en pakt een foto eruit. Hij is samen met iemand anders. “Dat is mijn vriend. Als je hem ziet, zeg dan dat ik altijd van hem hield”. Met een laatste traan en adem verlaat hij het leven. Je kan alleen maar staren. Je hebt iemand vermoord. Je voelt een hand op je rug. Rayan. Jouw nonsense komt later nog wel. Dit jongetje heeft nog een toekomst nodig. Hij klimt op jouw rug en jullie blijven lopen. Nog een laatste blik naar de arme man die niet kon ontsnappen van een vreselijk einde. Wie in hemelsnaam zou dit doen? Na een tijdje lopen merk je dat Rayan doodstil is.")
        time.sleep(5)
        vraag16()

def vraag14():
    print("Vraag 14: Wat doe je nu?")
    print("A: Niets")
    print("B: Opstaan en wegrennen")
    print("C: Terugvechten")

    antwoord15 = input("Wat is jouw antwoord?")

    if antwoord15 == 'A':
        print("Je kan niet meer doorgaan. Je bent zo ongelofelijk moe. En wat wil jij doen? Je kan niets! Je bent gewoon een normaal mens! Je hebt geen energie meer om wakker te blijven en valt in slaap. Wanneer je wakker wordt zie je dat je in een zaal bent. Je kijkt om je heen en zit tussen een paar andere mannen en vrouwen. Je hoort wat luide gesprekken. Eentje blijft kalm en de andere is huilend aan het schreeuwen. Je wordt pas echt wakker wanneer de rustige stem een kogel door de arme ziel heen schiet. Degene met de stem draait zich om. Het is jouw broer. Hij is hier dus echt achter. Plotseling wordt het vuur geopend van buiten. Jouw broer rent weg en de deuren van “waar je ook bent” worden open getrapt. Je wordt omhoog geholpen door een man die zeker niet lijkt op iemand die van jouw land komt. “Rustig aan. Ik neem aan dat je een hoop vragen hebt.”")
        time.sleep(5)
        vraag22()
    elif antwoord15 == 'B':
        print("Moven? Yep! Klinkt goed! Klinkt goed. Je blijft rennen over de baan. Voelt raar. Je loopt uit het station en rent over een brug. Je kijkt om je heen. Als dit een videogame geweest zou zijn zou dit nog leuk zijn. Maar dit is echt. Je kan geweer geluiden en gehuil nog horen en de lucht ziet er uit alsof de wereld vergaat. Zo voelt het tenminste. Je blijft lopen en denkt na over wat die man zij. Je hebt geen gids meer. Wat nu? Het enige waar je over denkt is de kust. Hebben ze een boot? Moet ik echt vluchten op een klein bootje? Niet zeiken! Beter dan niets. Alles beter dan hier blijven. Maar nu je alleen bent en adem kunt halen denk je na. Dit is mijn land. Mijn familie is hier. Daarover gesproken, wat deed mijn broer? Duizenden vragen gaan door jouw hoofd. Concentreren! Je moet stappen maken! Je hebt niet eens een wapen! Je hoort ineens gekraak. De brug stort in! Hebben ze bommen geplaatst?! Je heb niet eens meer de kans om te denken. De vloer onder je voeten breekt en je valt. De val is lang en de pijn is onwerkelijk. Je ligt op jouw rug en je kijkt omhoog naar waar je eerst stond. Het laatste wat je ziet een een stuk van de brug dat naar jou toe valt. Het is groter dan jou. Je hoort nog een bloederig geluid en alles gaat zwart.")
        time.sleep(5)
        DOOD()
    elif antwoord15 == 'C':
        print("Je hoofd kon geen antwoorden meer bedenken en je draait je om en rent naar je broer. Een schot kon je horen en je glijd door naar het volgende leven,")
        time.sleep(5)
        DOOD()

def vraag13():
    print("Vraag 13: Welke weg ga je naartoe?")
    print("A: Rechts")
    print("B: Links")
    print("C: Rechtdoor")

    antwoord14 = input("Wat is jouw antwoord")

    if antwoord14 == 'A':
        print("Mustafar wijst naar rechts. Klinkt oké, hij weet de weg wel. Na een tijdje lopen merk jij dat het niet lijkt dat iets opschiet. Alles wat je ziet zijn lege huizen en kapotte auto’s. Geen mens in zicht. Hij houd zijn hand omhoog en jij en Rayan stoppen. Hij draait zich ineens om en richt een pistool op jouw. Rayan schuilt zich achter jou.")
        time.sleep(5)
        vraag15()
    elif antwoord14 == 'B':
        print("Je voelt een gevoel in jouw maag dat je die kant op moet. Je belooft de anderen straks weer te zien. Oké. Ziet een mes en een pistool liggen. Je pakt ze op. Geen andere keuze meer. Je blijft doorlopen totdat je een meisje ziet zitten. Ze mompelt zegen haarzelf.")
        time.sleep(5)
        vraag6()
    elif antwoord14 == 'B':
        print("Je hoort een geluid recht voor je. Je loopt naar voren en kijkt om je heen. Je hoort plotseling een gil van Rayan. Voordat je jezelf volledig kon omdraaien, een shot is dwars door je heen gevuurd")
        time.sleep(5)
        DOOD()

def vraag12():
    print("Vraag 12: Wil je vluchten?")
    print("A: Ja")
    print("B: Nee")

    antwoord13 = input("Wat is je antwoord")

    if antwoord13 == 'A':
        print("Je grijpt Amyr’s hand en hij trekt je in de boot. Net op tijd. Er was bijna geen grond meer om op te rennen. Je zit neer naast Fatima, die Rayan probeert te kalmeren. Dit kan een lange reis worden.")
        time.sleep(5)
        einde4()
    elif antwoord13 == 'B':
        print("Je begint langzamer te rennen. Je wilt niet vluchten. Je familie, jouw thuis jouw… gedachten worden ineens onderbroken wanneer iemand jouw hand vastgrijpt. Het is Fatima. “Niet hier!” Amyr en Rayan helpen haar om jou de boot in de dragen. Je wil niet vluchten. Maar deze mensen… als je met deze groep bent is de wereld aangaan misschien niet zo erg.")
        time.sleep(5)
        einde4()

def vraag11():
    print("Vraag 11: Je bent er bijna! Wat doe je nu?")
    print("A: Rennen")
    print("B: Mes gebruiken")

    antwoord12 = input("Wat is jouw antwoord?")

    if antwoord12 == 'A':
        print("Je rent voor jouw leven maar een kogel gaat dwars door jouw rug heen. Fatima wordt daarna geraakt. Jullie vallen op de grond. Je ziet al dat Fatima al niet meer leeft. De kust was voor jullie, de zon breekt door en jij probeert met jouw hand die van Fatima te bereiken. Je faalt. Je hebt gefaald. Het laatste wat je ziet en hoort is Fatima’s gezicht, hoe je haar niet heb kunnen bereiken. Het laatste wat je hoort zijn mannen die het vuur openen. Iemand voelt aan je nek. “Hij is dood.”")
        time.sleep(5)
        einde3()
    elif antwoord12 == 'B':
        print("Je pakt jouw mes uit jouw zak en gooit het met alle kracht naar jouw broer. Raak. Het mes is recht in zijn schedel beland. Langzaam valt jouw broer achterover op de grond. Je kan jezelf nauwelijks geloven. Binnen een dag zijn jullie van beste vrienden naar oorlogs vijanden gegaan. Je kan je tranen niet inhouden. Fatima geeft je een knuffel. Vreemd. Een vreemdeling geeft meer om je dan jouw eigen broer. Nee… een broer is iemand van jouw familie. En familie geeft alles voor elkaar. Dit was jouw broer niet. Maar dat verandert niet dat je zojuist iemand hebt vermoord. Je hoort voetstappen. Je draait je om en ziet 3 gewapende mannen. Maar deze zien er niet uit als jouw broer. Soldaten? Eentje begint te spreken. “Oké. Jullie zijn de laatste. Mijn naam is Jack en ik moet jullie naar de kust brengen. Vanaf daar kunnen jullie met een bootje vluchten. Sorry. Dit is de enige weg.” Godzijdank. Na een tijdje lopen komen jullie eindelijk aan bij de kust. Jullie zien het bootje al. Er zijn veel mensen erop maar niet te veel. Zijn er echt zoveel doden gevallen? Een volwassen man begroet jullie. “Hoi. Mijn naam is Amyr. En dit is Rayan. Hij heeft zijn familie verloren. Kunnen jullie op hem letten?”. Fatima glimlacht en welkom Rayan met open armen. Bijda stappen in het bootje. Amyr kijkt nog even achteruit. Je vraagt of er iets aan de hand is. “Huh? Nou ja, ik heb iemand verloren. Misschien hadden we iets kunnen zijn.” Langzaam stapt Amyr op het bootje. “We hebben niet veel tijd meer. Jullie moeten gaan nu!” Een van de soldaten geeft de boot al een zetje. Je bent nog niet ingestapt! Je rent achter de boot aan. Amyr strekt zijn hand uit. Maar iets in jouw hoofd vraagt iets.")
        time.sleep(5)
        vraag12()

def vraag10():
    print("“Voeg je jezelf bij ons toe?”")
    print("A: Ja")
    print("B: Nee")
    
    antwoord11 = input("Wat is jouw antwoord?")

    if antwoord11 == 'A':
        print("Je haalt jouw handen omhoog. Je bent er klaar mee. Je bent geen vechter, geen strijder, wat wil je doen? Zo snel mogelijk jouw broer neerschieten? Dat kan jij niet. Je draait je om naar Fatima Oh. Ze is weg. Waar is ze naartoe gegaan? Je hoort ineens het geluid van een geweer. Verdomme… dat was jouw laatste lichtpuntje in deze duisternis. Voordat je helder kan nadenken draai jij je om naar jouw broer en probeer je hem te slaan. Je had je juist niet naar achter moeten gooien. Een kogel wordt tussen je ogen gestopt.")
        time.sleep(5)
        DOOD()
    elif antwoord11 == 'B':
        print("Voordat je iets zegt kijk je naar Fatima. Ze is een paar stappen naar achteren gegaan. Ze kan nauwelijks stilstaan. Kent ze jouw broer. Toen ineens komt een pijnlijke herinnering terug in jouw hoofd. Jouw broer was gearresteerd omdat hij slecht omging met vrouwen. Je dacht dat het maar gewoon een stalker probleem was. Maar nu niet meer. Dit arme onschuldige meisje… zij… jouw broer. Oh god… “we kunnen weer samen zijn.” zegt jouw broer die langzaam dichterbij komt. Samen zijn? Je wil een huis delen met dat monster?! Iets in jouw brein kan dit niet meer aan en je pakt jouw pistool uit je zak en schiet jouw broer in je arm. Zijn pistool valt uit zijn hand. Je hebt geen kogels meer maar dat maakt niet uit. Je tackelt hem omver en maak gebruik van jouw vuisten. Je bent woest. Alles wat jij en jouw broer samen hebben gedaan is omver gegooit. Je stopt niet met beuken. Alles wat je ziet is rood. Je blijft schreeuwen over wat een monster hij is. Hoe heeft hij dit kunnen doen? Tegen een onschuldig meisje. Tegen zijn eigen broer? Plotseling wordt jouw vuist gegrepen door iemand. Je kijkt om en ziet dat Fatima je stopt. Natuurlijk. Je wil niet zo geweldig dadig worden als jouw broer. Maar het voelde alsof je dit nodig had. Je staat op. Jouw broer beweegt voorlopig niet. Jullie lopen verder. Maar na heel even lopen staat jouw broer gewoon weer op.")
        time.sleep(5)
        vraag11()

def vraag9():
    print("Vraag 9: Waar wil je nu naartoe?")
    print("A: Links")
    print("B: Rechts")

    antwoord10 = input("Wat is jouw antwoord?")

    if antwoord10 == 'A':
        print("Doorlopen. Maar tijdens het lopen hoor je ineens een geladen pistool. Je draait je langzaam om. Waarom is er niet geschoten? Je ziet wie het pistool vasthoud. Jouw bloedeigen broer. Hij heeft die man doodgeschoten. En aan zijn vest te zien was dat niet de laatste. Je vraagt hem wat er aan de hand is. “(Naam). Je gelooft niet. In de naam van de heer moet ik jou hier eindigen. Laatste kans...”")
        time.sleep(5)
        vraag10()
    elif antwoord10 == 'B':
        print("Jij en Fatima rennen zo snel als je kunt naar wat je denkt de goede richting is. Je hoort ineens een raar geluid van achteren. Geblaf. Er zitten honden achter je aan. Je wordt getackelt en tot stukken gescheurt. Een langzame, pijnlijke...")
        time.sleep(5)
        DOOD()

def vraag8():
    print("Vraag 8: Vanaf waar wil je schieten?")
    print("A: Vanaf het dak")
    print("B: Van links")
    print("C: Van rechts")

    antwoord9 = input("Wat is jouw antwoord?")

    if antwoord9 == 'A':
        print("Je begint te schieten. Maar je hebt te laat door dat het geweer van jouw vijand veel sneller is. Je voelt een paar duizend kleine kogels door jouw hoofd vliegen. Alle gedachtes verlaten je en het laatste wat je voelt is de koude vloer die je welkom heet tot de dood.")
        time.sleep(5)
        DOOD()
    elif antwoord9 == 'B':
        print("Je wacht heel even totdat je snel langs de zijkant van de auto springt en schiet. Ondanks dat je geen ervaring heb, jouw kogel raakt en de man valt neer. Je helpt Fatima op en gaat door met rennen. Je staat op een heuvel en kijkt naar voren. Daar is een kust. Als je geluk hebt kan je daar een bootje regelen. Maar je moet opschieten. Zo makkelijk gaat dit niet. Je wilt weer rennen maar je draait je om en ziet dat Fatima gelukkig naar een kinderpark kijkt. Die glimlach. Iets zoals dat had je gemist. Je pakt rustig haar hand en geeft aan dat jullie weer moeten rennen. Haar lacht valt weg. Ouw. Die voelde je in je hart. Je kan het wel voorstellen. De onschuldigheid van een kind. Is dat wat er met haar is gebeurd? Heeft ze iets slechts gedaan? Je wilt het nu niet weten. Je blijft lopen, rennen en schuilen als je weer iemand ziet. Fatima volgt jou gewoon. Er worden niet eens vragen gesteld. Dit gaat te makkelijk. Wat is er aan de hand? Je blijft doorrennen. Een splitsing komt op.")
        time.sleep(5)
        vraag9()
    elif antwoord9 == 'C':
        print("Je wacht heel even totdat je snel langs de zijkant van de auto springt en schiet. Ondanks dat je geen ervaring heb, jouw kogel raakt en de man valt neer. Je helpt Fatima op en gaat door met rennen. Je staat op een heuvel en kijkt naar voren. Daar is een kust. Als je geluk hebt kan je daar een bootje regelen. Maar je moet opschieten. Zo makkelijk gaat dit niet. Je wilt weer rennen maar je draait je om en ziet dat Fatima gelukkig naar een kinderpark kijkt. Die glimlach. Iets zoals dat had je gemist. Je pakt rustig haar hand en geeft aan dat jullie weer moeten rennen. Haar lacht valt weg. Ouw. Die voelde je in je hart. Je kan het wel voorstellen. De onschuldigheid van een kind. Is dat wat er met haar is gebeurd? Heeft ze iets slechts gedaan? Je wilt het nu niet weten. Je blijft lopen, rennen en schuilen als je weer iemand ziet. Fatima volgt jou gewoon. Er worden niet eens vragen gesteld. Dit gaat te makkelijk. Wat is er aan de hand? Je blijft doorrennen. Een splitsing komt op.")
        time.sleep(5)
        vraag9()

def vraag7():
    print("Vraag 7: Wil je het meisje proberen over te halen om mee te gaan?")
    print("A: Ja")
    print("B: Nee")

    antwoord8 = input("Wat is jouw antwoord?")

    if antwoord8 == 'A':
        print("Genoeg nu. Je pakt haar hand en tilt haar omhoog. Je neemt haar mee. Ze heeft niet veel energie maar het ziet er niet naar uit dat ze haar eigen beslissingen kan maken. Wat hebben die mensen in vredesnaam met haar gedaan. Dit meisje heeft hulp nodig maar een ding is zeker. Dit is de slechtste optie. Na even tot rust te komen in een steegje vraag je naar haar naam. Ze reageert met een zwak stemmetje. “Fatima”. Oké. Ze spreekt. Goed! Je blijft doorlopen en probeert een beetje meer te communiceren met Fatima. Langzaam ziet het er naar uit dat ze jou kan vertrouwen. Je blijft doorlopen totdat het vuur van achteren wordt geopend. Jij en Fatima duiken meteen achter een auto. Je pakt jouw pistool uit jouw zak.")
        time.sleep(5)
        vraag8()
    elif antwoord8 == 'B':
        print("Oké! Dit duurt te lang! Tijd om te rennen. Verkeerde optie. In jouw haast heb niet door dat je recht in de armen van een terrorist loopt. Voordat je kan kijken hoe hij of zij eruit ziet zit er al een kogel in jouw brein.")
        time.sleep(5)
        DOOD()

def vraag6():
    print("Vraag 6: Neem jij de wapens mee?")
    print("A: Ja")
    print("B: Nee")

    antwoord7 = input("Wat is jouw antwoord?")

    if antwoord7 == 'A':
        print("Elke instinct in jouw lichaam zegt dat je dit niet moet doen. Maar mensen zijn doodgegaan. Beste idee is om deze wapens aan te pakken en door te lopen. Je hebt door dat de schreeuwende stad ineens helemaal stil is geworden. Je kan jouw eigen hart horen. Ineens is jouw favoriete stad een ghost town geworden. Wakker worden! Of die “spoken” pakken jou! Je pakt het mes en het geweer. Lekker. Bloed aan je handen. Dit laat jij nooit meer gaan. Je blijft lopen en rondkijken. Je mag misschien wel gewapend zijn maar dat betekent letterlijk niets tegen een groep. Je blijft rondkijken en ziet iemand in een straat met haar hoofd in haar benen. Ze leeft nog maar ze ziet er niet goed uit. Je loopt naar het meisje toe en vraagt wat er is gebeurt. Ze kijkt omhoog. In eerste instantie zien die ogen er prachtig uit. Maar aan de andere kant zie je dat ze leeg zijn. Alle emotie en licht dat die ogen ooit uitstraalde is verdwenen. Ze is depressief. Was ze dit al voordat… dit gebeurde? Je kan haar niet laten zitten. Je offert haar jouw hand. “Laat me doodgaan.” Je zegt dat het niet hier hoeft te eindigen. Ze luistert niet. Je hoort ineens voetstappen.")
        time.sleep(5)
        vraag7()
    elif antwoord7 == 'B':
        print("Je kan het niet aan. Jouw ontbijt komt naar boven. Je rent de andere kant op. Je rent een paar trappen af en komt een man en een kind tegen. Je begroet ze. De man, Mohammed zegt dat je met hem en het kind, Rayan, mee moet gaan voor veiligheid. Tuurlijk accepteer je dat!")
        time.sleep(5)
        vraag13()

def vraag5():
    print("Vraag 5: Neem jij het jongentje mee?")
    print("A: Ja")
    print("B: Nee")

    antwoord6 = input("Wat is jouw antwoord?")

    if antwoord6 == 'A':
        print("Je rent naar het jongetje toe en vraagt wat er aan de hand is. Hij wijst naar een klein ingestort huis. Zijn familie zat daar. Je laat het jongetje op jouw rug en laat je rugzak achter. Geen andere keuze. Je blijft rennen totdat je een man ziet die met handgebaren duidelijk maakt dat hij vriendelijk is. “Hoi, ik heb een vriend die jullie kan helpen vluchten.” De jongen kijkt droevig naar de man en vraagt “waar naartoe?”. “Het land uit. Het is hier niet meer veilig”. Dus zo erg is het. Je moet jouw eigen land uit. “Wat is jouw naam, kleine man?” “Rayan”. “Hallo, Rayan. Ik ben Mustafar. Ik ga jullie naar mijn vriend brengen. Vanaf daar kunnen jullie het zelf wel verder vinden.” Jullie gaan de schuilplaats uit en lopen door. Er zijn drie wegen die jullie op kunnen.")
        time.sleep(5)
        vraag13()
    elif antwoord6 == 'B':
        print("Nee. Je bent zelf al een makkelijk doelwit. Zeg dat wel. Voordat je kunt rennen wordt je in jouw achterhooft geschoten en gaan alle lichten uit.")
        time.sleep(5)
        DOOD()

def vraag4():
    print("Vraag 4: Waar ga je naartoe?")
    print("A: Rechts vooruit")
    print("B: Links vooruit")
    print("C: Hier blijven")

    antwoord5 = input("Wat is jouw antwoord")

    if antwoord5 == 'A':
        print("Klinkt goed. Je blijft lopen over de baan. Voelt raar. Je loopt uit het station en loopt over een brug. Je kijkt om je heen. Als dit een videogame geweest zou zijn zou dit nog leuk zijn. Maar dit is echt. Je kan geweer geluiden en gehuil nog horen en de lucht ziet er uit alsof de wereld vergaat. Zo voelt het tenminste. Je blijft lopen en denkt na over wat die man zij. Je hebt geen gids meer. Wat nu? Het enige waar je over denkt is de kust. Hebben ze een boot? Moet ik echt vluchten op een klein bootje? Niet zeiken! Beter dan niets. Alles beter dan hier blijven. Maar nu je alleen bent en adem kunt halen denk je na. Dit is mijn land. Mijn familie is hier. Daarover gesproken, wat deed mijn broer? Duizenden vragen gaan door jouw hoofd. Concentreren! Je moet stappen maken! Je hebt niet eens een wapen! Je hoort ineens gekraak. De brug stort in! Hebben ze bommen geplaatst?! Je heb niet eens meer de kans om te denken. De vloer onder je voeten breekt en je valt. De val is lang en de pijn is onwerkelijk. Je ligt op jouw rug en je kijkt omhoog naar waar je eerst stond. Het laatste wat je ziet een een stuk van de brug dat naar jou toe valt. Het is groter dan jou. Je hoort nog een bloederig geluid en alles gaat zwart.")
        time.sleep(5)
        DOOD()
    elif antwoord5 == 'B':
        print("Klinkt goed. Je blijft lopen over de baan. Voelt raar. Je loopt uit het station en loopt over een brug. Je kijkt om je heen. Als dit een videogame geweest zou zijn zou dit nog leuk zijn. Maar dit is echt. Je kan geweer geluiden en gehuil nog horen en de lucht ziet er uit alsof de wereld vergaat. Zo voelt het tenminste. Je blijft lopen en denkt na over wat die man zij. Je hebt geen gids meer. Wat nu? Het enige waar je over denkt is de kust. Hebben ze een boot? Moet ik echt vluchten op een klein bootje? Niet zeiken! Beter dan niets. Alles beter dan hier blijven. Maar nu je alleen bent en adem kunt halen denk je na. Dit is mijn land. Mijn familie is hier. Daarover gesproken, wat deed mijn broer? Duizenden vragen gaan door jouw hoofd. Concentreren! Je moet stappen maken! Je hebt niet eens een wapen! Na een tijdje lopen kom je aan bij het volgende station. Je ziet een twee mannen op de grond liggen. Eentje heeft een kogelgat in zijn hoofd. De andere een mes in zijn hart. Je moet bijna overgeven.")
        time.sleep(5)
        vraag6()
    elif antwoord5 == 'C':
        print("Alle kracht in jouw benen hebben je verlaten. Je kan niet meer. Je broer komt naar beneden met een geladen geweer. Je vraagt je af waarom hij dit doet. “(Naam), je gelooft niet in de heer die ons leven geeft. Kom bij ons en je hoeft niet te sterven.” Is hij gestoord? Hier kan het niet bij eindigen, toch?")
        time.sleep(5)
        vraag14()

def vraag3():
    print("Vraag 3: Wat doe je?")
    print("A: Bij de man blijven")
    print("B: Hallo zeggen tegen jouw broer")

    antwoord4 = input("Wat is jouw antwoord?")

    if antwoord4 == 'A':
        print("Met pijn in jouw hart blijf je achter de auto. Er is hier iets mis en je vertrouwt het niet. Hij kijkt de andere kant op. Er komen andere mensen aan. “We moeten NU gaan!” fluister schreeuwt de man. Opstaan en rennen. Je ziet een Metrostation! Ren erin en je bent veilig! Je bent er bijna maar je broer draait om en ziet jullie rennen. Het laatste wat je verwacht gebeurt. Je richt op jou en schiet. De man springt voor jou en wordt geraakt. De man valt nadat hij nog een keer zegt: “Blijf gaan! Jij kunt het halen!!” Je bent geschrokken maar de adrenaline laat je niet stoppen met rennen. Je rent het Metrostation in en ontwijkt nog net een kogel. Je valt van de trap maar je voelt niets. Een man is net doodgegaan om jou te beschermen! Jij kende hem niet eens! Je wist zijn naam niet eens! Je komt het station binnen en meteen zie je al een probleem. Alle stroom is kapot. Het beste wat je kan doen is een route kiezen en dan verder lopen.")
        time.sleep(5)
        vraag4()
    elif antwoord4 == 'B':
        print("Het is jouw broer. Wat kan er fout gaan. Je loopt van de auto vandaan en roept zijn naam. Hij draait zich om met een blik die jij nog nooit gezien hebt. Hij richt, schiet en alle gevoel in je lichaam verlaat jou.")
        time.sleep(5)
        DOOD()


def vraag2():
    print("Vraag 2: Ga je met hem mee?")
    print("A: Ja")
    print("B: Nee")

    Antwoord3 = input("Wat is jouw antwoord?")    

    if Antwoord3 == 'A':
        print("Alles beter dan achter een auto helemaal alleen sterven. Je rent zo snel als je kunt en bereikt het hoekje zonder dat de gewapende mannen jou kunnen vangen. “Kom mee. Ik heb een klein groepje dat je meeneemt” zegt de meneer. Tijdens het rennen zie jij jouw broer staan. De man neemt jou mee en schuilt achter een auto. “Hij heeft een geweer” zegt de man.")
        time.sleep(5)
        vraag3()
    elif Antwoord3 == 'B':
        print("Je vertrouwt het niet en blijft liggen. En je bent ook verstijfd van de angst. Maar voordat je kan nadenken wordt een bom gegooid. Je ziet het maar kan niet bewegen. Er is een grote explosie en alles wordt in een tel zwart.")
        time.sleep(5)
        DOOD()


def vraag1():
    print("Vraag 1: Wat doe je nu?")
    print("A: Op onderzoek uit gaan")
    print("B: Teruglopen")
    antwoord2 = input("Wat is jouw antwoord?")
    if antwoord2 == 'A':
        print("Een vreemd gevoel in jouw maag zegt dat je moet doorlopen en uitzoeken wat er aan de hand is. Wat kan er misgaan? Vraag jij jezelf af. Je krijgt het antwoord meteen. De school ontploft en de kracht van de knal duwt je omver. Momenten van jij met jouw vriendengroep vliegen voor jouw ogen. Je probeert weer op te staan en rent weg. Waar naartoe? Wie weet. Alles behalve hier. Na een stukje rennen kom je in een straat terecht maar verschuilt jezelf snel achter een auto. Mensen met geweren lopen door de straat. Hoe is dit gebeurt? Wat gebeurt er? Hoe zit het met mijn familie? Je kijkt voor je uit en ziet een man om de hoek met handgebaren duidelijk te maken dat je met hem mee moet gaan.")
        time.sleep(5)
        vraag2()
    elif antwoord2 == 'B':
        print("Je vertrouwt dit niet. Je loopt met een slecht gevoel weer terug. Je besluit je maar ziek te melden als je thuis bent. Halverwege met het lopen hoor je een keiharde explosie. De plek waar jouw school stond is opgegaan in vlammen. Je hoort geschreeuw en gegil. Je moet rennen. Elke plek in de wereld klinkt beter dan dit. Je blijft rennen en ziet een jongetje huilen.")
        time.sleep(5)
        vraag5()

vraag1()