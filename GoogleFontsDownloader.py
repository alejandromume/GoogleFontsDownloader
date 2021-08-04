import sys

import requests
from colorama import Fore
from tqdm import tqdm
from sys import argv
import argparse

parser = argparse.ArgumentParser(description="Download Google fonts")
parser.add_argument("-f", "--font", type=str, help="Set the font name")
parser.add_argument("-t", "--type", type=str, help="Set the font type (regular, italic...)")
parser.add_argument("-v", "--variants", help="Get the variants of the font (-f)",action="store_true")
parser.add_argument("-css", "--css", help="Get the import CSS url",action="store_true")
args = parser.parse_args()

font = args.font
type = args.type
variants = args.variants
css = args.css

###########################
api_key = "YOUR-API-kEY"
###########################

if api_key == "YOUR-API-kEY":
    print(f"{Fore.LIGHTRED_EX}You need to add your API key! {Fore.LIGHTYELLOW_EX}Go to https://console.cloud.google.com/marketplace/product/google/webfonts.googleapis.com")
    sys.exit()

if variants and not type and not css and font:
    api = f"https://www.googleapis.com/webfonts/v1/webfonts?key={api_key}"
    resp = requests.get(api)
    result = resp.json()["items"]
    pairs = len(resp.json()["items"])

    for x in result:
        if x["family"] == font:

            var = x["variants"]
            files = x["files"]
            for j in var:
                print(j)

elif font and type and not css and not variants:
    api = f"https://www.googleapis.com/webfonts/v1/webfonts?key={api_key}"
    resp = requests.get(api)
    result = resp.json()["items"]
    pairs = len(resp.json()["items"])

    for x in result:
        if x["family"] == font:

            files = x["files"][type]
            resp = requests.get(files, stream=True)
            total = int(resp.headers.get('content-length', 0))
            with open(f"{font}-{type}.ttf", 'wb') as file, tqdm(
                    desc=f"{font}-{type}.ttf",
                    total=total,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
            ) as bar:
                for data in resp.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)
                file.close()

            print("\n")
            print(f"                 {Fore.LIGHTGREEN_EX}Downloaded successfully! {Fore.RESET}")


if font and not type and not css and not variants:
    url = f"https://fonts.google.com/download?family={font}"

    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(f"{font}.zip", 'wb') as file, tqdm(
            desc=f"{font}.zip",
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

    print("\n")
    print(f"                 {Fore.LIGHTGREEN_EX}Downloaded successfully! {Fore.RESET}")

if font and css and not variants and not type:
    url = f"https://fonts.googleapis.com/css2?family={font}"

    style = """
    <style>
        @import url('"""+ url +"""');
    </style>    
    """

    print(style)