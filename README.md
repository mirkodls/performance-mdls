# PERFORMANCE by mdls - sito

Pagina della beta di PERFORMANCE by mdls (ottimizzatore Windows 10/11 per giochi), pubblicata con GitHub Pages.
Il codice del programma sta in un altro repository, privato.

- `index.html`: la pagina pubblicata. Non modificarla a mano: si rigenera.
- `sorgente/pagina.html`: testi (italiano + inglese) e stile da modificare. Poi `python3 sorgente/costruisci.py`.
- `licenze/OFL-Archivo.txt`: licenza del font Archivo, incorporato nella pagina.
- Installatore: nelle Release di `mirkodls/performance-mdls-download` (lo stesso repository che usa il programma per gli aggiornamenti).
- La pagina non usa cookie, statistiche o risorse esterne.

## Prima di accendere il sito
Tutto quello che ha la classe `segnaposto` (bordo arancio) va completato: link di download, versione del file, IVA,
pagine legali (`privacy/`, `cookie/`, `termini/`, `vendita/`, `rimborsi/`, `responsabilita/` e `en/...`), email dei contatti.

## Accendere il sito
Settings > Pages > Source "Deploy from a branch" > Branch `main`, cartella `/ (root)` > Save.
