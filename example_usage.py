import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# JSON veri setini yükleme
def load_json_data():
    with open('supplements.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# CSV veri setini yükleme
def load_csv_data():
    return pd.read_csv('supplements.csv')

# Kategorilere göre gruplandırma
def group_by_category(data):
    categories = {}
    for item in data:
        category = item['category']
        if category in categories:
            categories[category].append(item['name'])
        else:
            categories[category] = [item['name']]
    return categories

# Primary effects analizi
def analyze_primary_effects(data):
    all_effects = []
    for item in data:
        all_effects.extend(item['primary_effects'])
    
    effect_counter = Counter(all_effects)
    return effect_counter

# Görselleştirme - Kategori Dağılımı
def visualize_categories(categories):
    plt.figure(figsize=(12, 6))
    category_counts = {k: len(v) for k, v in categories.items()}
    sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    
    labels = [item[0] for item in sorted_categories]
    counts = [item[1] for item in sorted_categories]
    
    plt.bar(labels, counts)
    plt.xticks(rotation=45, ha='right')
    plt.title('Supplement Kategorilerine Göre Dağılım')
    plt.xlabel('Kategori')
    plt.ylabel('Adet')
    plt.tight_layout()
    plt.savefig('category_distribution.png')
    plt.close()

# Supplement Özelliklerini Görüntüleme
def show_supplement_details(data, supplement_name):
    for item in data:
        if item['name'].lower() == supplement_name.lower():
            print(f"Supplement: {item['name']}")
            print(f"Kategori: {item['category']}")
            print("\nTemel Etkileri:")
            for effect in item['primary_effects']:
                print(f"- {effect}")
            print(f"\nFitness Kullanımı: {item['fitness_use']}")
            print(f"\nSağlık Kullanımı: {item['health_use']}")
            print(f"\nBilimsel Destek: {item['scientific_support']}")
            print(f"\nYaygın Dozaj: {item['common_dosage']}")
            print(f"\nRiskler: {item['risks']}")
            print("\nKaynaklar:")
            for source in item['source_links']:
                print(f"- {source}")
            return
    
    print(f"{supplement_name} adlı supplement bulunamadı.")

# Örnek kullanım
if __name__ == "__main__":
    # JSON verisini yükleme
    data = load_json_data()
    
    # Kategorilere göre gruplandırma
    categories = group_by_category(data)
    print("Kategorilere göre gruplandırma:")
    for category, supplements in categories.items():
        print(f"{category}: {len(supplements)} supplement")
    
    # Görselleştirme
    visualize_categories(categories)
    print("\nKategori dağılım grafiği 'category_distribution.png' olarak kaydedildi.")
    
    # Belirli bir supplement hakkında detaylı bilgi
    print("\nBelirli bir supplement hakkında detaylı bilgi:")
    show_supplement_details(data, "Kreatin")
    
    # DataFrame olarak kullanım örneği
    df = load_csv_data()
    print("\nVeri setindeki toplam supplement sayısı:", len(df))
    print("\nÖrnek DataFrame (ilk 5 satır):")
    print(df[['name', 'category']].head())
    
    # Primary effects analizi
    effects = analyze_primary_effects(data)
    print("\nEn yaygın 5 etki:")
    for effect, count in effects.most_common(5):
        print(f"- {effect}: {count} kez") 