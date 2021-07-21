from common.constants import matchType
from re import search, findall


def extractMatchInformation(soupLink):
    matchTypeInf = findMatchType(soupLink)
    if matchTypeInf:
        return True, matchTypeInf, findMatchContenders(soupLink), findScoreCardInformation(soupLink)


def findMatchType(soupLink):
    matUnFormatted = str(soupLink.find("span", class_=""
                                                      "mc-header-info__match-description-match-type mc-theme-color"
                                                      "")).split(">")[1].replace("</span", "").split(" ")[-1]
    return matUnFormatted if matUnFormatted in matchType else False


def findMatchContenders(soupLink):
    contenderInfo = soupLink.find("h1", class_="mc-header-info__title")
    for element in contenderInfo:
        if "<strong>" in str(element):
            host, visitor = str(element).replace("<strong>", "").split("<")[0].split(" v ")
    return host, visitor


def returnDismissalType(streamToRead):
    outCategory = {'CAUGHT': r">c[ ]+([\w| |&|&amp;]+)[ ]+b[ ]+([\w| ]+)", 'LBW': r">lbw[ ]+([\w| ]+)",
                   'BOWLED': r">b[ ]+([\w| ]+)", 'RUNOUT': r">run out[ ]+[(]([\w| ]+)", 'HITWICKET': r">(Hit wicket)<"}
    bowlerNorRequiredList = ['RUNOUT', 'RUNOUT', 'HITWICKET']
    for key, value in outCategory.items():
        if search(value, streamToRead):
            if key not in bowlerNorRequiredList:
                return key, search(value, streamToRead).groups()[-1]
            else:
                return key, "NA"


def findScoreCardInformation(soupLink):
    playerList = []
    for i in range(0, 2):
        scoreContainer = soupLink.find_all(id=f"inning-{i}")
        if [search(r"[ ]+([\w| ]+) Batting", element).group(1) for element in str(scoreContainer).split("\n") if
            "Batting" in element][0] == "India":
            print(f"India is innings {i}")
            for data in scoreContainer:
                for data1 in str(data.find_all("tr", class_="scorecard__row")).split("</tr>"):
                    dismissalInfo = False
                    for data2 in data1.split("\n"):
                        if '<span class="">' in data2:
                            playerName = str(search(r">[ ]+([\w|<strong>| ]+)<", data2).group(1)).replace("<strong>",
                                                                                                          "").upper()
                        elif '<span class="scorecard__dismissal">' in data2:
                            dismissalInfo = returnDismissalType(data2)
                        elif '<span class="scorecard__not-out">' in data2:
                            dismissalInfo = "NOT OUT"
                        if dismissalInfo:
                            regexToMatch = r'.*scorecard__cell.*u-text-center">([<strong>|\d|.]+)<'
                            if search(regexToMatch, data2):
                                response = findall(regexToMatch, data1)
                                strikeRate = \
                                    float(response[0].replace("<strong>", "")) / \
                                    float(response[1].replace("<strong>", "")) if \
                                    float(response[1].replace("<strong>", "")) > 0 else 0
                                dataFieldKey = {'runsScored': float(response[0].replace("<strong>", "")),
                                                'ballsFaced': float(response[1].replace("<strong>", "")),
                                                'strikeRate': float("{0:.2f}".format(strikeRate * 100))}
                        else:
                            dataFieldKey = None
                    playerList.append([playerName, dismissalInfo, dataFieldKey])
                    if len(playerList) == 11:
                        break
    return playerList
