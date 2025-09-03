import requests


def post():
    data = {'UCID': None, 'first_name': None, 'last_name': None, 'github_username': None, 'discord_username': None,
            'favorite_cartoon': None, 'favorite_language': None, 'movie_or_game_or_book': None, 'section': None}

    for i in data:
        data[i] = input(f"Please enter your {i}:")

    url = 'https://student-info-api.netlify.app/.netlify/functions/submit_student_info'
    post_data = requests.post(url, json=data)

    print(f"Status: {post_data.status_code}")
    print(f"Body: {post_data.text}")


def get():
    url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info?UCID=as4384&section=101"
    get_data = requests.get(url)
    print(get_data.json())


if __name__ == "__main__":
    response = input("Enter 'p' for Post or 'g' for Get: ")
    if response == "p":
        post()
    elif response == "g":
        get()
    else:
        print("Invalid Input")
