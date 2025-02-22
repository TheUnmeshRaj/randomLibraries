import webbrowser

# List of phones to search
phones = [
    "Realme Narzo 70 Pro",
    "iQOO Z9 / Vivo T3",
    "Samsung Galaxy M35 5G",
    "Moto G85",
    "POCO X6",
    "POCO M6 Plus 5G",
    "Moto G64"
]


def get_amazon_search_url(phone):
    query = phone.replace(" ", "+")
    return f"https://www.amazon.in/s?k={query}"

def get_flipkart_search_url(phone):
    query = phone.replace(" ", "+")
    return f"https://www.flipkart.com/search?q={query}"


for phone in phones:
    print(f"Opening search results for {phone}...")
    amazon_url = get_amazon_search_url(phone)
    flipkart_url = get_flipkart_search_url(phone)
    
    webbrowser.open_new_tab(amazon_url)
    webbrowser.open_new_tab(flipkart_url)
