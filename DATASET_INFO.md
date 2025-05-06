# Veri Seti Oluşturma Süreci

Bu belge, supplement veri setinin oluşturulma sürecini anlatmaktadır.

## Veri Seti Kaynağı

Bu veri seti, OpenAI'nin GPT-4o modeli kullanılarak oluşturulmuştur. Fitness ve supplement alanında geniş bilgi birikimine sahip olan model, bilimsel literatüre dayalı kapsamlı bilgiler sunabilmektedir.

## Oluşturma Metodolojisi

1. **Veri Toplama**: GPT-4o modeline supplement türleri, etkileri ve kullanımları hakkında kapsamlı sorular soruldu.
2. **Yapılandırma**: Elde edilen bilgiler belirli bir format içinde yapılandırıldı (ad, kategori, etkiler, kullanım, riskler vb.)
3. **Doğrulama**: Elde edilen bilgiler bilimsel literatür referanslarıyla eşleştirildi.
4. **Görselleştirme**: Her supplement için açıklayıcı görseller oluşturuldu.
5. **Veri Formatı**: Veriler hem JSON hem de CSV formatlarında düzenlendi.

## İçerik Doğruluğu

Veri setindeki bilgiler, bilimsel literatürden alınan referanslarla desteklenmektedir. Ancak, her zaman güncel bilimsel araştırmaları takip etmek ve sağlık profesyonellerine danışmak önemlidir.

## Güncellemeler ve Katkılar

Bu veri seti, topluluk katkılarına açıktır. Yeni supplementler ekleyebilir, mevcut bilgileri güncelleyebilir veya düzeltmeler önerebilirsiniz. Bunun için GitHub üzerinden pull request gönderebilirsiniz.

## Veri Seti Yapısı

Her supplement için aşağıdaki alanlar bulunmaktadır:

- **name**: Supplement adı
- **category**: Hangi kategoriye ait olduğu (ör. Amino Asit, Vitamin, Mineral)
- **primary_effects**: Ana etkileri (liste halinde)
- **fitness_use**: Fitness/spor alanında kullanım şekli ve faydaları
- **health_use**: Genel sağlık açısından kullanım şekli ve faydaları
- **scientific_support**: Bilimsel literatürde nasıl desteklendiği
- **common_dosage**: Yaygın kullanım dozajı ve şekli
- **risks**: Olası yan etkiler ve riskler
- **source_links**: Bilimsel referans bağlantıları

## GPT-4o Kullanımı Hakkında

Bu veri seti, yapay zeka destekli içerik oluşturmanın bir örneğidir. GPT-4o gibi büyük dil modelleri, bilimsel literatürde yer alan bilgileri derleyerek kapsamlı ve yapılandırılmış veri setleri oluşturmada etkili olabilir.

---

# Dataset Creation Process

This document describes the process of creating the supplement dataset.

## Dataset Source

This dataset was created using OpenAI's GPT-4o model. The model, with extensive knowledge in fitness and supplements, can provide comprehensive information based on scientific literature.

## Creation Methodology

1. **Data Collection**: Comprehensive questions about supplement types, effects, and usage were asked to the GPT-4o model.
2. **Structuring**: The obtained information was structured in a specific format (name, category, effects, usage, risks, etc.)
3. **Verification**: The obtained information was matched with scientific literature references.
4. **Visualization**: Explanatory visuals were created for each supplement.
5. **Data Format**: Data was organized in both JSON and CSV formats.

## Content Accuracy

The information in the dataset is supported by references from scientific literature. However, it is always important to follow current scientific research and consult healthcare professionals.

## Updates and Contributions

This dataset is open to community contributions. You can add new supplements, update existing information, or suggest corrections. To do this, you can send a pull request via GitHub.

## Dataset Structure

The following fields are available for each supplement:

- **name**: Supplement name
- **category**: The category it belongs to (e.g., Amino Acid, Vitamin, Mineral)
- **primary_effects**: Main effects (as a list)
- **fitness_use**: How it is used in fitness/sports and its benefits
- **health_use**: How it is used in general health and its benefits
- **scientific_support**: How it is supported in scientific literature
- **common_dosage**: Common usage dosage and method
- **risks**: Possible side effects and risks
- **source_links**: Scientific reference links

## About GPT-4o Usage

This dataset is an example of AI-assisted content creation. Large language models like GPT-4o can be effective in creating comprehensive and structured datasets by compiling information from scientific literature. 
