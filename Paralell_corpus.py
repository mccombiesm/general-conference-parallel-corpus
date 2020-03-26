import requests, random, re
from bs4 import BeautifulSoup as bs
import urllib.parse



def return_talk_links(url):

    # get html code and parse to BeautifulSoup object
    webpage = requests.get(url)
    soup = bs(webpage.text, "html.parser")

    # get links
    link_objects = soup.find_all('a')
    links = []
    for link in link_objects:
        if re.findall('^((?!session).)*$',str(link)):
            if re.findall('study/general-conference/', str(link)):
                try:
                    links.append(link.attrs['href'])
                except:
                    print("")
    links = [s.replace('/study', "https://www.churchofjesuschrist.org/study") for s in links]
    print(links)



return_talk_links("https://www.churchofjesuschrist.org/study/general-conference/2013/10?lang=ara")





    # # keep only unique links
    # links = set(links)
    # links = list(links)

    # link_count = 0
    # import os
    # os.chdir("/Users/sethmccombie/Desktop/")
    # with open("Arabic_conference_scrape.txt", mode="a", encoding="utf8") as outfile:
    # for link in links:
    #     print("http://" + str(link))
    #     # outfile.write("http://" + str(link))



    # # scrape text from <p> tags and save to hard drive
    # paragraphs = soup.find_all('p')
    # webpage_name = urllib.parse.urlparse(url).netloc
    # with open("/Users/sethmccombie/Desktop/Arabic_Conference_Talks/saved_text" + str(i + 1) + "-" + webpage_name + ".txt", mode='w', encoding="utf8") as outfile:
    #     outfile.write(webpage_name + '\n')
    #     for p in paragraphs:
    #         outfile.write(p.get_text() + '\n')



# main
arabic_links = ["http://churchofjesuschrist.org/study/general-conference/2019/10?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2019/04?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2018/10?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2018/04?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2017/10?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2017/04?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2016/10?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2015/10?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2015/04?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2014/10?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2014/04?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2013/10?lang=ara",
"http://churchofjesuschrist.org/study/general-conference/2013/04?lang=ara"]

# for url in urls:
#     save_text_and_return_links(url, 0)



# # randomize the order of links, just for fun
# random.shuffle(links)
#
# pages_to_scrape = 10
#
# if len(links) < pages_to_scrape:
#     pages_to_scrape = len(links)
#
# print(pages_to_scrape)
#
# for i in range(pages_to_scrape):
#     print("Working on webpage", i + 1)
#     save_text_and_return_links(links[i], i)


# def get_talk_text(lang1_url,lang2_url):


# with open("Arabic_talk_links_all.txt", mode='r', encoding="utf8") as infile :
#     #work through every link in the file and put it in a list
#     arabic_links = []
#     count = 0
#     for line in infile:
#         line = re.sub("\n","",line)
#         arabic_links.append(line)
#         count += 1
#     arabic_links.sort()
#     arabic_links = list(dict.fromkeys(arabic_links))
#     print(arabic_links)

    # #for every URL in links, scrape the content of all of the P tags and get the webpage name
    # for link in arabic_links:
    #     print("Working on " + str(link))
    #     lang1_url = link
    #     webpage = requests.get(lang1_url)
    #     webpage.encoding = 'utf-8-sig'
    #     soup = bs(webpage.text, "html.parser")
    #     paragraphs = soup.find_all('p')
    #     title = soup.find('h1')
    #     title = title.get_text()
    #     webpage_name = urllib.parse.urlparse(lang1_url).netloc
    #     with open("/Users/sethmccombie/Desktop/Arabic_talks/" + title + ".txt", mode='a', encoding="utf-8-sig") as outfile:
    #         outfile.write(webpage_name + '\n')
    #         for p in paragraphs:
    #             outfile.write(p.get_text() + '\n')





#     webpage = requests.get(lang2_url)
#     webpage.encoding = 'utf-8-sig'
#     soup = bs(webpage.text, "html.parser")
#     paragraphs = soup.find_all('p')
#     webpage_name = urllib.parse.urlparse(lang2_url).netloc
#     with open("/Users/sethmccombie/Desktop/" + webpage_name + "ARA.txt", mode='w', encoding = "utf-8-sig") as outfile:
#         outfile.write(webpage_name + '\n')
#         for p in paragraphs:
#             outfile.write(p.get_text() + '\n')
#             # print(len(str(p.get_text())))
#
#
# lang1_url = "https://churchofjesuschrist.org/study/general-conference/2019/10/11holland?lang=eng"
# lang2_url = "https://churchofjesuschrist.org/study/general-conference/2019/10/11holland?lang=ara"

# get_talk_text(lang1_url, lang2_url)



##Writing to a CSV from two text files
#check to make sure that the number of paragraphs is the same
#open up a csv file

# with open("Arabic file", mode='r', encoding='utf8') as infile1, open("English file", mode='r', encoding='utf8') as infile2, open("the csv file", mode='a', encoding='utf8') as outfile:
#     outfile.write('Arabic talks' + "\t" + "English talk" + "\n")
#     para1 = infile.readlines()
#     para2 = infile.readlines()
#     if len(para1) != len(para2):
#         print("Different number of paragraphs")
#
#         for i in range(len(para1)):
#             outfile.write(para1[1] + "\t" + para2[i] + "\n")
# lines = f.readlines()
# #just get the length of the list
# for i to range()

