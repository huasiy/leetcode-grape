import requests
import json
from types import SimpleNamespace
from weasyprint import HTML

baseJSON = {
    "operationName": "questionTranslations",
    "variables": {
        "titleSlug": "PLACEHOLDER"
    },
    "query": "\n    query questionTranslations($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    translatedTitle\n    translatedContent\n  }\n}\n    "
}

headers = {
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'random-uuid': '1e4654b6-ca63-1819-49ed-fa01136c2664'
}

graphQLEndpoint = 'https://leetcode.cn/graphql/'

htmlstr = '<div>'
htmlstr += '<style> @page { size: A4; margin: 10mm;}\n * { word-wrap: break-word; } pre { white-space: pre-wrap; } </style>'

def update_question_links(question_links):
  with open('question_links.txt') as f:
    links =  f.read()

  links = links.split('\n')

  for each in links:
    question_links.append(each)

def get_section(section_text):
  global htmlstr
  htmlstr += '<div>'
  htmlstr += f'<h1>{section_text[1:]}</h1>'
  htmlstr += '</div>'
  htmlstr += '<p style="page-break-before: always" ></p>'

def get_question(question_link):
  slug = question_link.split('https://leetcode.cn/problems/', 1)[1]
  slug = slug.split('/',1)[0]
  baseJSON['variables']['titleSlug'] = slug

  resp = requests.get(graphQLEndpoint, json=baseJSON, headers=headers)
  if resp.status_code != 200:
    print(f"Request for {slug} failed, status code is {resp.status_code}")
    return
  else:
    print(f"Request for {slug} succeed")
  x = json.loads(resp.text, object_hook=lambda d: SimpleNamespace(**d))

  global htmlstr
  htmlstr += '<p style="page-break-before: always" ></p>'
  htmlstr += '<div>'
  htmlstr += f'<h2>{x.data.question.translatedTitle}</h2>'
  htmlstr += x.data.question.translatedContent 
  htmlstr += '</div>'

def main():
  question_links = []
  update_question_links(question_links)
  for line in question_links:
    try:
      if line[0] == '~':
        get_section(line)
      else:
        get_question(line)
    except:
      continue
  
  global htmlstr
  htmlstr += '</div>'
  HTML(string=htmlstr).write_pdf('questions.pdf')


if __name__=='__main__':
  print('\n')
  main()
  
