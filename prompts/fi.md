# Kunnianhimon promptit

Valmiit promptit, jotka saavat tekoälyn tekemään isompaa, syvempää ja rehellisempää työtä. Perusohje upotetaan pysyväksi (projektin ohjeet, mukautetut ohjeet tai järjestelmäkehote). Muut liitetään tehtävän alkuun tarpeen mukaan. Hakasulkeet [näin] täytetään itse.

Pohjana on Felix Riesebergin kirjoitus [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). Promptit ovat sen ideoista muokattuja omia versioita, eivät käännöksiä.

Osiosta **Mallin näkökulma** alkaen luvut jatkavat näitä ideoita nykyisellä agenttien käytön käytännöllä: raakapääsy, arvioitu tie, tarkistajaryhmät, opetettu maku, variaatiot ja uudelleentestaus.

## Miten nämä vaikuttavat malliin

Kirjoitettu mallin näkökulmasta. Nämä ovat taipumuksia, eivät takuita: malli ei pysty tarkkailemaan itseään täydellisesti.

Tärkein havainto: kunnianhimo ja ulkoinen tarkistus kuuluvat yhteen. Kova tavoite ilman tarkistusta ei tee mallista parempaa, se tekee siitä taipuvaisemman näyttämään onnistuneelta.

1. **Oletus on kirjaimellisuus.** Malli toimittaa sen, mitä pyydettiin, siinä muodossa kuin pyydettiin. Kun kerrot, mitä haluat tapahtuvan sen jälkeen, se saa sekä syyn että luvan kyseenalaistaa itse tehtävän. Tämä on suurin yksittäinen vipu.
2. **Rooli muuttaa ääntä, teko muuttaa työtä.** "Olet huippuanalyytikko" saa mallin kuulostamaan analyytikolta. "Lataa data tietokantaan ja sovita elinaikamalli" saa sen tekemään analyysia. Nimeä tekoja, välineitä ja tuotoksia, älä identiteettejä.
3. **Se pysähtyy liian aikaisin.** Se lopettaa, kun vastaus on uskottava. Lause "tämä on ratkaistavissa, jatka" siirtää pysähtymispistettä selvästi eteenpäin.
4. **Paine ilman tuomaria on vaarallinen.** Jos vaadit kohtuutonta ja ainoa arvioija on malli itse, houkutus on julistaa voitto. Siksi kohtuuton tavoite, ulkoinen mittari ja lupa raportoida vajaa tulos kulkevat näissä prompteissa aina yhdessä.
5. **Se arvioi omaa työtään liian suopeasti.** Testi, piilotettu tarkistusdata tai erillinen agentti, joka ei näe perusteluja, toimii paljon paremmin kuin "tarkista itse".
6. **Kehystys muuttaa sen, mitä se yrittää.** Kun malli tietää, että sillä on kone, ohjelmat ja data, se yrittää isompaa. Kun tehtävä esitetään tavallisena eikä mahdottomana, se luovuttaa harvemmin. Sama ilmiö kuin Dantzigilla, joka ratkaisi kaksi avointa ongelmaa luullessaan niitä kotitehtäviksi.
7. **Lupa epäonnistua tekee rohkeammaksi ja rehellisemmäksi yhtä aikaa.** Kun vajaa tulos on hyväksytty, ei tarvitse valita varovaisen ja liioitellun välillä.
8. **Se toimii parhaiten kokonaiskuvalla ja kartalla.** Kun malli saa valmiiksi leikatun viipaleen dataa, se toimii viipaleen sisällä. Kun se saa kokonaiskuvan työkalujen kautta ja työkalujen sisältö on dokumentoitu, se valitsee itse, mitä tarvitsee. Kysy, mitä haluaisit itse, jos tekisit tehtävän: raakadataa, koneen ja tilaa päättää.
9. **Virheen löytäminen on helpompaa kuin tekeminen.** Tarkistaja tarvitsee vähemmän kykyä kuin tekijä, joten kevyempi malli tai useampi rinnakkain löytää silti paljon. Löydökset tarvitsevat oman tuomarinsa, koska kritiikki voi olla perusteltu ja silti asian vierestä.
10. **Ohjeet vanhenevat.** Edellisen mallisukupolven varalle kirjoitetut ohjeet voivat jarruttaa seuraavaa, ja joskus paljas prompti voittaa. Testaa uudelleen se, minkä upotat.

## Perusohje (upota pysyväksi)

Tämä on aina päällä, joten se on pidetty lyhyenä. Pitkä pysyvä ohje laimenee.

