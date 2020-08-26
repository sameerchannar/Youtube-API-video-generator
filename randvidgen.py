import json
import urllib.request
import string
import random
import webbrowser

usercontinue = True
loopcount = 0
while (usercontinue and loopcount < 10):
    loopcount += 1
    #setup web browser
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

    #random video id API request
    count = 1
    API_KEY = '<omitted for security>'
    randomstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,randomstring)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    #print(data)
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    videoids = []


    #store data from API request
    for data in results['items']:
        videoId = (data['id']['videoId'])
        videoids.append(videoId)
        views = (data['id'])
        #store your ids
        #webbrowser.get('chrome').open('https://www.youtube.com/watch?v=' + videoId)

    print(videoids)

"""

    #obtain statistics of video
    for video in videoids:
        stats = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=' + video + '&key={}'.format(API_KEY)
        statsURL = urllib.request.urlopen(stats)
        statsdata = statsURL.read()
        statsencoding = statsURL.info().get_content_charset('utf-8')
        statsresults = json.loads(statsdata.decode(statsencoding)) #convert into list

        views = statsresults['items'][0]['statistics']['viewCount']
        print("views: " + views)
        if int(views) < 100000:
            print("not popular")
        else:
            print("popular")
        usercontinue = False
        userinput = input("Continue? ")
        if (userinput == "Yes" or userinput == "yes"):
            usercontinue = True
"""