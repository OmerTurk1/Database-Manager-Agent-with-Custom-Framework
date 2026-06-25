import pandas as pd

# Veri setini yükle
file_path = 'train.csv'
df = pd.read_csv(file_path)

# Veri özet bilgisi
print('=== Veri yapısı ===')
print(df.info())

# İlk birkaç satır
print('\n=== İlk 5 satır ===')
print(df.head())

# Temel istatistikler
print('\n=== Sayısal sütunların temel istatistikleri ===')
print(df.describe())

# Eksik verilerin analizi
print('\n=== Eksik değerlerin oranı ===')
missing_ratio = df.isnull().mean() * 100
print(missing_ratio[missing_ratio > 0])

# Kategorik sütunların frekans analizleri
print('\n=== Kategorik sütunların frekans değerleri ===')
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    print(f'\n-- {col} --')
    print(df[col].value_counts(dropna=False))

# Korelasyon matrisi
print('\n=== Sayısal sütunların korelasyon matrisi ===')
df_numeric = df.select_dtypes(include=[float, int])
print(df_numeric.corr())

# Özet
print('\n=== Veri seti analizi tamamlandı ===')
