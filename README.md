# Web Lucky Canteen (luckycanteen.sk)

Statický web – náhrada za WordPress/Mioweb (od 28. 10. 2026). Texty a rozloženie sú 1:1 ako pôvodný web, farby čierna + červená z loga. **Texty nemeniť bez súhlasu Samuela.**

## Denné menu
Stránka `/denne-menu/` a sekcia na úvode ťahajú menu **automaticky z Menučka.sk** (widget `menucka.sk/widget/main/luckycanteen/weekmenu`). Stačí, že je menu zadané na Menučke – na webe netreba nič robiť.

## Týždenné menu (obrázok) – každý týždeň
Na úvodnej stránke je pod widgetom obrázok týždenného menu: `img/tyzdenne-menu.jpg`.
Postup (robí Claude kolegyne):
1. Nový obrázok menu (PNG/JPG) ulož ako `img/tyzdenne-menu.jpg` – prepíš starý (JPG, šírka ~1000 px; na Macu: `sips -s format jpeg -Z 1000 nove.png --out img/tyzdenne-menu.jpg`).
2. Skontroluj lokálne: `python3 -m http.server` v tomto priečinku → http://127.0.0.1:8000
3. `git add img/tyzdenne-menu.jpg && git commit -m "Týždenné menu DD.MM.–DD.MM." && git push` – po pushi sa web nasadí sám (hosting doplniť po spustení).

## Úpravy stránok
Stránky sa generujú z `build.py` (`python3 build.py`) – needituj priamo `index.html`, ale `build.py` a potom spusti build.
