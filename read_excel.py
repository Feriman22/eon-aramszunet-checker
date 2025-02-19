import pandas as pd
import os
import sys

def download_file(url, output_path):
    """Letölti a fájlt a megadott URL-ről."""
    import requests
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"Fájl letöltve: {output_path}")
    else:
        print(f"Hiba történt a fájl letöltése közben. Státusz kód: {response.status_code}")
        exit(1)

def read_excel(file_path, search_term):
    """Beolvassa az Excel fájlt és szűr a megadott szóra."""
    try:
        # Excel fájl beolvasása
        df = pd.read_excel(file_path)
        # Szűrés a megadott szóra
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term).any(), axis=1)]
        if not filtered_df.empty:
            print(f"Találatok a '{search_term}' szóra:")
            print(filtered_df.to_string(index=False))
        else:
            print(f"Nincs találat a '{search_term}' szóra.")
    except Exception as e:
        print(f"Hiba történt az Excel fájl feldolgozása közben: {e}")

if __name__ == "__main__":
    # Ellenőrizze, hogy a szűrési kifejezés meg van-e adva
    if len(sys.argv) != 2:
        print("Használat: python read_excel.py <szűrési_kifejezés>")
        exit(1)

    # Szűrési kifejezés lekérése
    search_term = sys.argv[1]

    # Fájl letöltése
    file_url = "https://fbapps.cloudwave.hu/eon/eonuzemzavar/page/xls"
    file_name = "eon-aramszunet.xls"
    download_file(file_url, file_name)

    # Excel fájl feldolgozása
    read_excel(file_name, search_term)
