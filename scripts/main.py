from selenium import webdriver
import requests

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


# def go_to_question(driver, questionNum):


if __name__ == '__main__':
	query = raw_input("Question: ")
	question_url = find_question(query)
	print question_url
	# main()