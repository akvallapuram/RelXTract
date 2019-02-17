import wptools
page = wptools.page('Donald Trump').get_parse(show=False)
print(page.data)
