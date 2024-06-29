import requests

def search_gifs(search_query, api_key, limit=5):
    url = f"https://api.giphy.com/v1/gifs/search"
    params = {
        'api_key': api_key,
        'q': search_query,
        'limit': limit
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        gif_urls = []
        for gif in data['data']:
            gif_url = gif['images']['downsized']['url']
            gif_urls.append(gif_url)

        return gif_urls

    except requests.exceptions.RequestException as e:
        print(f"Помилка отримання даних: {e}")
        return []

def main():
    api_key = 'cBbsmSW1e4K0gxcMhAMs6TDINEzEUYFi'
    search_query = input("Введіть слово для пошуку GIF-зображень: ")
    gif_urls = search_gifs(search_query, api_key)

    print(f"\nОсь посилання на GIF-зображення, пов'язані із '{search_query}':\n")
    for url in gif_urls:
        print(url)

main()