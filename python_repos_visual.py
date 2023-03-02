import requests

from plotly import offline

# Sukuriame kintamaji kuriame yra API kvietimas.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# nurodom naujausia API versija, nes kitaip mes error
headers = {'Accept': 'application/vnd.github.v3+json'}

# Naudojam get() metoda perduodame URL ir header,
# o atsakymo objektą priskiriame kintamajam r.
# Atsakymo objektas turi atributą status_code, kuris nurodo, ar užklausa buvo sėkminga.
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# API atsakui priskiriam kintamaji
response = r.json()
repos = response['items']

# Sukuriam listus, kuriuose saugosim duomenis, kuriuos atvaizduosim
repo_links, stars, labels = [], [], []
for repo in repos:
    repo_name = repo['name']
    repo_url = repo['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo['stargazers_count'])
    owner = repo['owner']['login']
    description = repo['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Sukuriam listą. Jame yra žodynas, nurodo ploto tipa (bar) ir nurodo
# x ir y duomenis, hovertext čia ką matysim užėję su pele

data = [{'type': 'bar', 'x': repo_links, 'y': stars, 'hovertext': labels,'marker':
    { 'color': 'rgb(60, 100, 150)', 'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}},
    'opacity': 0.6,}]

# Apsirašom diagramos išdėstymą naudodami žodyno metodą.
# Naudojame žodyną su norimomis maketavimo specifikacijomis.
# Sukuriame diagramos pavadinimą ir kiekvienai ašiai title.

layout = {'title': 'Most Starred Python Projects on GitHub', 'titlefont': {'size': 28}, 'xaxis':
    {'title': 'Repository', 'titlefont': {'size': 24}, 'tickfont': {'size': 14},},'yaxis':
    {'title': 'Stars', 'titlefont': {'size': 24}, 'tickfont': {'size': 14}, },}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='python_repos.html')
