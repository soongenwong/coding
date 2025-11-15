import requests

def topArticles(limit):
    articles = []
    page = 1
    
    while True:
        response = requests.get(f'https://jsonmock.hackerrank.com/api/articles?page={page}')
        data = response.json()
        
        for item in data['data']:
            title = item['title'] if item['title'] else item['story_title']
            if title:
                comments = item['num_comments'] if item['num_comments'] is not None else 0
                articles.append((title, comments))
        
        if page >= data['total_pages']:
            break
        page += 1
    
    articles.sort(key=lambda x: (-x[1], x[0]))
    return [title for title, _ in articles[:limit]]