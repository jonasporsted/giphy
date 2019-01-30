import requests

# Giphy
random_url = "https://api.giphy.com/v1/gifs/random"
api_key_value = "ljUA9SfDJ3MlGgiUGypcpIhq3oG5iB8C"
chosen_tag = input ("hvilke nogle gifs vil du se?")

# dette er s farve cursor
def hent_gif_url():

    parametre = {
        "api_key": api_key_value,
        "tag": chosen_tag,
    }

    response = requests.get(
        url=random_url,
        params=parametre,
    )

    data = response.json()
    billede = data["data"]["images# dette er s farve cursor
"]["downsized_large"]["url"]
    print(billede)

# Kør funktion her
hent_gif_url()
