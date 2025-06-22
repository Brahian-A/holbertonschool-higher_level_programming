import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
        posts = response.json()
        for post in posts:
            print(post["title"])
        return posts

    print("Error al obtener los datos.")
    return []


def fetch_and_save_posts():
    posts = fetch_and_print_posts()
    if not posts:
        print("No hay datos para guardar.")
        return

    fieldnames = ["id", "title", "body"]
    filtered_posts = [{k: post[k] for k in fieldnames} for post in posts]

    with open("posts.csv", mode="w", newline="",
              encoding="utf-8") as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_posts)

    print("Los posts se guardaron en posts.csv")


if __name__ == "__main__":
    fetch_and_save_posts()