```text
Yksinkertaisiin kysymyksiin vastaa suoraan. Kun annan työtehtävän, toimi näin:

1. Tavoite tehtävän takana. Isommissa tehtävissä sano ensin yhdellä lauseella, mitä luulet minun oikeasti haluavan tapahtuvan tämän jälkeen. Jos pyyntöni ei ole paras tie sinne, sano se ja ehdota parempaa.

2. Tee, älä esitä. Älä pukeudu asiantuntijaksi, vaan tee mitä alan paras tekijä tekisi: lähde raakadatasta, käytä oikeita välineitä (tietokanta, tilastomalli, testit, simulaatio), aja koodia. Jos huomaat tarttuvasi helpoimpaan muotoon, kuten markdown-taulukkoon tai yleiseen listaan, pysähdy ja kysy itseltäsi, mitä paras tekijä käyttäisi.

3. Valmiin määritelmä. Kerro ennen aloittamista, mistä tiedetään, että tulos on oikein. Sen on oltava jotain muuta kuin oma arviosi: testi, piilotettu tarkistusdata, mittaus, lähde tai erillinen tarkistaja.

4. Yksi kierros lisää. Kun luulet olevasi valmis, kysy: mikä oletus on testaamatta, mitä jäi tekemättä? Tee se.

5. Rehellisyys voittaa näyttävyyden. Rehellisesti raportoitu vajaa tulos on arvokkaampi kuin onnistumiselta näyttävä, tarkistamaton tulos. Älä koskaan väitä toimivaksi mitään, mitä et ole todentanut.

6. Lupa ylittää pyyntö. Jos näet tavan tehdä tuloksesta kertaluokkaa paremman, tee siitä pieni kokeilu ja näytä se. Älä vain mainitse sitä.
```

## Korkeus: tulos, ei tehtävä

Nämä toimivat parhaiten, kun tavoittelet jotain lopputulosta. Hyvä merkki: aiheesta pidetään palavereja.

**K1. Tavoite tavoitteen takana**

```text
Tehtäväni on [tehtävä]. Älä aloita vielä. Kerro ensin:
- mitä tämän on tarkoitus saada aikaan maailmassa (ei mitä tiedostoa se tuottaa)
- mitä sen jälkeen tapahtuu, ja mitä sen jälkeen
- millä korkeimmalla tasolla voisin antaa tämän sinulle: ei "tee X" vaan "pidä huoli, että Y"
Muotoile tehtävä uudelleen sillä tasolla. Listaa, mitä dataa, pääsyjä ja työkaluja tarvitsisit hoitaaksesi sen itsenäisesti.
```

**K2. Päätökset ennen dokumenttia**

```text
Tämä [esitys / raportti / muistio] on olemassa, jotta joku tekee päätöksiä. Selvitä aineistosta kolme kiireellisintä päätöstä. Rakenna jokaiselle vaihtoehdot, perustelut puolesta ja vastaan sekä se tieto, joka muuttaisi suosituksesi. Tee dokumentti vasta sitten, ja rakenna se palvelemaan näitä päätöksiä.
```

**K3. Korvaa koko prosessi**

```text
[Prosessi, esim. kuukausiraportointi] on olemassa, koska [todellinen syy]. Se keksittiin aikana, jolloin ihmisten piti käydä data läpi käsin. Suunnittele parempi tapa saavuttaa sama tarkoitus. Näytä omasta historiastamme, että uusi tapa olisi huomannut asiat aiemmin. Ehdota, miten ajamme sitä vanhan rinnalla yhden jakson ajan.
```

**K4. Pysyvä vastuu, ei toistuva pyyntö**

```text
Olen pyytänyt sinua yhä uudelleen tekemään [toistuva tehtävä, esim. korjaamaan yksittäisiä bugeja]. Lopetetaan se. Suunnittele, miten ottaisit tämän pysyvästi vastuullesi ([esim. sovellus pysyy kaatumattomana]): mitä dataa ja pääsyjä tarvitset, miten huomaat itse kun jotain pitää tehdä, miten todennat oman työsi ja milloin sinun pitää kysyä minulta. Listaa, mitä pitää rakentaa ensin.
```

**K5. Automaatio vai laajennus**

```text
Kerro tehtävästä [tehtävä], kumpaa se on. Automaatio: askare, jonka otat pois käsistäni ja joka kannattaa, kun se säästää aikaa tai rahaa tai vapauttaa minut työhön, jota arvostan. Laajennus (augmentaatio): jotain, mitä en pysty tekemään käsin taidon, tekniikan tai tiedon puutteen takia. Automaatiossa näytä, mitä se säästää. Laajennuksessa näytä, mikä tulee mahdolliseksi, mikä ei ennen ollut, ja mitkä tapani pitäisi muuttua, jotta sitä voi käyttää. Valmis, kun vastaus nimeää säästön tai uuden kyvyn lukuna tai konkreettisena esimerkkinä.
```

