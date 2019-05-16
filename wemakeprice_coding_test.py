# 위메프 코딩 테스트
# 작성자 : 박 상 민
# 주  제 : biz_logic
# 일  시 : 2019-05-17

import re
import requests
from bs4 import BeautifulSoup

class Biz_logic():

	def url_parser(self, url):
		url_link = url
		html = ""
		resp = requests.get(url_link)
		
		if resp.status_code == 200:
			html = resp.text

		html = BeautifulSoup(html, 'html.parser')

		return html

	def text_type(self, type_text, html_text):
		if type_text == '0':

			tag_remover = re.compile('<.+?>')
			content = re.sub(tag_remover, '', str(html_text))

			return content
		
		elif type_text == '1':

			return str(html_text)

	def word_selection(self, origin_text):

		alpha = []
		alpha_sort = []
		number = []
		ascii_sort = []
		up_ascii = [i for i in range(65, 91)]
		low_ascii = [j for j in range(97, 123)]
		
		sort_alpha = []

		for i, j in zip(up_ascii, low_ascii):
			ascii_sort.append(i)
			ascii_sort.append(j) 
		
		temp = ''

		word_selecter = re.compile('[a-zA-Z0-9]+')
		content = word_selecter.findall(origin_text)
	
		for token in content:
			temp = temp + token
		
		for char in temp:
			if char.isalpha():
				alpha.append(char)
			elif char.isdigit():
				number.append(char)

		for target in ascii_sort:
			
			for i in range(0, len(alpha)):
				if target == ord(alpha[i]):
					alpha_sort.append(alpha[i])


		number.sort()	

		return alpha_sort, number
	
	def printer(self, pre_alpha, num):

		sorted_text = ''

		alpha_len = len(pre_alpha)
		num_len = len(num)

		if alpha_len > num_len:
			for i in range(num_len, alpha_len):
				num.append('none')

		elif num_len > alpha_len:
			for i in range(alpha_len, num_len):
				pre_alpha.append('none')

		for a, n in zip(pre_alpha, num):

			if a != 'none':
				sorted_text = sorted_text + a

			if n != 'none':
				sorted_text = sorted_text + n
			
			
		pack = int(input("출력 묶음 단위 : "))
		
		remainder_num = len(sorted_text)%pack
		
		quotient = sorted_text[0:len(sorted_text)-remainder_num]
		remainder = sorted_text[len(sorted_text)-remainder_num:]
		
		return quotient, remainder

if __name__ == "__main__":

	biz = Biz_logic()
	url = input("URL : ")
	html_text = biz.url_parser(url)
	type_text = input("Type(0: remove tag, 1:original text) : ")
	origin_text = biz.text_type(type_text, html_text)
	pre_alpha, num = biz.word_selection(origin_text)
	quotient, remainder = biz.printer(pre_alpha, num)
	print("몫 : " + quotient)
	print("나머지 : " + remainder)



