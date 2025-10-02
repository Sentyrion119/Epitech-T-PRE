text = "hello world"
text_list = list(text)
print(text_list)
text_list[5] = "x"
new_text = "".join(text_list)
print(new_text)  # "helloxworld"