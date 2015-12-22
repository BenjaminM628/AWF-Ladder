from api import *
from library import *
import random
email="benmeshanko@gmail.com"
password="CENSORED"
token=getAPIToken(email, password)
gamename="![AWF Ladder] Week 3"
message="AWF Ladder Game. Shoutout to ppface and kachan for purchasing my Membership!"
def createOne():
    players1 = [andrew, benjamin628, bilboswaggins, blortis, character, lesophagus, jayvan, jim, jplatt821, jt, jz, kachan, legacy, legendofthephoenix, hankypinky, masterofdesaster, ppface, shyb, stealth90, sugi, thethedde, tschombawomba, yellowswag, oscar]
    random.shuffle(players1)
    template1 = 306574
    for x in xrange(0, len(players1)/2):
        teams= [players1[((x+1)*2)-2], players1[((x+1)*2)-1]]
        result = createGame(email, token, template=template1, gameName=gameName, message=message, teams=teams)
        print result
def createTwo():
    players2 = [andrew, benjamin628, bilboswaggins, blortis, jammawind, jayvan, jplatt821, jt, jz, kachan, legacy, hankypinky, marsadpl, ppface, shyb, stealth90, thethedde, tschombawomba, yellowswag, oscar]
    random.shuffle(players2)
    template2 = 761215
    for x in xrange(0, len(players2)/4):
        teams= [[players2[((x+1)*4)-4], players2[((x+1)*4)-3]], [players2[((x+1)*4)-2], players2[((x+1)*4)-1]]]
        result = createGame(email, token, template=template2, gameName=gameName, message=message, teams=teams)
        print result
def createThree():
    players3 = [andrew, benjamin628, bilboswaggins, blortis, jammawind, jayvan, jplatt821, jt, jz, kachan, legacy, legendofthephoenix, hankypinky, ppface, shyb, stealth90, yellowswag, oscar]
    random.shuffle(players3)
    template3 = 477357
    for x in xrange(0, len(players3)/6):
        teams= [[players3[((x+1)*6)-6], players3[((x+1)*6)-5], players3[((x+1)*6)-4]], [players3[((x+1)*6)-3], players3[((x+1)*6)-2], players3[((x+1)*6)-1]]]
        result = createGame(email, token, template=template3, gameName=gameName, message=message, teams=teams)
        print result
    

