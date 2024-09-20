import requests
from bs4 import BeautifulSoup

def scrape_news_details():
    url = 'https://edition.cnn.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    projects = []

    for item in soup.find_all('div', class_='container__item'):
        title_div = item.find('div', class_='container__text container_list-headlines__text')
        if title_div:
            title = title_div.find('span', class_='container__headline-text').text.strip() if title_div.find('span', class_='container__headline-text') else "No title"
            project_url = item.find('a')['href'] if item.find('a') else "No URL"

            if project_url.startswith('/'):
                project_url = url + project_url

            project_data = {'title': title, 'project': project_url}
            projects.append(project_data)

    return projects

projects = scrape_news_details()

for project in projects:
    print(f"Title: {project['title']}, URL: {project['project']}")