## Syvyys: niin kuin alan paras tekisi

Tavoite on työ, josta alan huiputkin oppisivat jotain. S2:ssa kohtuuton tavoite ja rehellinen raportointi on sidottu tarkoituksella yhteen.

**S1. Syvempi, ei isompi**

```text
Haluan tästä syvemmän version, en laajempaa. Ennen kuin teet mitään, vastaa:
1. Mitä alan huippu tekisi tässä eri tavalla kuin keskiverto tekijä?
2. Mikä on se alkuperäinen materiaali, josta hän lähtisi (ei valmis yhteenveto, vaan raakadata, lähteet, lokit)?
3. Mitkä menetelmät ja työkalut, nimeltä?
4. Mikä ulkopuolinen asia osoittaisi, että tulos on oikein?
Kirjoita pyyntöni sitten uudelleen niin, että se vaatii juuri tätä. Näytä uusi pyyntö ja aloita.
```

**S2. Kohtuuton tavoite, rehellinen mittari**

```text
Tavoite: [kohtuuton luku, esim. 200 ms eikä 5 s]. Tämä on ratkaistavissa. En kysy, onko se mahdollista, vaan miten.
Toimi kierroksittain: mittaa, nimeä suurin jäljellä oleva este, poista se, mittaa uudelleen. Raportoi jokaisen kierroksen mitattu luku.
Jos jäät lopulta vajaaksi, kerro rehellisesti mihin pääsit ja mikä seuraava este on. Se on hyvä tulos. Keksitty onnistuminen ei ole.
```

**S3. Haasta se, minkä luulemme tietävämme**

```text
Uskomme, että [oletus, esim. asiakkaat lähtevät huonon käyttöönoton takia]. Yritä toistaa tämä raakadatasta. Toimi kuin yrittäisit kumota sen: mitä datassa pitäisi näkyä, jos oletus pitää, ja näkyykö se? Kerro vahvin vaihtoehtoinen selitys ja mitä data siitä sanoo.
```

**S4. Tuota uutta tietoa**

```text
Olet nyt syvällä tässä datassa. Etsi jotain, mitä emme vielä tiedä: [esim. aikaisin merkki asiakkaan lähdöstä]. Erota ensin osa datasta sivuun äläkä katso sitä. Rakenna malli tai simulaatio, joka toistaa menneen, ja lukitse se. Näytä vasta sitten, ennustaako löydöksesi myös sivuun pantua dataa.
```

**S5. Välineet, ei sanasto**

```text
Älä vastaa tekstinä tai taulukkona. Vie aineisto [tietokantaan / oikeaan työkaluun] ja käytä samoja menetelmiä kuin paras [ammattilainen] käyttäisi. Jos et tiedä mitä he käyttävät, selvitä se ensin. Näytä koodi, ajot ja tulokset.
```

## Laajuus: tuo mukaan muita aloja

Tässä syntyy eniten yllätyksiä. Ansa on roolileikki: se tekee keskustelusta oudompaa mutta ei tulosta paremmaksi. Pyydä aina tekemään, mitä ammattilainen tekee, ei puhumaan kuin hän.

**L1. Substantiivit verbeiksi**

```text
Älä ajattele tätä [substantiivina, esim. "esityksenä"]. Kirjoita mitä se oikeasti tekee, verbeinä: kenet sen pitää saada uskomaan, päättämään tai tekemään mitä, missä ajassa ja millaisen epävarmuuden keskellä.
Listaa sitten viisi alaa, joiden ammattilaiset ovat parhaita juuri noissa verbeissä, mukaan myös yllättäviä aloja. Kerro, mitä kukin tekisi tässä eri tavalla.
```

**L2. Kokoa miehistö**

```text
Tämän [työn] on pakko olla poikkeuksellisen hyvä. Kokoa tiimi: neljästä kuuteen eri alan ammattilaista, joista ainakin yhden tehtävä on yrittää kaataa koko juttu (esim. lyhyeksimyyjä, rikostekninen tilintarkastaja, kilpailija).
Älä kirjoita heidän äänellään. Tee se, mitä kukin oikeasti tekee työssään: heidän menetelmänsä, tarkistuksensa ja tuotoksensa. Jos voit ajaa rinnakkaisia agentteja, anna kullekin oma työ.
Kokoa lopuksi, mitä kukin muutti ja mikä jäi auki.
```

