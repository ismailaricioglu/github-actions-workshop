# Gorev 16: Custom Composite Action

## Amac
Python kurulumu ve bagimliliklarin yuklenmesini tek bir adimda yapan **custom composite action** olusturun.

## Gereksinimler

- Dosya: `.github/actions/setup-python-app/action.yml` (composite action)
  - Input olarak `python-version` alsin (default: "3.11")
  - Python'u kurup `pip install -r requirements.txt` calistirsin
  - Kurulum tamamlandiginda Python versiyonunu ve yuklenen paket sayisini loglara yazsin

- Dosya: `.github/workflows/use-composite.yml` (action'i kullanan workflow)
  - `main` branch'e PR acildiginda tetiklensin
  - Olusturdugunuz composite action'i kullansin
  - Ardindan testleri calistirsin

## Ipuclari

- Composite action dosya yolu: `.github/actions/<isim>/action.yml`
- Action tanimlama: `runs: using: 'composite'`
- Her adim icin `shell: bash` belirtilmeli
- Adimlar `runs.steps` altinda tanimlanir
- Local action kullanma: `uses: ./.github/actions/setup-python-app`
- `actions/setup-python@v5` composite action icinden cagrilabilir

## Test Etme
- PR acin ve workflow'un composite action'i basariyla cagirdigini goruntuleyin
- Python versiyonunu degistirip tekrar deneyin
- Action loglarinda Python versiyonu ve paket sayisini goruntuleyin
