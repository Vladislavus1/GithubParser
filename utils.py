import requests
import colorama
import keyboard
import pyperclip

#main_screen, search_results_panel, repo_information_panel, help_panel, search_input_panel

state = "main_screen"
repo_clone_url = None


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data from {url}: {response.status_code} - {response.reason}")
        return None


def change_current_repo_clone_url(url):
    global repo_clone_url
    repo_clone_url = url


def clone_repo_url(event):
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('q'):
        if repo_clone_url != None:
            pyperclip.copy(f"git clone {repo_clone_url}")
        else:
            pass


def print_error_message(exception):
    print(colorama.Fore.RED + "Error:" + colorama.Style.RESET_ALL + f" {exception}")


def get_repo_info(full_name):
    api_url = f"https://api.github.com/repos/{full_name}"
    repo_info = get_data(api_url)

    if repo_info:
        repo_license = repo_info.get('license', None)
        programming_languages = ", ".join(get_data(repo_info.get('languages_url', {})).keys())
        contributors = [contributor_info['login'] for contributor_info in
                        get_data(repo_info.get('contributors_url', []))] if 'contributors_url' in repo_info else []
        print_main_message({"ctrl + shift + q": "Allows you to copy the repository's clone command if the program is displaying information about a repository.",
                            "esc": "exits program.\n"})
        print(colorama.Fore.GREEN + f"\nRepository Name:" + colorama.Style.RESET_ALL + f" {repo_info['name']}")
        print(colorama.Fore.GREEN + f"Repository Url:" + colorama.Style.RESET_ALL + f" https://github.com/{full_name}")
        print(colorama.Fore.GREEN + f"Description:" + colorama.Style.RESET_ALL + f" {repo_info['description']}")
        print(colorama.Fore.GREEN + f"Owner/Author:" + colorama.Style.RESET_ALL + f" {repo_info['owner']['login']}")
        print(colorama.Fore.GREEN + f"Creation Date:" + colorama.Style.RESET_ALL + f" {repo_info['created_at']}")
        print(colorama.Fore.GREEN + f"Last Updated:" + colorama.Style.RESET_ALL + f" {repo_info['updated_at']}")
        print(colorama.Fore.GREEN + f"Programming Language:" + colorama.Style.RESET_ALL + f" {programming_languages}")

        print(colorama.Fore.GREEN + f"License:" + colorama.Style.RESET_ALL)
        if repo_license:
            print("\t•" + colorama.Fore.GREEN + "Key:" + colorama.Style.RESET_ALL + f" {repo_license['key']}")
            print("\t•" + colorama.Fore.GREEN + "Name:" + colorama.Style.RESET_ALL + f" {repo_license['name']}")
            print("\t•" + colorama.Fore.GREEN + "SPDX id:" + colorama.Style.RESET_ALL + f" {repo_license['spdx_id']}")
            print("\t•" + colorama.Fore.GREEN + "Node id:" + colorama.Style.RESET_ALL + f" {repo_license['node_id']}")
        else:
            print("\t" + colorama.Fore.RED + "License can't be found." + colorama.Style.RESET_ALL)

        print(
            colorama.Fore.GREEN + f"Number of Stars:" + colorama.Style.RESET_ALL + f" {repo_info['stargazers_count']}")
        print(colorama.Fore.GREEN + f"Number of Forks:" + colorama.Style.RESET_ALL + f" {repo_info['forks']}")
        print(colorama.Fore.GREEN + f"Number of Watchers:" + colorama.Style.RESET_ALL + f" {repo_info['watchers']}")

        print(colorama.Fore.GREEN + f"Contributors:" + colorama.Style.RESET_ALL)
        if contributors:
            for index, contributor_login in enumerate(contributors):
                print(f"\t{index + 1}) {contributor_login}")
        else:
            print("\t" + colorama.Fore.RED + "Contributors can't be found." + colorama.Style.RESET_ALL)

        print(colorama.Fore.GREEN + f"Open Issues:" + colorama.Style.RESET_ALL + f" {repo_info['open_issues_count']}")
        print(colorama.Fore.GREEN + f"Latest Release:" + colorama.Style.RESET_ALL + f" {repo_info['pushed_at']}")

        change_current_repo_clone_url(repo_info.get("clone_url", None))
        keyboard.on_press(clone_repo_url)
    else:
        print_error_message("Failed to retrieve repository information.")

def print_main_message(list_of_combinations):
    print("\n")
    if list_of_combinations != {}:
        for key, meaning in list_of_combinations.items():
            print(colorama.Fore.GREEN + f"   {key}" + colorama.Style.RESET_ALL + f" - {meaning}")
    else:
        pass
    print("--------------------\n")