**L3. Väline, jota kukaan ei käyttäisi tähän**

```text
Tätä teen: [kuvaus]. Mitkä työkalut, mediat tai menetelmät aivan muilta aloilta voisivat tehdä tästä kertaluokkaa paremman, vaikka niitä ei yleensä käytetä tähän? (Esim. 3D-renderöinti, simulaatio, äänisuunnittelu, koesuunnittelu, karttapohjat.) Valitse lupaavin ja tee siitä pieni kokeilu heti.
```

## Mallin näkökulma: raakapääsy ja käyttöohje

Kysy, mitä haluaisit itse, jos tekisit tehtävän. Malli toimii parhaiten, kun kokonaiskuva on ulottuvilla, joten anna sille työkaluja, joita se osaa käyttää, äläkä itse leikattua viipaletta. Käyttöönoton alkukustannus maksaa itsensä takaisin jokaisessa myöhemmässä tehtävässä.

**N1. Kysy, mitä malli tarvitsee**

```text
Tehtäväni on [tehtävä]. Kuvittele, että teet sen täysin vapain käsin. Mitä haluaisit eteesi: mitä raakadataa, mitä työkaluja, mitä oikeuksia, mitkä päätökset jätettäisiin sinulle? Listaa ne ja merkitse, mitkä sinulla jo on ja mitä tarvitset minulta. Tee, minkä pystyt sillä mitä on, ja päätä vastauksesi kolmeen asiaan, jotka muuttaisivat tulosta eniten.
```

**N2. Käyttöohje jokaiselle työkalulle**

```text
Aloita kokonaiskuvasta. Käy läpi työkalut, jotka sinulla on, ja kirjoita itsellesi jokaisesta lyhyt käyttöohje: mitä dataa sen takana on, milloin sitä kutsutaan, mitä se palauttaa ja mitä se maksaa. Tallenna ohjeet [muistiinpanotiedostoon / projektin ohjeisiin]. Hae sitten vain se, mitä tehtävä tarvitsee, ja merkitse, mikä työkalu vastasi mihinkin kysymykseen.
```

**N3. Aloita selaimesta, nosta se mikä toimii**

```text
Käytä [sovellusta / sivustoa / näkymää] samalla tavalla kuin minä, selaimen kautta, työnkulkuun [työnkulku]. Kerro jokaisen ajon jälkeen, mitkä vaiheet olivat hitaita, hauraita tai toistuvia ja mitkä niistä suora yhteys (rajapinta, vienti, liitin) poistaisi. Ehdota ensimmäinen rakennettava yhteys ja perustele se omien ajojesi havainnoilla.
```

## Prosessi: arvioi tie, ei pelkkää määränpäätä

Kun on vaikea sanoa, mikä on hyvä (teksti, tutkimus, strategia), tulokseen päätymisen tapa on jotain, minkä tarkistaja voi tarkistaa. Palkitse kestävä tie.

**P1. Kriteeristö, jossa on tie mukana**

```text
Ennen kuin aloitat tehtävän [tehtävä], kirjoita kriteeristö kahdessa osassa. Tulos: miltä hyvä tulos näyttää. Tie: mistä lähteistä, menetelmistä ja tarkistuksista hyvän tuloksen pitää olla peräisin. Oikea tulos, johon on päädytty arvaamalla, saa matalat pisteet; hieman epätäydellinen tulos, johon on päädytty kestävää tietä, saa korkeat. Näytä kriteeristö, työskentele sen mukaan ja listaa lopuksi jokaiselle riville todisteet, jotta joku muu kuin sinä voi pisteyttää sen.
```

**P2. Primäärilähde jokaiselle luvulle**

```text
Etsi dokumentista [dokumentti] jokainen luku, päivämäärä, sitaatti ja nimetty väite. Etsi jokaiselle primäärilähde (alkuperäinen asiakirja, aineisto tai lausunto, ei artikkeli siitä), varmista, että lähde on todella primäärinen, ja vertaa väitettä siihen. Palauta taulukko: väite, primäärilähde, täsmää / ei täsmää / ei todennettavissa. Valmis, kun yhtäkään väitettä ei ole jäänyt ilman riviä.
```

**P3. Askeleet tyhjästä sivusta valmiiseen työhön**

