import os
from utils import *


def search(event):
    if keyboard.is_pressed("space"):
        os.system("cls")
        print_main_message({})
        print("What do you wanna search?")
        search_query = input(colorama.Fore.GREEN + ">>> " + colorama.Style.RESET_ALL)
        url = "https://api.github.com/search/repositories"
        params = {'q': search_query}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            try:
                search_results = response.json()
                repositories = search_results['items']
                result = []
                for i in range(1, 10+1):
                    result.append(repositories[i]['full_name'])
                search_result = result
                os.system("cls")
                need_to_explore = search_result[0]
                print_main_message({"1-0": "Allows you to select the search result you are interested in.",
                                    "alt": "Allows you to get selected repository information\n"})
                print(colorama.Fore.GREEN + "Search results:" + colorama.Style.RESET_ALL)
                for index, full_name in enumerate(search_result):
                    print(f"{index + 1}) {full_name}")
                keys_to_monitor = [str(i) for i in range(1, 10)] + ['0']

                while True:
                    for key in keys_to_monitor:
                        if keyboard.is_pressed(key):
                            os.system("cls")
                            print_main_message({"1-0": "Allows you to select the search result you are interested in.",
                                                "alt": "Allows you to get selected repository information\n"})
                            print(colorama.Fore.GREEN + "Search results:" + colorama.Style.RESET_ALL)
                            for index, full_name in enumerate(search_result):
                                if index+1 == int(key) or int(key) == index-9:
                                    print(colorama.Back.GREEN + f"{index + 1}) {full_name}" + colorama.Style.RESET_ALL)
                                    need_to_explore = full_name
                                else:
                                    print(f"{index + 1}) {full_name}")
                    if keyboard.is_pressed('alt') and need_to_explore:
                        os.system("cls")
                        get_repo_info(need_to_explore)
                        break
            except IndexError:
                print_error_message("Nothing found.")
        else:
            print_error_message("Failed to load search results.")




