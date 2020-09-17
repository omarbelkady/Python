fav_langs={"python", "javascript", "C#", "C++","Java"}
nelan_favs= {"pascal", "Java","Assembly", "C","Machine Language"}

#Union symbol: | combine two sets and remove any duplicates
all_langs = fav_langs | nelan_favs
print(all_langs)

#ntersection: combine two sets and display the similarity using the ampersand symbol
intersec = fav_langs & nelan_favs
print(intersec)


