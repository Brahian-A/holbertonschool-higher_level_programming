import requests
import csv


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Error al obtener los datos.")


def fetch_and_save_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        filtered_posts = ["id", "title", "body"]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
            writer.writerows(filtered_posts)

        print("Los posts se han guardado en posts.csv")
    else:
        print("Error al obtener los datos.")


if __name__ == "__main__":

    fetch_and_print_posts()
    fetch_and_save_posts()
