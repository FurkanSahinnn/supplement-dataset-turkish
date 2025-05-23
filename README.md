# Supplement Veri Seti (Türkçe)

Bu veri seti, spor ve fitness alanlarında kullanılan takviyeler (supplement) hakkında kapsamlı bilgiler içeren Türkçe bir kaynaktır. Veri seti, GPT-4o ile oluşturulmuştur ve çeşitli takviyeler hakkında bilimsel temelli bilgiler sunmaktadır.

## Veri Seti İçeriği

Veri seti aşağıdaki formatlarda sunulmaktadır:
- `supplements.json`: JSON formatında tüm verileri içerir
- `supplements.csv`: CSV formatında tüm verileri içerir
- `image/`: Her takviye için bilgilendirici görsel içeren klasör

Her takviye için aşağıdaki bilgiler mevcuttur:
- Takviyenin Adı
- Kategori
- Temel Etkileri
- Fitness Kullanımı
- Sağlık Kullanımı
- Bilimsel Destek
- Yaygın Dozaj
- Riskler
- Kaynak Bağlantıları
- Görsel URL'si (GitHub üzerindeki görsele doğrudan bağlantı)

## Veri Seti Kullanımı

Bu veri seti şu amaçlarla kullanılabilir:
- Fitness ve beslenme uygulamaları için referans veritabanı
- Spor ve sağlık içeriği oluşturanlar için kaynak
- Fitness eğitmenleri ve sağlık profesyonelleri için eğitim materyali
- Supplement seçiminde tüketicilere yardımcı olmak için bilgilendirme

### Örnek Python Kullanımı

```python
# Görselleri kullanma örneği
import requests
from PIL import Image
from io import BytesIO

# JSON verisinden supplement bilgisi al
with open('supplements.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Belirli bir supplement için görseli indir
supplement_name = "Kreatin"
for item in data:
    if item['name'] == supplement_name:
        # Görseli URL'den indir
        response = requests.get(item['image_url'])
        img = Image.open(BytesIO(response.content))
        # Görseli kaydet
        img.save(f"{supplement_name}.png")
        print(f"Görsel kaydedildi: {supplement_name}.png")
        break
```

## Uyarı

Bu veri seti eğitim amaçlı oluşturulmuştur. Supplement kullanımına başlamadan önce her zaman sağlık uzmanlarına danışılmalıdır. Buradaki bilgiler tıbbi tavsiye yerine geçmez.

## Lisans

Bu veri seti MIT lisansı altında paylaşılmaktadır. Akademik, ticari veya kişisel projelerde serbestçe kullanılabilir ve değiştirilebilir.

## İletişim

Veri seti hakkında sorularınız veya önerileriniz için GitHub üzerinden iletişime geçebilirsiniz.

---

# Supplements Dataset (Turkish)

This dataset contains comprehensive information about supplements used in sports and fitness, in Turkish. The dataset was created using GPT-4o and provides scientifically-based information about various supplements.

## Dataset Content

The dataset is provided in the following formats:
- `supplements.json`: Contains all data in JSON format
- `supplements.csv`: Contains all data in CSV format
- `image/`: Folder containing informative visuals for each supplement

For each supplement, the following information is available:
- Supplement Name
- Category
- Primary Effects
- Fitness Usage
- Health Usage
- Scientific Support
- Common Dosage
- Risks
- Source Links
- Image URL (Direct link to the image on GitHub)

## Dataset Usage

This dataset can be used for:
- Reference database for fitness and nutrition applications
- Resource for sports and health content creators
- Educational material for fitness trainers and health professionals
- Informing consumers to help with supplement choices

### Example Python Usage

```python
# Example of using images
import requests
from PIL import Image
from io import BytesIO

# Get supplement information from JSON data
with open('supplements.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Download image for a specific supplement
supplement_name = "Kreatin"
for item in data:
    if item['name'] == supplement_name:
        # Download image from URL
        response = requests.get(item['image_url'])
        img = Image.open(BytesIO(response.content))
        # Save the image
        img.save(f"{supplement_name}.png")
        print(f"Image saved: {supplement_name}.png")
        break
```

## Warning

This dataset was created for educational purposes. Always consult healthcare professionals before starting any supplement. The information here does not substitute medical advice.

## License

This dataset is shared under MIT license. It can be freely used and modified in academic, commercial, or personal projects.

## Contact

For questions or suggestions about the dataset, please contact via GitHub. 
