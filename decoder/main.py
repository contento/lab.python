
import requests
from bs4 import BeautifulSoup

def print_grid_from_public_doc(doc_url):
    """
    Given the public URL of a published Google Doc containing an HTML table with columns:
    [x-coordinate, Character, y-coordinate],
    this function retrieves and parses the document, extracts the table data,
    builds the grid of characters (filling missing positions with a space),
    and prints the grid so that when viewed in a fixed-width font, the secret message appears.
    """
    # Fetch the published document's HTML.
    response = requests.get(doc_url)
    if response.status_code != 200:
        print("Failed to retrieve the document. Please check the URL and ensure it is published.")
        return

    # Parse the HTML content.
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first table in the document.
    table = soup.find('table')
    if not table:
        print("No table found in the document.")
        return

    # Initialize a dictionary to hold grid data.
    grid_map = {}  # Key: (x, y), Value: character
    max_x = 0
    max_y = 0

    # Iterate over table rows.
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) < 3:
            # We expect three columns: x-coordinate, character, and y-coordinate.
            continue

        # Extract text for each cell and strip whitespace.
        x_str = cells[0].get_text(strip=True)
        character = cells[1].get_text(strip=True)
        y_str = cells[2].get_text(strip=True)

        try:
            x = int(x_str)
            y = int(y_str)
        except ValueError:
            # Skip rows with invalid x or y coordinate.
            continue

        grid_map[(x, y)] = character
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Build and print the grid.
    for row in range(max_y + 1):
        row_chars = []
        for col in range(max_x + 1):
            row_chars.append(grid_map.get((col, row), ' '))
        print("".join(row_chars))


if __name__ == "__main__":
    # File locally saved as
    #   ./encoded-document.html
    my_doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

    print_grid_from_public_doc(my_doc_url)
