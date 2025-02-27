import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url):
    response = requests.get(doc_url)
    if response.status_code != 200:
        print("Error: Unable to fetch the document.")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if not table:
        print("Error: No table found in the document.")
        return

    data = []
    rows = table.find_all('tr')[1:]

    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 3:
            continue

        try:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            data.append((x, y, char))
        except ValueError:
            continue

    if not data:
        print("Error: No valid data found.")
        return

    max_x = max(entry[0] for entry in data)
    max_y = max(entry[1] for entry in data)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in data:
        grid[y][x] = char
    for row in grid:
        print(''.join(row))

doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
decode_secret_message(doc_url)

