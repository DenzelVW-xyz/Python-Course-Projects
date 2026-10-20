genre = input("Input the genre (Action, Comedy, Drama, Sci-Fi): ").lower()
rating = input("Input the age rating (PG, PG-13, R): ").lower()

if genre != "action" or rating != "pg":
    print("Move is not suitable for children")
else:
    print("Movie is only suitable for those 13 and up.")