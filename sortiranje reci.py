#author: DanijelXDA
# Program koji sortira
# date reči sa standardnoh
# ulaza
mojString = "Haj, ovo je samo niz reci.";

# Učitaj string 
mojString = input("Unesite string:  ");
reci = mojString.split();

# Sortiranje reči
reci.sort();

print("Sortiranje reci:\n");

for rec in reci:
    print(rec);