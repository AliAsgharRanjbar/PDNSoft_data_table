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

s = 0
fa = 0
r = 0
war = 0
wai = 0

status_list = []





with open("C:/Users/Ali/Desktop/pooyesh/pdn/statics/sample.json", 'r') as f:
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
    status_list.append(data["PDNSOFT"][jn]["Status"])
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




for status in status_list:
    if status == "Success":
        s += 1
    elif status == "Failure":
        fa += 1
    elif status == "Running":
        r += 1
    elif status == "Warning":
        war += 1
    else:
        wai += 1



print(s, fa, r, war, wai)

# status_data = {'Success': list(status_list[0]), 'Failure': list(status_list[1]), 'Running': list(status_list[2]), 'Warning': list(status_list[3]), 'Waiting': list(status_list[4])}
# status_df = pd.DataFrame(status_data)
# print(status_df)







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

    dict(selector="th", props=[("color", "white"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#347cb3"),
                               # ("text-transform", "uppercase"),
                               ("font-size", "18px"),
                               ('font-family', 'Courier New'),
                               ]),
    dict(selector="td", props=[("color", "#000000"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "20px"),
                               ("text-align", "center"),
                               ]),
    dict(selector="table", props=[
        ("font-family", 'Arial'),
        ("margin", "25px auto"),
        ("border-collapse", "collapse"),
        ("border", "1px solid #eee"),
        ("border-bottom", "2px solid #00cccc"),
    ]),
    dict(selector="caption", props=[("caption-side", "top"),
                                    ("color", "#000000"),
                                    ("border", "1px solid #eee"),
                                    ("padding", "12px 35px"),
                                    ("border-collapse", "collapse"),
                                    ("font-size", "20px"),
                                    ('font-family', 'Courier New'),
                                    ("font-weight", "bold"),
                                    ])

]

# df.sort_values(choice).style.set_table_styles(styles).to_html(f'FINAL_{choice}.html')
# df.style.hide(axis="index").set_table_styles(styles).applymap.to_html("NOINDEX.html")

# df.set_index('Job name').sort_values(choice).style.set_table_styles(styles).to_html(f'FINAL_{choice}.html')








'''df = pd.DataFrame({
    "name":         ["alan","beth","charlie","david", "edward"],
    "age" :         [34,    12,     43,      '32',      77],
    "num_children": [1,     0,      '2',       1,       6],
    "num_pets":     [1,     0,      1,       2,       0],
    "bank_balance": [100.0, 10.0,   -10.0,   30.0,    30.0]})'''

def background_color_changer(cell_value):

    highlight_success = 'background-color: #5ab65f'
    highlight_failure = 'background-color: #d6514c;'
    highlight_running = 'background-color: #5dbfdf;'
    highlight_warning = 'background-color: #f7ab4f;'
    highlight_waiting = 'background-color: #75757d;'

    default = ''

    if not cell_value.isnumeric():
        try:
            if cell_value == "Success":
                return highlight_success
            elif cell_value == "Failure":
                return highlight_failure
            elif cell_value == "Running":
                return highlight_running
            elif cell_value == "Warning":
                return highlight_warning
            elif cell_value == "Waiting":
                return highlight_waiting
        except TypeError:
            return default






'''def status_cells_text_color_changer(cell_value):

    change_color = "color: white;"

    default = ''

    if not cell_value.isnumeric():
        try:
            if cell_value == "Success":
                return change_color
            elif cell_value == "Failure":
                return change_color
            elif cell_value == "Running":
                return change_color
            elif cell_value == "Warning":
                return change_color
            elif cell_value == "Waiting":
                return change_color
        except TypeError:
            return default'''











# df.style.set_table_styles([{'selector': 'th', 'props': [('font-size', '5pt')]}]).set_properties(**{'font-size': '10pt'})
# df.sort_values("Job name")
df.sort_values("Start", ascending=False).style.hide(axis="index").set_table_styles(styles).applymap(background_color_changer).set_caption("Most recent job status").to_html("NOINDEX.html")

cell = 'alan'
cell1 = '123'

print(cell.isnumeric())
print(cell1.isnumeric())

print("CELL 1: \n")
print(eval(f"{cell1} % 2"))
print("CELL: \n")
#print(eval(f"{cell} % 2"))

print(s)









styles_success = [
    dict(selector="tr:hover",
         props=[("background", "#f4f4f4")]),

    dict(selector="th", props=[("color", "white"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#5ab65f"),
                               # ("text-transform", "uppercase"),
                               ("font-size", "18px"),
                               ('font-family', 'Courier New'),
                               ]),
    dict(selector="td", props=[("color", "#000000"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "20px"),
                               ("text-align", "center"),
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






styles_failure = [
    dict(selector="tr:hover",
         props=[("background", "#f4f4f4")]),

    dict(selector="th", props=[("color", "white"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#d6514c"),
                               # ("text-transform", "uppercase"),
                               ("font-size", "18px"),
                               ('font-family', 'Courier New'),
                               ]),
    dict(selector="td", props=[("color", "#000000"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "20px"),
                               ("text-align", "center"),
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









styles_running = [
    dict(selector="tr:hover",
         props=[("background", "#f4f4f4")]),

    dict(selector="th", props=[("color", "white"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#5dbfdf"),
                               # ("text-transform", "uppercase"),
                               ("font-size", "18px"),
                               ('font-family', 'Courier New'),
                               ]),
    dict(selector="td", props=[("color", "#000000"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "20px"),
                               ("text-align", "center"),
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









styles_warning = [
    dict(selector="tr:hover",
         props=[("background", "#f4f4f4")]),

    dict(selector="th", props=[("color", "white"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#f7ab4f"),
                               # ("text-transform", "uppercase"),
                               ("font-size", "18px"),
                               ('font-family', 'Courier New'),
                               ]),
    dict(selector="td", props=[("color", "#000000"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "20px"),
                               ("text-align", "center"),
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







styles_waiting = [
    dict(selector="tr:hover",
         props=[("background", "#f4f4f4")]),

    dict(selector="th", props=[("color", "white"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#75757d"),
                               # ("text-transform", "uppercase"),
                               ("font-size", "18px"),
                               ('font-family', 'Courier New'),
                               ]),
    dict(selector="td", props=[("color", "#000000"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "20px"),
                               ("text-align", "center"),
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




















status_data_success = dict(Success=s)
status_df_success = pd.DataFrame(status_data_success, index=[0])
status_df_success.style.hide(axis="index").set_table_styles(styles_success).to_html("STATUS_Success.html")





status_data_failure = dict(Failure=fa)
status_df_failure = pd.DataFrame(status_data_failure, index=[0])
status_df_failure.style.hide(axis="index").set_table_styles(styles_failure).to_html("STATUS_Failure.html")



status_data_running = dict(Running=r)
status_df_running = pd.DataFrame(status_data_running, index=[0])
status_df_running.style.hide(axis="index").set_table_styles(styles_running).to_html("STATUS_Running.html")



status_data_warning = dict(Warning=war)
status_df_warning = pd.DataFrame(status_data_warning, index=[0])
status_df_warning.style.hide(axis="index").set_table_styles(styles_warning).to_html("STATUS_Warning.html")



status_data_waiting = dict(Waiting=wai)
status_df_waiting = pd.DataFrame(status_data_waiting, index=[0])
status_df_waiting.style.hide(axis="index").set_table_styles(styles_waiting).to_html("STATUS_Waiting.html")





# status_df.style.hide(axis="index").set_table_styles([{'selector': 'th', 'props':\
# [('font-size', '5pt')]}]).set_properties(**{'font-size': '10pt'}).to_html("NOINDEX.html")
