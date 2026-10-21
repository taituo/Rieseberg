# Rieseberg: skillit kunnianhimoiseen työhön

Metaskillejä, jotka muuttavat sitä, *miten* agentti tarttuu tehtävään: se tähtää korkeammalle ja on rehellinen siitä, mihin pääsi. Toimivat millä tahansa mallilla ja alalla.

[In English](./README.md)

Pohjana on Felix Riesebergin kirjoitus [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). Hän jakaa kunnianhimon neljään suuntaan: **nopeus**, **korkeus** (altitude), **syvyys** (depth) ja **laajuus** (range). Nopeus tulee mallin mukana ilmaiseksi. Nämä skillit tekevät kolmesta muusta askelia, jotka agentti ajaa, ja lisäävät palan, joka pitää ne rehellisinä: **ulkopuolisen tuomarin** (outside judge).

## Asennus

Claude Code:

```bash
claude plugin marketplace add taituo/rieseberg
claude plugin install rieseberg@taituo
```

Muut agentit: `npx skills@latest add taituo/rieseberg`. Muut tavat [englanninkielisessä README:ssä](./README.md#installation).

Kirjoita sitten `/ambition` seuraavan oikean tehtävän eteen.

## Skillit

Itse kutsuttavat:

- **[ambition](./skills/ambition/ambition/SKILL.md)**: suunnittelee tehtävän korkeuden, syvyyden ja laajuuden kautta ja tarkistaa tuloksen ulkopuolisella tuomarilla. Aloita tästä.
- **[ambitious-prompt](./skills/ambition/ambitious-prompt/SKILL.md)**: kirjoittaa promptin uudelleen kunnianhimoisemmaksi.

Agentti käyttää näitä itsekin, kun tehtävä sopii:

- **[altitude](./skills/ambition/altitude/SKILL.md)**: nostaa tehtävän siihen lopputulokseen, jota se palvelee.
- **[depth](./skills/ambition/depth/SKILL.md)**: tekee työn niin kuin alan paras tekijä: raakadata, oikeat välineet, oletusten haastaminen, mitatut kierrokset.
- **[range](./skills/ambition/range/SKILL.md)**: tuo menetelmiä muilta aloilta: verbit, miehistö ja vastustaja, yksi vieraan alan väline.
- **[outside-judge](./skills/ambition/outside-judge/SKILL.md)**: todentaa työn jollain muulla kuin agentin omalla arviolla.

## Ilman skillejä

- **[CORE.md](./CORE.md)**: kuusi lyhyttä pysyvää ohjetta (englanniksi) upotettavaksi `CLAUDE.md`:hen, projektin ohjeisiin tai järjestelmäkehotteeseen. Suomenkielinen versio on [prompts/fi.md](./prompts/fi.md):ssä.
- **[prompts/fi.md](./prompts/fi.md)**: samat ideat valmiina kopioitavina prompteina, sekä analyysi siitä, miten ne vaikuttavat malliin.
