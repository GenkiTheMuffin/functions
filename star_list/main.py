def star_list(width: int, text=""):
    if text != "":
        text = " " + text + " "
    front_padding = (width - len(text)) // 2
    back_padding = width - len(text) - front_padding
    print("*" * front_padding + text + "*" * back_padding)


star_list(40)
star_list(40, "kys")
