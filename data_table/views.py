from django.shortcuts import render, HttpResponse

# Create your views here.

import pandas as pd
import json
from time import sleep

Job_name = []
Status = []
Job_ID = []
Client = []
Level = []
Start = []
End = []
Bytes = []


with open("C:/Users/Ali/Desktop/pooyesh/pdn/statics/sample.json", 'r') as f:
    data = json.loads(f.read())

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
# 'tableview/static/csv/20_Startups.csv' is the django
# directory where csv file exist.
# Manipulate DataFrame using to_html() function

data = {
    'Job name': Job_name,
    'Status': Status,
    'Job ID': Job_ID,
    'Client': Client,
    'Level': Level,
    'Start': Start,
    'End': End,
    'Bytes': Bytes,
}
df = pd.DataFrame(data)
# df.to_html('mld.html')

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
        #("width", '100%'),

    ]),
    dict(selector="caption", props=[("caption-side", "top"),
                                    ("text-align", "center"),
                                    ("color", "#000000"),
                                    ("border", "1px solid #eee"),
                                    ("padding", "12px 35px"),
                                    ("border-collapse", "collapse"),
                                    ("font-size", "20px"),
                                    ('font-family', 'Courier New'),
                                    ("font-weight", "bold"),
                                    ])

]


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













blank = pd.DataFrame()


def table(request):

    styled = df.sort_values("Start", ascending=False).style.hide(axis="index").\
        set_table_styles(styles).applymap(background_color_changer).\
        set_caption("Most recent job status").to_html("C:/Users/Ali/Desktop/pooyesh/data_table/templates/RES.html")

    # result = styled.render()
    # result = styled.to_html("C:/Users/Ali/Desktop/pooyesh/pdn/templates/RES.html")
    '''with open("C:/Users/Ali/Desktop/pooyesh/data_table/templates/RES.html", "w") as f:
        f.write('{% extends "base.html" %\}{% load static %}{% block page_content %}')
        f.close()

    with open("C:/Users/Ali/Desktop/pooyesh/data_table/templates/RES.html", "a") as f:
        f.write(f"{result}")
        f.write("{% endblock %}")
        f.close()'''

    return render(request, "RES.html", {})


def aboutme(request):
    return render(request, "test.html", {})