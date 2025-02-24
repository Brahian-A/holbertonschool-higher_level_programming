import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
        return posts

    print("Error al obtener los datos.")
    return []


def fetch_and_save_posts(posts):
    if not posts:
        print("No hay datos para guardar.")
        return posts

    fieldnames = ["id", "title", "body"]

    with open("posts.csv", mode="w", newline="",
              encoding="utf-8") as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts)

    print("Los posts se han guardado en posts.csv")


if __name__ == "__main__":
    posts = fetch_and_print_posts()
    fetch_and_save_posts(posts)
