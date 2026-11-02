# Návod pre Clauda: týždenné menu Lucky Canteen na web

Pre: Sára Práznovská (a jej Claude). Robí sa raz týždenne, keď je hotové PDF s menu (napr. `2.11.2026-6.11.2026.pdf`).

## Jednorazovo (prvýkrát)
1. Sára má GitHub účet a Samuel ju pridal ako spolupracovníka do repa `smahelsamo-sketch/luckycanteen-web` (Settings → Collaborators). Pozvánku prijme v maile.
2. Na Macu: nainštalovaný Claude Code (claude.ai/code) a prihlásený `gh` (`gh auth login`).
3. `git clone https://github.com/smahelsamo-sketch/luckycanteen-web.git ~/Desktop/luckycanteen-web`

## Každý týždeň (Claude to urobí sám)
Sára povie Claudovi: „Daj na web nové menu“ a pošle mu cestu k PDF. Claude:
1. `cd ~/Desktop/luckycanteen-web && git pull`
2. Prevedie PDF na obrázok (Mac, bez inštalácie):
   ```
   qlmanage -t -s 2000 -o /tmp "CESTA/K/menu.pdf"
   sips -s format jpeg -s formatOptions 85 "/tmp/menu.pdf.png" --out img/tyzdenne-menu.jpg
   ```
   (výsledok má mať ~1414 × 2000 px; prepíše starý obrázok – názov súboru sa NEMENÍ)
3. Otvorí `img/tyzdenne-menu.jpg` a skontroluje, že je to nové menu so správnymi dátumami.
4. `git add img/tyzdenne-menu.jpg && git commit -m "Týždenné menu D.M.–D.M." && git push`
5. Po ~2 minútach overí https://www.luckycanteen.sk/ (obrázok pod denným menu; ak je starý, obnoviť stránku s Shift).

## Čo nerobiť
- Nemeniť iné súbory ani texty webu (len `img/tyzdenne-menu.jpg`). Texty mení len Samuel.
- Denné menu (widget Menučka.sk) sa na webe aktualizuje samo – stačí ho zadať na Menučke.
- Ak niečo nejde (push zamietnutý, chyba), nič neobchádzať – napísať Samuelovi.
