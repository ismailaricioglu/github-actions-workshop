# Gorev 3: Test Workflow

## Amac
PR acildiginda ve main'e push yapildiginda **pytest** ile testleri calistiran bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/test.yml`
- Tetikleme: iki durumda calissin:
  1. `main` branch'e PR acildiginda
  2. `main` branch'e push yapildiginda
- Tum bagimliliklari `requirements.txt` uzerinden yukleyin
- `pytest tests/ -v` ile testleri calistirin

## Ipuclari

- `on:` altinda birden fazla event tanimlanabilir
- `-v` flagi detayli cikti verir
- Bagimliliklari yuklemeden pytest calistirsaniz hata alisiniz

## Test Etme
- Mevcut testlerin gectigini dogrulayin
- `test_app.py` icinde bir assert degerini degistirip PR acin
- Workflow fail etmeli, duzeltip tekrar push edin
