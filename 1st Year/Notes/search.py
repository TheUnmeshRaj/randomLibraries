import webbrowser
text = "+".join(input("Search: ").split(" "))
webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+text)

import pywhatkit as pw
pw.playonyt(input("What to play?: "))
