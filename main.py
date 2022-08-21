import json
import requests
import pandas as pd
import random

'''
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}



#print(type(data))

with open("test_file.json", "w") as file:
    json.dump(data, file)


print(json.dumps(data))
#print(json.dumps(data, indent=10))
print(json.dumps(data, separators=(",",":")))


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print(todos[:3])

print(type(todos))


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


names = []
ages = []

for child in myfamily:
    print(myfamily[child]["name"], end=' ')
    names.append(myfamily[child]["name"])

print('\n')

for child in myfamily:
    print(myfamily[child]["year"], end=' ')
    ages.append(myfamily[child]["year"])
print('\n')

print(names, ages, sep='\n')'''

###########################################################################################################
Job_name = []
Status = []
Job_ID = []
Client = []
Level = []
Start = []
End = []
Bytes = []

with open("C:/Users/Ali/Desktop/pooyesh/data_table/statics/sample.json", 'r') as f:
    data = json.loads(f.read())

# data = list(data)
# print(data)
df = pd.DataFrame(data)
# print(df)
# multiple_lvl_data = pd.json_normalize(data, record_path= ["PDNSOFT"] , record_prefix='')

# multiple_lvl_data.to_html('mld.html', index=False)

for jn in data["PDNSOFT"]:
    # print(data["PDNSOFT"][jn]["Jobe name"])  # there is a typo in json file
    Job_name.append(data["PDNSOFT"][jn]["Jobe name"])
    # print(data["PDNSOFT"][jn]["Status"])
    Status.append(data["PDNSOFT"][jn]["Status"])
    # print(data["PDNSOFT"][jn]["Jobe ID"])
    Job_ID.append(data["PDNSOFT"][jn]["Jobe ID"])  # there is a typo in json file
    # print(data["PDNSOFT"][jn]["Client"])
    Client.append(data["PDNSOFT"][jn]["Client"])
    # print(data["PDNSOFT"][jn]["Level"])
    Level.append(data["PDNSOFT"][jn]["Level"])
    # print(data["PDNSOFT"][jn]["Start"])
    Start.append(data["PDNSOFT"][jn]["Start"])
    # print(data["PDNSOFT"][jn]["End"])
    End.append(data["PDNSOFT"][jn]["End"])
    # print(data["PDNSOFT"][jn]["Bytes"])
    Bytes.append(data["PDNSOFT"][jn]["Bytes"])

data = {'Name': ['Karan', 'Rohit', 'Sahil', 'Aryan'], 'Age': [23, 22, 21, 24]}

df = pd.DataFrame(data)

# print(df)

# print(Job_name)

data = {'Job name': Job_name, 'Status': Status, 'Job ID': Job_ID, 'Client': Client, 'Level': Level, 'Start': Start,
        'End': End, 'Bytes': Bytes}
df = pd.DataFrame(data)
df.to_html('mld.html')

# print(df)

ran_list = ['Job name', 'Status', 'Job ID', 'Client', 'Level', 'Start', 'End', 'Bytes']

choice = random.choice(ran_list)

# df.sort_values(choice).to_html(f'randomly_sorted_by_{choice}.html')


# df.style.set_properties(**{'border': '1.3px solid green',
# 'color': 'magenta'}).to_html('sttttttttttttt.html')


'''

# Set CSS properties for th elements in dataframe
th_props = [
  ('font-size', '20px'),
  ('font-family', 'Comic Sans MS'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', 'white'),
  ('background-color', '#347cb3'),
  ]

# Set CSS properties for td elements in dataframe
td_props = [
  ('font-size', '19px'),
  ('font-family', 'Comic Sans MS'),
  ('text-align', 'center'),
  ("padding", "12px 20px"),


  ]

# Set table styles
styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]'''

# df.set_index("Job name").style.set_table_styles(styles).to_html('FINAL.html')
# df.style.set_table_styles(styles).to_html('FINAL.html', index_names=False, index=False)
# df.to_html('FINAL.html', index_names=False, index=False)


styles = [
    dict(selector="tr:hover",
         props=[("background", "#f4f4f4")]),

    dict(selector="th", props=[("color", "#fff"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#347cb3"),
                               # ("text-transform", "uppercase"),
                               ("font-size", "18px"),
                               ('font-family', 'Courier New'),
                               ]),
    dict(selector="td", props=[("color", "#999"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "20px"),
                               ]),
    dict(selector="table", props=[
        ("font-family", 'Arial'),
        ("margin", "25px auto"),
        ("border-collapse", "collapse"),
        ("border", "1px solid #eee"),
        ("border-bottom", "2px solid #00cccc"),
    ]),
    dict(selector="caption", props=[("caption-side", "bottom")])
]

# df.sort_values(choice).style.set_table_styles(styles).to_html(f'FINAL_{choice}.html')

# df.set_index('Job name').sort_values(choice).style.set_table_styles(styles).to_html(f'FINAL_{choice}.html')

