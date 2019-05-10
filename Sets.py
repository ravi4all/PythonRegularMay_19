dataset = {
    "action" : ['hulk','superman','batman','thor','ironman','baahubali','kgf',
                'aquaman','I','kabali','kaabil'],
    "comedy" : ['zero'],
    "biopic" : ['ms dhoni','sultan'],
    "thriller" : ['kaabil','kgf','I']
    }

user_1 = {'hulk','superman','batman','thor','ironman','baahubali','kgf','zero',
          'sultan','kaabil'}
user_2 = {'hulk','aquaman','batman','avengers','ironman','baahubali','I','zero',
          'ms dhoni','kabali'}

simMovies = user_1.intersection(user_2)
print(simMovies)
union = user_1.union(user_2)
dist = len(simMovies) / len(union)
print("Similarity is",round(dist * 100,2))

action = 0
comedy = 0
biopic = 0
thriller = 0

for movie in simMovies:
    if movie in dataset["action"]:
        action += 1
    
