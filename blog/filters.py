

def slugify(title):
    al_num_title = ""
    for letter in title:
        str_letter = str(letter)
        if str_letter.isalnum() or str_letter == " ":
            al_num_title += str_letter
    return "-".join(al_num_title.split()).lower()
