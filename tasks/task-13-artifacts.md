# Gorev 13: Artifact Upload/Download

## Amac
Test sonuclarini ve coverage raporunu **artifact** olarak saklayan bir workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/artifacts.yml`
- Tetikleme: `main` branch'e PR acildiginda
- Python 3.11 kullanin
- `pytest` ile testleri calistirin ve JUnit XML raporu olusturun
- `pytest-cov` ile coverage raporu olusturun (HTML formatinda)
- Her iki raporu da artifact olarak upload edin
- Artifact retention suresi 7 gun olsun

## Ipuclari

- JUnit raporu: `pytest --junitxml=report.xml`
- Coverage raporu: `pytest --cov=app --cov-report=html`
- `actions/upload-artifact@v4` ile dosya/klasor yukleyin
- `pytest-cov` paketini `pip install` ile ekleyin
- Her artifact'a anlamli isim verin (ornegin `test-report`, `coverage-report`)

## Test Etme
- PR acin ve workflow'un basarili calistigini goruntuleyin
- Actions sekmesinde workflow run'a tiklayin, "Artifacts" bolumunde raporlari gorun
- Artifact'lari indirip iclerini kontrol edin
- Coverage HTML raporunu tarayicida acin
