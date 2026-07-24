import pandas as pd

df = pd.read_csv("D:/App Data/netflix_titles.csv.zip")

print("\n-----------Data Description-----------")
print(df.info())

print("\n-------Null Values-------")

print(df.isnull().sum())

print("\n-------Rows x Columns-------")
print(df.shape)

print("\n-------Top 5 Rows-------")
print(df.head())

print("\n-------Last 5 Rows-------")
print(df.tail())

print("\n-------Duplicate values-------")
print(df.duplicated().sum())

print("\n----------Date column format---------")
print(df["date_added"])


print("\n-------Convertinng Date DType & Checking null values again-------")
df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="%B %d, %Y",
    errors="coerce"
)

print(df.isnull().sum())

print("\n--------------Values creating problems--------------")

invalid_dates = df[df["date_added"].isna()]
print(invalid_dates[["show_id", "date_added"]])
df = pd.read_csv("D:/App Data/netflix_titles.csv.zip")

mask = pd.to_datetime(
    df["date_added"],
    format="%B %d, %Y",
    errors="coerce"
).isna()

print("\n---------Dates didn't convert due to extra spaces---------")

print(df.loc[mask, "date_added"])

df["date_added"] = df["date_added"].str.strip()

df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="%B %d, %Y",
    errors="coerce"
)

print("\nAfter trimming spaces....")

print("\n----------Null values---------")

print(df.isna().sum())

print("\n-------------Data Types------------")
print(df.dtypes)

print("\nFilling null values....")
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["duration"] = df["duration"].fillna(df["duration"].mode()[0])

print("\n----------Null values---------")
print(df.isna().sum())

print("\n-------Rows x Columns-------")
print(df.shape)

print("\nAfter removing Null Dates....")
df = df.dropna(subset=["date_added"])

print("\n-------Rows x Columns-------")
print(df.shape)

print("\n-------------Data Description--------------")
print(df.info())

print("\n---------Null Values---------")
print(df.isnull().sum())

print("\nAfter Capitalizing Title & Removing underscore....")
df.columns = df.columns.str.replace("_", " ").str.title()

print("\n--------------Final Output----------------")
print(df.info())

df.to_csv(r"D:\Python Program\Python Gui or Pandas\netflix_cleaned.csv", index=False)