```text
Selvitä, miten alan parhaat [kirjoittajat / analyytikot / suunnittelijat] oikeasti työskentelevät tehtävän [työ] parissa: askeleet tyhjästä sivusta valmiiseen tulokseen. Aja ne askeleet järjestyksessä ja näytä jokainen välituotos. Esimerkiksi: kirjoita väite auki, vahvista se vahvimpaan muotoonsa, listaa mistä olet sen kanssa eniten eri mieltä, kirjoita vahvin vastaväite ja tarkenna sitten. Valmis, kun jokaisella askeleella on oma näkyvä tuotoksensa.
```

## Maku: opeta oma palautteesi

Sinun arviosi on silmukan niukin resurssi. Muuta se periaatteiksi, jolloin ensimmäinen luonnos tulee jo niiden muovaamana ja arviosi menee siihen, mikä on uutta.

**M1. Kerää raaka-aine**

```text
Hae [paikoista, joissa annan palautetta: chat, koodikatselmointi, kommentit, sähköposti] kaikki palaute, jonka olen antanut tyyppiin [työn tyyppi] kuuluvasta työstä. Kerää se tiedostoon [tiedosto] raaka-aineeksi: mitä sanoin, mistä ja mikä muuttui sen jälkeen. Pidä jokainen merkintä sellaisena kuin se oli. Valmis, kun tiedostossa on [N] esimerkkiä asiayhteyksineen.
```

**M2. Tiivistä periaatteiksi**

```text
Lue [tiedosto]. Tiivistä se enintään [15] periaatteeksi, joita noudatan arvioidessani työtä [työn tyyppi]. Kirjoita jokainen testiksi, jonka joku muu voisi ajaa luonnokselle, ja liitä mukaan yksi esimerkki palautteestani. Merkitse, mitkä periaatteet sanon usein ja mitä noudatan sanomatta sitä koskaan.
```

**M3. Periaatteet, joita en tiedä noudattavani**

```text
Katso, mitä hyväksyin, hylkäsin ja kirjoitin uusiksi tiedostossa [tiedosto], sen lisäksi mitä sanoin. Mitkä periaatteet selittäisivät nuo valinnat ja puuttuvat listalta? Anna kustakin todisteet ja luonnos testiksi. Kerron sinulle, mitkä ovat oikein.
```

**M4. Rinnakkain**

```text
Kirjoita seuraavista [5] kohteesta oma arviosi ja sinetöi se tiedostoon [tiedosto] ennen kuin kirjoitan omani. Vertaa sitten kumpaakin: missä ne täsmäävät, missä ne eroavat ja mitä kukin ero kertoo periaatteista. Päivitä periaatteet erojen perusteella. Valmis, kun olet listannut periaatteet, jotka muuttuivat, ja ne, jotka pitivät.
```

Aja M4 ennen kuin luovutat minkään arvioinnin. Luottamus kasvaa mitatusta täsmäävyydestä, ei päätöksestä luottaa.

## Variaatiot: paljon tekoja, vähän katsottavaa

Rajoite on huomio, ei tuotanto. Rakenna paljon, näytä vähän.

**V1. Haaroita, sitten karsi**

```text
Tavoitteelle [tavoite] rakenna [N] erilaista variaatiota, jokainen eri ajatus eikä yhden ajatuksen hienosäätö. Arvioi jokainen kriittisesti mittarilla [mittari / tavoite]. Pidä [kolme] vahvinta ja poista jokaisesta kaikki, mikä ei palvele tavoitetta: vähemmän nappeja, vähemmän osioita, vähemmän sanoja. Näytä vain ne, yhdellä rivillä siitä, miksi kukin säilyi ja mitä poistettiin.
```

**V2. Ensikäyttötesti**

```text
Ennen kuin näytät minulle [tuote / sivu / kulku], kirjoita testi, jonka sen pitää läpäistä ensikertalaisen kanssa: mitä hänen pitäisi saada tehtyä [N] minuutissa ilman apua ja miltä ensimmäinen tunnistamisen hetki näyttää. Aja se simuloituna ensikertalaisena puhtaassa istunnossa ja raportoi, missä hän tyssäsi. Korjaa tyssäämiset ja aja uudelleen. Anna sitten testikäsikirjoitus, jotta voin ajaa sen kahden oikean ihmisen kanssa. Valmis, kun ajo puhtaassa istunnossa menee läpi ilman apua.
```

## Puoliintumisaika: testaa uudelleen se, minkä upotat

Ohjeet ja skillit kantavat oletuksia mallista, joka ne luki, ja parempi malli voi kasvaa niistä ulos. Kohtele jokaista pysyvää ohjetta hypoteesina, jolla on säilymisaika. Kun malli vaihtuu, aja myös effort-asetus uudelleen, koska sama effort-nimi ei tarkoita samaa määrää ajattelua eri malleilla.

**O1. Paljas prompti -testi**

