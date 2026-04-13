# Gorev 14: Reusable Workflow

## Amac
Tekrar kullanilabilir (reusable) bir test workflow'u olusturun ve onu ikinci bir workflow'dan **cagirin**. Her iki dosyayi da siz olusturacaksiniz.

## Gereksinimler

**Dosya 1:** `.github/workflows/reusable-test.yml` (cagrilacak workflow)
- Tetikleme: `workflow_call` (sadece baska workflow'lardan cagrilabilir)
- Input olarak `python-version` alsin (zorunlu, string tipinde)
- Adimlar:
  1. Kodu checkout etsin
  2. Gelen `python-version` input'u ile Python kursun
  3. Bagimliliklari yuklesin
  4. `pytest tests/ -v` calistirsin

**Dosya 2:** `.github/workflows/call-tests.yml` (cagiran workflow)
- Tetikleme: `main` branch'e PR acildiginda
- Iki job tanimlayin:
  1. `test-311`: Dosya 1'i `python-version: "3.11"` ile cagirsin
  2. `test-310`: Dosya 1'i `python-version: "3.10"` ile cagirsin

> **Not:** Her iki dosya da sizin tarafinizdan olusturulacak. Baska birinin workflow'una bagli degilsiniz.

## Ipuclari

- Reusable workflow tetikleyicisi:
  ```yaml
  on:
    workflow_call:
      inputs:
        python-version:
          required: true
          type: string
  ```
- Input'a erisim: `${{ inputs.python-version }}`
- Cagirma (call-tests.yml icinde):
  ```yaml
  jobs:
    test-311:
      uses: ./.github/workflows/reusable-test.yml
      with:
        python-version: "3.11"
  ```
- `uses:` ile cagirilan workflow ayni repo'da olmalidir (`./.github/workflows/...`)

## Test Etme
- PR acin, `call-tests.yml`'in tetiklendigini goruntuleyin
- Actions sekmesinde iki ayri job gormelisiniz: `test-311` ve `test-310`
- Her ikisinin de `reusable-test.yml`'i farkli Python versiyonuyla cagirdigini dogrulayin
- Reusable workflow'da bilerek hata yapin (ornegin yanlis komut), her iki job'un da fail ettigini gorun
