# Gorev 4: Matrix Strategy - Coklu Python Versiyonu

## Amac
Testleri **birden fazla Python versiyonunda** ayni anda calistiran bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/matrix-test.yml`
- Tetikleme: `main` branch'e PR acildiginda
- Python 3.9, 3.10 ve 3.11 versiyonlarinda testleri calistirin
- Bir versiyon fail etse bile diger versiyonlar calismayi bitirsin

## Arastirma Konulari

- GitHub Actions'da `strategy.matrix` nasil kullanilir?
- `fail-fast` ne ise yarar ve varsayilan degeri nedir?
- Matrix degiskenine step icinden nasil erisirilir? (`${{ }}`)

## Test Etme
- PR acin ve Actions sekmesinde 3 paralel job goruntuleyin
- Her job'un farkli Python versiyonu kullandigini loglardan dogrulayin
