# making an API call
# breaking down the URL
'''
https://api.github.com  # Directs the request to GitHub's API
search/repositories     # Searches all GitHub repositories
?q=                     # Begins the query argument
language:python         # Filters for Python repositories
+sort:stars             # Sorts results by numbers of stars
'''


# processing an API
# python_repos.py
import requests
# make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:pythoon+sort:stars:>10000"
header = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# convert the response object to a dictionary
response_dict = r.json()
print(response_dict.keys())


# working with the response dictionary
# explore infrormation about the repositories
print(f"Total repositories: {response_dict["total_count"]}")
print(f"Complete result: {not response_dict["incomplete_results"]}")

repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

# examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
    
    
# visualising repositories using plotly
import requests
import plotly.express as px
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
header = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers = headers)
response_dict = r.json()
repo_dicts = response_dict["items"]
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])
# make visualisation
fig = px.bar(x=repo_names, y=stars)
fig.show()


# styling the chart
# add a title and axis labels
title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)
# customise font size
fig.update_layout(
    title_font_size = 28,
    xaxis_title_font_size = 20,
    yaxis_title_font_size = 20
)
# customise bar colour and transparency
fig.update_traces(marker_colour="SteelBlue", marker_opacity=0.6)
fig.show()


# adding custom tooltips and clickable links
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # clickable link for x-axis label
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict["stargazers_count"])
    # custom tooltip text
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br/>{description}"
    hover_texts.append(hover_text)
    
fig = px.bar(x = repo_links, y = stars, title = title,
             labels = labels, hover_name = hover_texts)


# summarising hacker news top stories
# for operator import itemgetter
# import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)