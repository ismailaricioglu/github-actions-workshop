# Gorev 17: Concurrency Control

## Amac
Ayni PR icin ayni anda birden fazla workflow calismasini engelleyen **concurrency** kontrolu ekleyin.

## Gereksinimler

- Dosya: `.github/workflows/concurrency-test.yml`
- Tetikleme: `main` branch'e PR acildiginda
- Concurrency group tanimlayin: ayni PR'dan gelen yeni push, onceki calisan workflow'u iptal etsin
- `cancel-in-progress: true` kullanin
- Workflow adimlari:
  1. Kodu checkout edin
  2. Python 3.11 kurun
  3. Bagimliliklari yukleyin (`pip install -r requirements.txt`)
  4. `echo "Running checks..."` yazin
  5. 60 saniye bekleyin (`sleep 60`) — bu sayede ikinci push'u test edebilirsiniz
  6. `echo "Checks complete!"` yazin

## Ipuclari

- Concurrency tanimlama (workflow seviyesinde):
  ```yaml
  concurrency:
    group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
    cancel-in-progress: true
  ```
- Group key olarak PR numarasi kullanildiginda, ayni PR'dan gelen yeni push onceki run'i iptal eder
- `cancel-in-progress: true` olmadan yeni run kuyrukta bekler (iptal etmez)
- `sleep 60` adimi workflow'u yavas tutarak cancel davranisini test etmeyi kolaylastirir

## Test Etme
- PR acin ve workflow baslasin
- Workflow `sleep 60` adimindayken hizlica yeni bir commit push edin
- Onceki workflow run'in "cancelled" oldugunu goruntuleyin
- Sadece son run'in tamamlandigini dogrulayin
