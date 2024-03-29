from os import path
import json

home = path.expanduser("~")
qtile_path = path.join(home, '.config', 'qtile')
qtile_scripts = path.join(qtile_path, "scripts")
qtile_themes = path.join(qtile_path, "themes")
config = path.join(qtile_path, "manager.json")

def check_theme():
    theme = "default"
    if path.isfile(config):
        with open(config) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            f.write(f'{{\n"theme": "{theme}\n"}}\n')
    return theme


def theme_selector(theme=check_theme()):
    # 1 theme in 1 file
    theme_file = path.join(qtile_themes, f'{theme}.json')
    if not path.isfile(theme_file):
        return 0
    with open(theme_file) as f:
        return json.load(f)


def theme_selector_v2(theme=check_theme()):
    theme_file = path.join(qtile_themes, 'themes.json')

    if not path.isfile(theme_file):
        return 0
    with open(theme_file) as f:
        return json.load(f)[theme]


def scheme_selector():
    if theme_selector() != 0:
        return theme_selector()

    if theme_selector_v2() != 0:
        return theme_selector_v2()

    return theme_selector_v2("default")


def check_property(property:str):
    prop=''
    with open(config) as f:
        prop = json.load(f)[property]
    return prop

browser = check_property("browser")
theme = scheme_selector()
editor = check_property("editor")
fileManager = check_property("fileManager")
font = check_property("font") # nerd fonts https://www.nerdfonts.com/cheat-sheet
mail = check_property("mail")
terminal = check_property("terminal")