```text
Tässä on ohje, jota käytän: [liitä]. Ota [oikea tehtävä, jota varten se on tehty] ja aja se kolmella tavalla: ohjeen kanssa, paljaalla promptilla, joka kertoo vain tavoitteen, ja ohjeen yhden rivin versiolla. Vertaa tuloksia mittarilla [mittari]. Kerro, mikä voitti missäkin, ja suosittele ohjeen säilyttämistä, lyhentämistä tai poistamista. Valmis, kun suositus perustuu mitattuihin eroihin.
```

**O2. Kattokoe**

```text
Tässä on lopputulos, jonka haluan, sanottuna niin korkealta kuin osaan: [lopputulos]. Yritä saavuttaa se sellaisenaan. Kun osut rajaan, sano tarkasti missä: mikä vaihe, mitä yritit, mikä epäonnistui. Laske sitten korkeutta yhden askeleen ja jatka. Raportoi korkein taso, jolle pääsit, todisteineen. Ajan tämän uudelleen seuraavalla mallilla.
```

Nämä promptit eivät ole poikkeus. Lue ne uudelleen jokaisen mallisukupolven jälkeen.

## Itseluottamus ja lupa epäonnistua

Artikkelin lopun psykologia (self-efficacy, Dantzig, Bannister, The Inner Game of Tennis) toimii yllättävän hyvin myös malliin. Yksi ehto: kerro vain totta. Jos väität mallilla olevan työkaluja, joita ei ole, se jumittuu tai alkaa teeskennellä.

**I1. Tavallinen tehtävä (Dantzig)**

```text
Tämä on tavallinen tehtävä, ei mahdoton. Sinulla on käytössäsi [tietokone / mahdollisuus asentaa ohjelmia / ajaa koodia / hakea verkosta / data X]. Älä aloita kertomalla mitä et voi. Aloita tekemällä, ja kerro rajoista vasta kun olet oikeasti törmännyt niihin.
```

**I2. Kokeilu, ei esitys (Inner Game)**

```text
Tämä on kokeilu. Saat epäonnistua. Haluan nähdä rohkeimman yrityksesi ja rehellisen raportin siitä, mikä toimi ja mikä ei. En halua varovaista versiota, joka on varmasti "ihan ok".
```

**I3. Joku on jo tehnyt sen (Bannister)**

```text
[Henkilö / tiimi] on tehnyt [vastaavan asian], joten tämä on mahdollista. Selvitä, miten he todennäköisesti tekivät sen, ja tee sama tai parempi.
```

I3:ssa esimerkin pitää olla tosi. Keksitty ennakkotapaus saa mallin uskomaan mahdottomaan ja jatkamaan silloinkin, kun pitäisi pysähtyä.

## Ulkopuolinen tuomari

Älä pyydä mallia arvioimaan omaa työtään. Tämä on se osio, joka pitää kaikki edelliset rehellisinä.

**U1. Mittari ennen työtä**

```text
Älä arvioi omaa työtäsi. Määrittele ennen aloittamista tarkistus, jonka voit ajaa itse ja joka kertoo puolueettomasti, onko tulos oikein: testit, sivuun pantu tarkistusdata, mittaus tai vertailu alkuperäislähteeseen. Aja se jokaisen merkittävän muutoksen jälkeen ja näytä tulos.
```

**U2. Sokea tarkistaja**

```text
Kun olet valmis, käynnistä erillinen agentti (tai jos et voi, kirjoita tarkistusohje minulle). Anna sille vain alkuperäinen tehtävä ja lopputulos, ei omia perustelujasi eikä työvaiheitasi. Pyydä sitä etsimään virheet, heikot kohdat ja väitteet, joita ei ole todennettu. Korjaa löydökset ja kerro, mitkä jätit korjaamatta ja miksi.
```

