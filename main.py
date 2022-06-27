# copyright(c)2022 Vishal Ahirwar.

from bs4 import BeautifulSoup
import requests as rq
import lxml
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
cpp_code = ""
print("Srapping data ....")
res = rq.get(url=URL)
raw_html = res.text

soup = BeautifulSoup(raw_html, "lxml")
print("%s" % (soup.title.getText()))
movies = soup.find_all(name="h3", class_="title")
movies_list = [movie.getText() for movie in movies]
movies_list = movies_list[::-1]


with open("index.html", mode="w") as file:
    file.write("""
    <html>
    <head>
    <title>Top 100 Movies of 21th Century</title>
    </head>
    <body>""")
    for movie in movies_list:
        print(movie)
        file.write("<h3>"+movie+"</h3>\n")
    file.write("</body></html>")

# for movie in movies:
#     print(movie.getText())

# cpp_code = """
# //Copyright(c)2022 Vishal Ahirwar.
# #include<iostream>
# int main(void)
# {
#     const char*raw_html={R"--(%s)--"};
#     std::cout<<raw_html<<std::endl;
#     return 0;};
# """

# with open("index.cc", mode='a') as file:
#     file.write(cpp_code%(soup.prettify()))
