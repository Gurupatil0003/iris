import requests
# Change the value of experience that you want to test
url = 'http://127.0.0.1:5000/api'
feature = [[7,5,4.7, 5]]
labels ={
  0: "setosa",
  1: "versicolor",
  2: "virginica"
}

r = requests.post(url,json={'feature': feature})
print(labels[r.json()])