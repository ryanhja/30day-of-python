import numpy as np
import webbrowser

nb_a = [4,5,6]

print(nb_a*2)

nb_b = np.array(nb_a)

print(nb_b*2)

urls = ['https://www.google.com', 'https://www.facebook.com']

for url in urls:
    webbrowser.open_new_tab(url)