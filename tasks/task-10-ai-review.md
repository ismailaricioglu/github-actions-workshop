# Gorev 10: PR Diff Ozeti ve Otomatik Review (Zor)

## Amac
PR acildiginda degisen dosyalari analiz edip PR'a otomatik bir **ozet yorum** yazan workflow olusturun.

## Gereksinimler

- Dosya: `.github/workflows/ai-review.yml`
- Tetikleme: PR acildiginda ve yeni commit push edildiginde
- Workflow su adimlari icermeli:
  1. Kodu cek (tum git gecmisiyle — diff alabilmek icin)
  2. PR branch'i ile base branch arasindaki farki al
  3. Degisen dosya listesini cikar
  4. Su bilgileri iceren bir PR yorumu yaz:
     - Degisen dosya listesi
     - Toplam degisen dosya sayisi
     - Python dosyasi sayisi
     - Kontrol listesi

## Arastirma Konulari

- `actions/checkout` ile tum git gecmisi nasil cekilir? (`fetch-depth`)
- `git diff origin/main...HEAD --name-only` ne yapar?
- Bir adimin ciktisini sonraki adima nasil aktarirsiniz? (`$GITHUB_OUTPUT` ve `echo "key=value" >> $GITHUB_OUTPUT`)
- Cok satirli ciktiyi `$GITHUB_OUTPUT`'a nasil yazarsiniz? (EOF delimiter)
- `gh pr comment` ile cok satirli yorum nasil yazilir?

## Zorluk
Bu gorevde birden fazla adim birbirine veri aktariyor. `$GITHUB_OUTPUT` mekanizmasini ve
`${{ steps.<id>.outputs.<key> }}` syntax'ini iyi anlamaniz gerekiyor.

## Bonus (Opsiyonel)
Gercek bir AI API'si (OpenAI/Anthropic) ekleyerek diff'i analiz ettirebilirsiniz.
Bunun icin repo Settings > Secrets > Actions'a API key eklemeniz gerekir.
