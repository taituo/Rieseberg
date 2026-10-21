# Kunnianhimon promptit

Valmiit promptit, jotka saavat tekoälyn tekemään isompaa, syvempää ja rehellisempää työtä. Perusohje upotetaan pysyväksi (projektin ohjeet, mukautetut ohjeet tai järjestelmäkehote). Muut liitetään tehtävän alkuun tarpeen mukaan. Hakasulkeet [näin] täytetään itse.

Pohjana on Felix Riesebergin kirjoitus [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). Promptit ovat sen ideoista muokattuja omia versioita, eivät käännöksiä.

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

## Kaikki yhdessä

Isoon tehtävään, kun haluat kaikki suunnat kerralla.

```text
Tehtävä: [kuvaus]. Käy tämä läpi neljästä suunnasta ennen kuin teet mitään:

KORKEUS: Mitä tämän on tarkoitus saada aikaan? Onko pyyntöni oikea tie sinne, vai onko olemassa korkeampi tavoite, jonka voisit ottaa vastuullesi?
SYVYYS: Mitä alan paras tekijä tekisi, mistä raakamateriaalista ja millä välineillä?
LAAJUUS: Mitkä muut alat näkisivät tässä jotain, mitä tämän alan ihmiset eivät näe? Mitä he tekisivät?
TODENNUS: Mikä muu kuin sinä osoittaa, että tulos on oikein?

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

Artikkelin "muuten avaruusolennot tuhoavat maapallon" -kehys on ajatteluväline sinulle, kun mietit ketä tarvitset. Sitä ei kannata kirjoittaa promptiin painostukseksi.
