# Gorev 2: Format Check Workflow

## Amac
PR acildiginda kodun **black** ve **isort** ile formatlanip formatlanmadigini kontrol eden bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/format.yml`
- Tetikleme: `main` branch'e PR acildiginda
- Python 3.11 kullanin
- Hem `black` hem `isort` kontrolu yapin
- Onemli: dosyalari degistirmeyin, sadece kontrol edin

## Ipuclari

- black ve isort'un `--check` modu dosyalari degistirmeden kontrol eder
- isort icin `--check-only` flagi kullanilir
- `--diff` flagi ile farklar gorulebilir

## Test Etme
- Formatsiz bir dosya ekleyip PR acin (ornegin cok uzun satirlar, karisik importlar)
- Workflow fail etmeli
- Lokal'de `black app/ tests/` ve `isort app/ tests/` calistirip push edin
