import os
import glob
import requests
import time

QUESTION_SET = requests.get("https://leetcode.com/api/problems/all/").json()['stat_status_pairs']

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
        os.system("mv '{}' ../{}".format(croppedImage, x))
        sizeVal = len(glob.glob("../croppedImages/*.png"))
        query = raw_input("search: ")
    main()