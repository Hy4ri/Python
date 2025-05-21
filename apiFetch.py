import requests

base_url = "https://pokeapi.co/api/v2/"


def get_poke_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"failed erorr {response.status_code}")


poke_name = input("Enter a Pokemon: ")
poke_data = get_poke_info(poke_name)

if poke_data:
    print(f"name: {poke_data['name']}")
