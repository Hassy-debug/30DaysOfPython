import pandas as pd

df = pd.read_csv('hacker_news.csv')     #reads the file
print(df.head())                         

print(df.head(5))                        
print(df.tail(5))                        

titles = df['title']                     
print(type(titles))                      
print(titles)

print(df.shape)                          

python_titles = df[df['title'].str.contains('python|Python', na=False)]
print(len(python_titles))                # number of titles with python
print(python_titles['title'])

js_titles = df[df['title'].str.contains('JavaScript', na=False)]
print(len(js_titles))                    
print(js_titles['title'])

print(df.describe())                     
print(df.info())
print(df['author'].value_counts().head(10))   # the 10 most activ authors

data = {
    'Name': ['Asabeneh', 'David', 'John'],
    'Country': ['Finland', 'UK', 'Sweden'],
    'City': ['Helsinki', 'London', 'Stockholm'],
    'Age': [250, 40, 35],
}

people = pd.DataFrame(data)
print(people)
print(people[people['Age'] < 120])       # filtering the rows by condition