import requests
import json

VERSION = "17.0.0"


def openmoji_color_url(unicode: str) -> str:
    return f"https://cdn.jsdelivr.net/gh/hfg-gmuend/openmoji@{VERSION}/color/svg/{unicode}.svg"


def openmoji_black_url(unicode: str) -> str:
    return f"https://cdn.jsdelivr.net/gh/hfg-gmuend/openmoji@{VERSION}/black/svg/{unicode}.svg"


class Emoji:
    def __init__(self, hexcode: str, annotation: str):
        self.hexcode = hexcode
        self.annotation = annotation


def main():
    with open("preamble.css", "r") as preamble_file:
        preamble_lines = preamble_file.readlines()

    preamble_lines = [
        line.replace("{VERSION}", f"{VERSION}") if "{VERSION}" in line else line
        for line in preamble_lines
    ]

    response = requests.get(
        f"https://raw.githubusercontent.com/hfg-gmuend/openmoji/{VERSION}/data/openmoji.json"
    )
    data = json.loads(response.text)

    result = [Emoji(item["hexcode"], item["annotation"]) for item in data]

    new = [
        Emoji(
            emoji.hexcode.upper().replace(" ", "-"),
            emoji.annotation.lower()
            .replace(" ", "-")
            .replace(":", "")
            .replace("(", "")
            .replace(")", ""),
        )
        for emoji in result
        if all(
            char.isalpha() or char in [" ", "-", ":", "(", ")"]
            for char in emoji.annotation
        )
    ]

    css_color_classes = [
        f"""
        .oma-{emoji.annotation} {{
            background-image: url("{openmoji_color_url(emoji.hexcode)}")
        }}
        """
        for emoji in new
    ]

    css_black_classes = [
        f"""
        .oma-black-{emoji.annotation} {{
            background-image: url("{openmoji_black_url(emoji.hexcode)}")
        }}
        """
        for emoji in new
    ]

    print(f"Generated a total of {len(new)} emoji CSS classes.")

    with open("openmoji-color-awesome.css", "w") as color_file:
        color_file.writelines(preamble_lines)
        color_file.write(
            f"\n\n/* Generated a total of {len(new)} emoji CSS classes. */\n\n"
        )
        color_file.writelines(css_color_classes)

    with open("openmoji-black-awesome.css", "w") as black_file:
        black_file.writelines(preamble_lines)
        black_file.write(
            f"\n\n/* Generated a total of {len(new)} emoji CSS classes. */\n\n"
        )
        black_file.writelines(css_black_classes)


if __name__ == "__main__":
    main()
