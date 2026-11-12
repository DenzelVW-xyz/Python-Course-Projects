url = input("Input your url: ")
split_url = url.partition("www.")

print(split_url[2])