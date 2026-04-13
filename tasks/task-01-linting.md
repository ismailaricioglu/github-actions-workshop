# Gorev 1: Linting Workflow

## Amac
PR acildiginda Python kodunu **flake8** ile lint eden bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/lint.yml`
- Tetikleme: `main` branch'e PR acildiginda
- Python 3.11 kullanin
- `flake8 app/ tests/` komutunu calistirin

## Ipuclari

- `actions/checkout@v4` ile kodu cekin
- `actions/setup-python@v5` ile Python kurun
- `pip install flake8` ile araci yukleyin

## Test Etme
- Bilerek hatali bir Python dosyasi ekleyin (ornegin gereksiz bosluklar, kullanilmayan import)
- PR acin, workflow'un hata verdigini goruntuleyin
- Duzeltip push edin, yesil tik alin
