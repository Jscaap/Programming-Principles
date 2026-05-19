# # 2.2 Exercise 1
# '''
# Understanding and Making API Calls
# An API (Application Programming Interface) allows programs to interact with websites via specific
# URLs. These requests, known as API calls, typically return data in formats like JSON or CSV.
# a) Define what an API is in the context of web interaction.
# b) Break down the following GitHub API URL and explain what each component does -
# https://api.github.com/search/repositories?q=language:python+sort:stars.
# c) Install the requests package using a terminal command.
# d) Write a Python program that uses the requests library to make a GET request to the GitHub
# API URL provided above. Parse the JSON response and print the names of the top 5
# repositories
# '''
# # a - what is an API?
# '''
# An API (Application Porgramming Interface) is a system that allows different software application 
# to communicate with each other. 
# In web interaction, an API allows a program to send requests to a website or online service and receive
# data back, usually in formats such as JSON or CSV.
# For example, the GitHub API allows developers to access GitHub data such as repositories, users and commits 
# through specific URLs
# '''

# # b - breakdown of the GitHub API URL
# '''
# https://api.github.com/search/repositories?q=language:python+sort:stars
# https://                The protocol used for secure communication over the internet
# api.github.com          The GitHub API server
# /search/repositories    The API endpoint used to search GitHub repositories
# #                       Starts the query parameters
# q=                      The search query parameter
# language:python         Searches for repositories written in Python
# +                       Combines multiple search conditions
# sort:stars              Sorts repositories by the number of stars
# (This API call searches for Python repositories on GitHub and sorts them according to popularity(stars))
# '''

# # c - intall the requests package
# # pip install requests or pip3 install requests

# # d - Python program using the GitHub API
# import requests
# # GitHub API URL
# url = "https://api.github.com/search/repositories?q=language:python+sort:stars"

# # send GET request
# response = requests.get(url)

# # convert response to JSON
# data = response.json()

# # get repository items
# repositories = data["items"]

# # print top 5 repository names
# print("Top 5 Python repositories on GitHub:\n")

# for repo in repositories[:5]:
#     print(repo["name"])


# # 2.3 Exercise 2
# '''
# Managing Virtual Environments (venv)
# Virtual environments are isolated spaces that keep project dependencies separate from the system-
# wide Python installation, preventing version conflicts.
# a) Provide the command to create a virtual environment named .venv.
# b) Provide the activation commands for both Windows (PowerShell) and macOS/Linux.
# c) Explain how to export your installed packages to a requirements.txt file for collaboration.
# d) Write the command to install packages from a requirements.txt file in a new environment
# '''

# # a - command to cretae a Virtual Environment
# # python -m venv .venv

# # b - activation commands
# # .venv\Scripts\Activate (Windows - PowerShell)
# # source .venv\bin\activate (macOS/Linux)

# # c - export installed packages to requirements.txt
# # pip freeze > requirements.txt

# # d - intall packages from requirements.txt
# # pip install -r requirements.txt


# # 2.4 Exercise 4
# '''
# Processing API Responses and Dictionaries
# Python’s requests library can convert a JSON response into a Python dictionary, allowing you to
# access data using keys.
# a) Write a Python script that.
# 1. Imports the requests library.
# 2. Makes a GET request to
# https://api.github.com/search/repositories?q=language:python+sort:stars.
# 3. Converts the response to a dictionary and prints the total_count of repositories found.
# 4. Includes a check for the status code to ensure the request was successful (code 200).
# 5. Handles potential errors by printing an appropriate message if the request fails.
# '''
# import requests
# # GitHub API URL
# url = "https://api.github.com/search/repositories?q=language:python+sort:stars"

# try:
#     # make GET request
#     response = requests.get(url)
    
#     # check if request was successful
#     if response.status_code == 200:
#         # convert JSON response to Python dictionary
#         response_dict = response.json()
#         # print total number of repositories found
#         print("Request successful")
#         print("Total repositories found:",
#               response_dict["total_count"])
#     else:
#         # handle unsucessful status codes
#         print(f"Request failed with status code: {response.status_code}")

# except requests.exceptions.RequestException as e:
#     # handle request errors
#     print("An error occures while making the request")
#     print("Error: ", e)


# # 2.5 Exercise 4
# '''
# Visualising Data and Rate Limits
# Data retrieved from APIs can be visualised using libraries like Plotly. However, developers must
# respect rate limits, which restrict how many requests can be made in a timeframe.
# a) Explain what remaining and reset mean when monitoring an API’s rate limit.
# b) Write a code snippet using plotly.express to create a basic bar chart where the x-axis represents
# repo_names and the y-axis represents stars.
# c) How do you add a custom title and axis labels to a Plotly chart? Provide an example.
# d) Describe how you would handle a situation where you hit the API’s rate limit while trying to
# retrieve data.
# '''

# # a - meaning of remaining and reset in API rate limits
# '''
# when using an API, rate limits control how many request can be made witin a certain period
# remaining       The number of API requests you still have available before reaching the limit
# reset           The time when the rate limit will reset and you can make requests again
# '''

# # b - plotly express bar chart example
# import plotly.express as px
# # sample data
# repo_names = ["Repo A", "Repo B", "Repo C"]
# stars = [5000, 3000, 4500]

# # create bar chart
# fig = px.bar(
#     x = repo_names,
#     y = stars
# )
# # display chart
# fig.show()

# # c - adding custom titles and axis lables
# import plotly.express as px
# # sample data
# repo_names = ["Repo A", "Repo B", "Repo C"]
# stars = [5000, 3000, 4500]

# # create chart with custom titles
# fig = px.bar(
#     x = repo_names,
#     y = stars,
#     title = "Top GitHub Python Repositories",
#     labels = {
#         "x": "Repository Names",
#         "y": "Number of Stars"
#     }
# )
# # display chart
# fig.show()


# # d - handling API rate limits
# '''
# If I hit the API rate limit while retrieving data, I would:
# 1. Check the API response headers for:
#     - remaining
#     - reset
# 2. Pause requests until the reset time using functions such as time.sleep().
# 3. Reduce the number of requests by:
#     - Caching data
#     - Requesting only necessary information
#     - Increasing the time between requests
# 4. Use authentication tokens if supported, because authenticated users often receive higher rate limits.
# 5. Display an error message to inform the user that the limit has been reached and the program will retry later.
# '''
# import time
# # wait before retrying
# time.sleep(60)


