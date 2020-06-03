import os
import glob
import requests
import time

QUESTION_SET = requests.get("https://leetcode.com/api/problems/all/").json()['stat_status_pairs']
levels = {1: "Easy", 2: "Medium", 3: "Hard"}
def find_question(query):
    if 'http' in query:
        question_title = query.partition("/problems/")[2].partition("/")[0]
        for question in QUESTION_SET:
            if question['stat']['question__title_slug'] == question_title:
                return 'https://leetcode.com/problems/{}/'.format(question_title)
    else:
        for question in QUESTION_SET:
            if str(question['stat']['frontend_question_id']) == query:
                return 'https://leetcode.com/problems/{}/'.format(question['stat']['question__title_slug'])

def return_question_filename(url):
    return url.partition("/problems/")[2].partition("/")[0] + ".png"

def write_to_markdown(fileName):
    question_title = fileName.partition(".pn")[0]
    for question in QUESTION_SET:
        if question['stat']['question__title_slug'] == question_title:
            url = 'https://leetcode.com/problems/{}/'.format(question_title)
            os.system("echo >> ../README.md")
            os.system("echo >> ../README.md")
            difficulty = levels[question['difficulty']['level']]
            number = question['stat']['frontend_question_id']
            title = question['stat']['question__title']

            os.system("echo '## [{} - #{} | Difficulty: {}]({})' >> ../README.md".format(title, number, difficulty, url))
            os.system("echo >> ../README.md")
            os.system("echo '[![N|Solid](images/{})](#)' >> ../README.md".format(fileName))

if __name__ == '__main__':
    query = raw_input("search: ")
    sizeVal = len(glob.glob("../croppedImages/*.png"))
    while len(query) > 0:
        x = return_question_filename(find_question(query))
        os.system("open {}".format(x))
        while len(glob.glob("../croppedImages/*.png")) != sizeVal:
            time.sleep(1)
        croppedImage = sorted(glob.glob("../croppedImages/*.png"), key=os.path.getmtime)[-1]
        print croppedImage
        os.system("mv '{}' ../images/{}".format(croppedImage, x))
        write_to_markdown(x)
        sizeVal = len(glob.glob("../croppedImages/*.png"))
        query = raw_input("search: ")
    main()