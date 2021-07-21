import requests
from bs4 import BeautifulSoup
from common.constants import matchType
from common.findMatchInformations import extractMatchInformation


class ScrapPage:
    def __init__(self):
        self.MatchInformationDataBase = {}
        for key, value in matchLinkInformation.items():
            connectionHandler = requests.get(value)
            if connectionHandler.status_code == 200:
                print(f"{value} : Connection Success")
                matchId = value.split("/")[value.split("/").index("match") + 1]
                pageSoup = BeautifulSoup(connectionHandler.content, "html.parser")
                try:
                    executionStatus = extractMatchInformation(pageSoup)
                    if executionStatus[0]:
                        print(f"{matchId}   ::  {executionStatus}")
                        '''for element in executionStatus[-1]:
                            print(element)'''
                except Exception as E:
                    print("Exception", E)
            # break


if __name__ == "__main__":
    matchLinkInformation = {}
    htmlFileToProcess = open(r'The Board of Control for Cricket in India.html', "r", encoding="utf8")
    contents = htmlFileToProcess.read().encode()
    beautifulSoupText = BeautifulSoup(contents, 'html.parser')
    with open("xyz.txt", "a", encoding="utf-8") as fp:
        for line in beautifulSoupText.body.prettify().split("\n"):
            fp.write(str(line) + "\n")
            if 'data-match-id' in line:
                dataToParse = line.replace('="', '^').replace(" ", "").replace('"', '^').split("^")
                matchLinkInformation[dataToParse[dataToParse.index("data-match-id") + 1]] = \
                    dataToParse[dataToParse.index("href") + 1]
    fp.close()
    ScrapPage()