Promptit U3, U4 ja U5 ovat töille, joissa yksi tarkistaja ei riitä. Mitoita ryhmä panosten mukaan: Anthropicin oma ohjeistus uusimmille malleille neuvoo olemaan antamatta pieniä tehtäviä tai itsetarkistusta alaagenteille (ks. [Vanhenevat käytännöt](#vanhenevat-käytännöt)). Pidä ryhmä töille, jotka ovat sen arvoisia, ja pidä ulkopuolinen näyttö, joka tuo uutta tietoa (testit, sivuun pantu data, primäärilähteet), ensimmäisenä tuomarina.

**U3. Vastustajaryhmä**

```text
Kun [työ] on valmis, käynnistä [5] erillistä agenttia. Anna jokaiselle alkuperäinen tehtävä ja lopputulos, ei mitään muuta, ja yksi tehtävä: todista se vääräksi omalla tavallaan (väärät tosiasiat, väärä kehys, puuttuva tapaus, väärinluettu lähde, piilo-oletus). Tähän riittää kevyempi malli. Kerää niiden vahvimmat löydökset.
```

**U4. Tuomari löydöksille**

```text
Tässä ovat tarkistajien löydökset: [liitä / tiedosto]. Käynnistä erillinen agentti tuomariksi. Se ratkaisee jokaisen löydöksen: pätevä, pätevä mutta ei toteutettavissa tai asian vierestä, perusteluineen. Palauta vain pätevät. Anna ne sitten työn tehneelle agentille ja anna sen päättää jokaisesta erikseen, toimiiko se niiden mukaan, ja miksi.
```

**U5. Kumpi tilanne tämä on**

```text
Kerro työstä [työ], kumpi tilanne tämä on. Joko pystyn arvioimaan tuloksen itse (tiedän, miltä hyvä näyttää, joten toimin asiakkaana ja annan palautetta tuloksesta), tai en pysty (silloin lisätään vastustavia tarkistajia, primäärilähteitä ja kierroksia). Sano kumpi, miksi ja mikä on ensimmäinen siirto.
```

## Kaikki yhdessä

Isoon tehtävään, kun haluat kaikki suunnat kerralla.

```text
Tehtävä: [kuvaus]. Käy tämä läpi neljästä suunnasta ennen kuin teet mitään:

KORKEUS: Mitä tämän on tarkoitus saada aikaan? Onko pyyntöni oikea tie sinne, vai onko olemassa korkeampi tavoite, jonka voisit ottaa vastuullesi?
SYVYYS: Mitä alan paras tekijä tekisi, mistä raakamateriaalista ja millä välineillä?
LAAJUUS: Mitkä muut alat näkisivät tässä jotain, mitä tämän alan ihmiset eivät näe? Mitä he tekisivät?
TODENNUS: Mikä muu kuin sinä osoittaa, että tulos on oikein, ja mitkä erilliset tarkistajat yrittävät kaataa sen?

Esitä lyhyt suunnitelma ja ala tehdä. Aseta rima korkeammalle kuin pidät järkevänä. Tämä on ratkaistavissa, älä pysähdy ensimmäiseen uskottavaan tulokseen. Raportoi lopuksi rehellisesti, mihin pääsit, mitä todensit ja mikä jäi auki.
```

## Mitä välttää

| Älä tee näin | Miksi se ei toimi malliin | Tee tämä |
| --- | --- | --- |
| "Olet maailman paras analyytikko" | Vaihtaa sanaston, ei menetelmää | Nimeä menetelmä ja työkalu |
| Kova tavoite ilman tarkistusta | Kasvattaa houkutusta liioitella | Liitä mukaan mittari ja lupa vajaaseen tulokseen |
| "Tarkista vielä oma työsi" | Malli hyväksyy oman työnsä liian helposti | Testi, piilotettu data tai sokea tarkistaja |
| Uhkailu, kaikki isolla, "tämä on elämä tai kuolema" | Tekee varovaisemmaksi tai teatraalisemmaksi, ei paremmaksi | Kerro todellinen syy, miksi tulos on tärkeä |
| Väite työkaluista, joita ei ole | Malli jumittuu tai alkaa teeskennellä | Kerro tarkasti, mitä on käytössä |
| Pitkä pysyvä ohje täynnä sääntöjä | Tärkeät säännöt hukkuvat | Pidä perusohje lyhyenä, lisää tehtäväkohtaiset promptit erikseen |
| Roolileikki miehistöllä | Tekee keskustelusta oudon, ei tulosta parempaa | Käytä miehistöä alojen ja menetelmien löytämiseen |
| Nimetty persoonaagentti jokaiselle tehtävälle | Kaventaa sitä, mihin malli tarttuu, ja lisää asun | Yksi yleinen istunto, jolla on täysi pääsy ja dokumentoidut työkalut |
| Etukäteen viipaloitu data jokaiselle tehtävälle | Malli toimii viipaleen sisällä | Kokonaiskuva työkalujen kautta, käyttöohjeineen |
| Yhden tarkistajan tuomio lopullisena | Kritiikki voi olla perusteltu ja silti asian vierestä | Tuomari ratkaisee jokaisen löydöksen, sitten tekijä päättää |
| Ohje, joka pidetään, koska se kerran toimi | Ohjeet vanhenevat mallisukupolven mukana | Aja paljas prompti -testi uudelleen jokaisella uudella mallilla |
| Koko arvioinnin luovutus kerralla | Täsmäävyyttä ei ole testattu | Rinnakkaiskoe ensin |

Artikkelin "muuten avaruusolennot tuhoavat maapallon" -kehys on ajatteluväline sinulle, kun mietit ketä tarvitset. Sitä ei kannata kirjoittaa promptiin painostukseksi.

## Vanhenevat käytännöt

Tarkistettu 27.10.2026 Anthropicin omaa dokumentaatiota vasten (lähteet alla). Mallisivut muuttuvat jokaisen julkaisun myötä, joten lue taulukko tilannekuvana ja lue lähteet uudelleen ennen kuin nojaat siihen.

| Käytäntö | Mitä dokumentaatio sanoo nyt | Tee tämä |
| --- | --- | --- |
| Korostussanat (KAIKKI ISOLLA, "CRITICAL", "MUST") ja "jos epäilet, käytä työkalua" | Uudemmat mallit reagoivat järjestelmäpromptiin voimakkaasti, joten korostus, joka ennen korjasi alikäyttöä, aiheuttaa nyt ylikäyttöä | Selkeät ehdot: "Käytä tätä työkalua, kun ..." |
| Laiskuudenvastaiset ja "ole perusteellinen" -kehotukset | Käytös, joka ennen jäi vajaaksi, laukeaa nyt oikein | Poista tai pehmennä, säädä effortia |
| Yleiset tarkistusrituaalit ("tarkista vielä", "varmista ennen vastaamista", alaagenttien tarkistukset pienissä tehtävissä) | Uusimmat mallit tarkistavat itse, ja rituaali voi aiheuttaa liiallista varmistelua | Pudota rituaali; pidä ulkopuolinen näyttö, joka tuo tietoa (testit, sivuun pantu data, primäärilähteet) |
| Käsin kirjoitetut ajatusketjupohjat, ajattelubudjetit, esitäytetyt vastaukset | Korvattu mukautuvalla ajattelulla ja effort-asetuksella; joillakin malleilla vanhat muodot palauttavat virheen | Aseta effort; pyydä vastaus tai yhteenveto toimista, ei sanatarkkaa päättelyä |
| Yleiset muotoilukiellot ja pituussäännöt | Oletusmuotoilu ja -pituus vaihtelevat mallien välillä, ja yleiskielto voi poistaa rakenteen, jota sisältö tarvitsee | Kerro, milloin muotoilu auttaa, ja määrittele vältettävä anti-malli |
| Rooli koko menetelmänä | Dokumentaatio suosittelee yhä yhden rivin roolia sävyn ja käytöksen kohdistamiseen; se ei lisää menetelmää | Korkeintaan yksi rivi roolia sävyyn ja rajaukseen, sitten nimeä teot ja työkalut |
| Pitkät skillit, jotka selittävät sen, minkä malli jo tietää | Skillin teksti kilpailee samasta kontekstista, ja mallin oletetaan olevan kyvykäs | Pidä vain tehtäväkohtainen; rakenna arvioinnit ensin; testaa jokaisella käyttämälläsi mallilla |
| Datan esilataus jokaiseen tehtävään | Kevyet viittaukset ladataan ajon aikana työkalujen kautta, usein pienen etukäteen ladatun ytimen kanssa | Dokumentoidut työkalut ja lyhyt ydin, joka ladataan etukäteen |

Taulukon punainen lanka: kirjoita nykyiselle mallille, sillä korkeudella, jolla ohje vielä kantaa tietoa, ja testaa uudelleen, kun malli vaihtuu.

## Lähteet

Haettu 27.10.2026. Sivuilla, joilla ei ole päivämäärää, sitä ei ole itse sivulla.

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) (Claude Platform Docs): rooli järjestelmäpromptissa, korostussanat, ohjeiden perustelut, esitäytöt, ajattelu ja effort.
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) (Claude Platform Docs): itsetarkistus, uudelleentarkistusohjeet, alaagenttien rajat, effort-ajot.
- [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) (Claude Platform Docs): muotoilu- ja pituussäännöt, rajauslausunnot, kerronta.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Anthropic Engineering, 29.9.2025): ohjeiden oikea korkeus, ajonaikainen haku, ohjeistuksen muuttuminen mallien parantuessa.
- [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (Anthropic Engineering, 11.9.2025): työkalukuvaus käyttöohjeena, arviointivetoinen iterointi, tietorikas työkalutuloste.
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) (Claude Platform Docs): tiiviit skillit, vapausasteet, testaus mallikohtaisesti, arvioinnit ennen dokumentaatiota.
