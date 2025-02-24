import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        return response.json()
    print("Error al obtener los datos.")


def fetch_and_save_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()
        fieldnames = ["id", "title", "body"]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({key: post[key] for key in fieldnames})

        print("Los posts se han guardado en posts.csv")
    else:
        print("Error al obtener los datos.")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
