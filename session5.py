# accessing values in a dictionary
alien_0 = {"color": "green",
           "points": 5
           }
print(alien_0["color"])
print(alien_0["points"])


# adding new key-value pairs
alien_1 = {}
alien_1["x_position"] = 0
alien_1["y_position"] = 25
print(alien_1)


# modifying values
alien_2 = {"color": "green"}
print(f"The alien is {alien_2["color"]}")
alien_2["color"] = "yellow"
print(f"The alien is now {alien_2["color"]}")


# modifying values
alien_3 = {"x_position": 0,
           "y_position": 25,
           "speed": "medium"
           }
print(f"Original position: {alien_3["x_position"]}")

if alien_3["speed"] == "slow":
    x_increment = 1
elif alien_3["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
print(alien_3)

alien_3["x_position"] = alien_3["x_position"] + x_increment
print(f"New position: {alien_3["x_position"]}")


# removing key-value pairs
alien_4 = {"color": "green",
           "points": 5
           }
print(alien_4["points"])

del alien_4["points"]
print(alien_4)


# accessing and using the dictionary
favorite_languages = {"jen": "python",
                      "sarah": "c",
                      "edward": "rust",
                      "phil": "python"
                      }
language = favorite_languages["sarah"].title() # title() to make it capital letter
print(f"Sarah's favorite language is {language}")


# using get()
alien_5 = {"color": "green",
           "speed": "slow"
           }
point_value = alien_5.get("point", "No point value assigned")
print(point_value)


# lopping through a dictionary use sorted()
favorite_languages = {"jen": "python",
                      "sarah": "c",
                      "edward": "rust",
                      "phil": "python"
                      }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")
    

# lopping through a dictionary use specific values
favorite_languages = {"jen": "python",
                      "sarah": "c",
                      "edward": "rust",
                      "phil": "python"
                      }
print("The following languages have been mentioned")
for language in favorite_languages.values():
    print(language)
    

# lopping through a dictionary use unique values
favorite_languages = {"jen": "python",
                      "sarah": "c",
                      "edward": "rust",
                      "phil": "python"
                      }
print("The following languages have been mentioned")
for language in set(favorite_languages.values()):
    print(language.title())
    
    
# lopping through a dictionary use both keys and values
favorite_languages = {"jen": "python",
                      "sarah": "c",
                      "phil": "java"
                      }
for name, language in favorite_languages.items():
    print(f"{name} knows {language} language")
    
    
# nesting, nest dictionaries inside a list
alien_0 = {"color": "green",
           "points": 5
           }
alien_1 = {"color": "yellow",
           "points": 10
           }
alien_2 = {"color": "red",
           "points": 15
           }
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    

# nesting, generate a list dynamically
aliens = []
for alien_number in range(30):
    new_alien = {"color": "green",
                 "points": 5,
                 "speed": "slow"
                 }
    aliens.append(new_alien)
    
for alien in aliens[:5]:
    print(alien)
    
print(f"Total number of aliens: {len(aliens)}")


# nesting, for loop and an if statement
aliens = []
for alien_number in range(30):
    new_alien = {"color": "green",
                 "points": 5,
                 "speed": "slow"
                 }
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] == "yellow"
        alien["speed"] == "medium"
        alien["points"] == 10
        
for alien in alien[:5]:
    print(alien)
    print("...")
    
    
# nesting, a list in a dictionary
pizza = {"crust": "thick",
         "toppings": ["mushrooms", "extra cheese"]
         }
print(f"You orderes a {pizza["crust"]} crust pizza with the following toppings")
for topping in pizza["toppings"]:
    print(f"\t{topping}")
    
    
# nesting, looping through the dictionary
favorite_language = {"jen": ["python", "rush"],
                     "sarah": ["c"],
                     "edward": ["rust", "go"],
                     "phil": ["python", "haskell"]
                     }

for name, languages in favorite_language.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
        
        
# nesting, a dictionary in a dictionary
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton"
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris"
    },
}

for username, user_info in users.items():
    print(f"\n Username: {username}")
    full_name = f"{user_info["first"]}{user_info["last"]}"
    location = user_info["location"]
    print(f"\t Full name: {full_name.title()}")
    print(f"\t Location: {location.title()}")