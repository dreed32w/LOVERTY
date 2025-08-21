import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich import print
import time

chakel = Console()

arnab = """
        (\_/)
        (•_•)
        (   )
        /   \\
"""
chakel.print(arnab, style="bold yellow")
chakel.print("       [bold red on yellow]   LOVERTY   [/bold red on yellow]")
chakel.print("\n[bold blue]          by mohamed ilkhadry[/bold blue]\n")

def get_headers(url):
    try:
        jawab = requests.get(url)
        if jawab.status_code == 200:
            print(f"[bold red on white]Headers for {url}[/]\n")
            for x, y in jawab.headers.items():
                print(f"[bold yellow]{x}[/] : [bold green]{y}[/]")
        else:
            print("[bold red]no connected[/]")
    except Exception as e:
        print(f"[bold red]erro: {e}[/]")

def get_forms(url):
    try:
        jawab = requests.get(url)
        soup = BeautifulSoup(jawab.text, "html.parser")
        forms = soup.find_all("form")

        if not forms:
            print("[bold red]no HTML form  on this page[/]")
            return

        for i, form in enumerate(forms):
            print(f"\n[bold blue]Form {i+1}[/]")
            print(f" [cyan]Action[/]: {form.get('action')}")
            print(f" [cyan]Method[/]: {form.get('method')}\n")

            inputs = form.find_all(["input", "button"])
            for element in inputs:
                if element.name == "input" and element.get("type") in ["text", "email"]:
                    print("[bold green]name or email input:[/]")
                    print(element.prettify())
                elif element.name == "input" and element.get("type") == "password":
                    print("[bold green]password input:[/]")
                    print(element.prettify())
                elif element.name == "input" and element.get("type") in ["submit", "button"]:
                    print("[bold green]submit input:[/]")
                    print(element.prettify())
                elif element.name == "button":
                    print("[bold green]button :[/]")
                    print(element.prettify())
            print("-" * 30)
    except Exception as e:
        print(f"[bold red]error: {e}[/]")

while True:
    chakel.print("\n[bold green]choose an option:[/]")
    chakel.print("[bold yellow]1[/]: [bold blue]search URL Headers[/]")
    chakel.print("[bold yellow]2[/]: [bold blue]search URL HTML Forms[/]")
    chakel.print("[bold yellow]0[/]: [bold red]exit[/]")

    choice = input("===> ")

    if choice == "1":
        url = input("Enter your URL: ")
        get_headers(url)
    elif choice == "2":
        url = input("Enter your URL: ")
        get_forms(url)
    elif choice == "0":
        print("[bold red]exit.....[/]")
        break
    else:
        print("[bold red]enter 1 or 2 or 0[/]")
