import requests

# Sukuriame kintamaji kuriame yra API kvietimas.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# nurodom naujausia API versija, nes kitaip mes error
headers = {'Accept': 'X-GitHub-Api-Version:2022-11-28'}

# Naudojam get() metoda perduodame URL ir header,
# o atsakymo objektą priskiriame kintamajam r.
# Atsakymo objektas turi atributą status_code, kuris nurodo, ar užklausa buvo sėkminga.
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# API grąžina informaciją JSON formatu, todėl mes naudojame json() metodą,
# norėdami konvertuoti informaciją į Python žodyną
# gautą žodyną saugome response.
response = r.json()

# Atspausdiname vertę, susietą su total_count,
# kuri parodo bendrą „Python“ repozitorijų skaičių „GitHub“.
print(f"Total repositories: {response['total_count']}")

# Informacija apie repozitorijas.
# items yra žodynų list'as su atskirom Python repozitorijom
# Tada atspausdiname repos, kad matytume, apie kiek repozitoriju turime informacijos.
repos = response['items']
print(f"Repositories returned: {len(repos)}")

#Kai kursim vizualizaciją, norėsime įtraukti daugiau nei vieną repozitorija. Tai parasom
# for cikla su mum reikiama info

print("\nInformation about each repository:")
for repo in repos:
# projekto pavadinimas
    print(f"Name: {repo['name']}") #projekto pavadinimas
# naudojam owner login kad pasiekti žodyną, kuris priklauso tam tikram vartotojui su atititnkamu loginu
    print(f"Owner: {repo['owner']['login']}")
# kiek žvaigdžių turi projektas ir projekto GitHub URL
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository: {repo['html_url']}")
    print(f"Created: {repo['created_at']}")
    print(f"Updated: {repo['updated_at']}")
    print(f"Description: {repo['description']}")
