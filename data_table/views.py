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

blank = pd.DataFrame()


def table(request):

    styled = df.style.set_table_styles(styles)
    result = styled.render()
    #result = styled.to_html("C:/Users/Ali/Desktop/pooyesh/pdn/templates/RES.html")
    with open("C:/Users/Ali/Desktop/pooyesh/data_table/templates/RES.html", "w") as f:
        f.write('''{% extends "base.html" %}
        {% load static %}
        {% block page_content %}
                                ''')
        f.close()

    with open("C:/Users/Ali/Desktop/pooyesh/data_table/templates/RES.html", "a") as f:
        f.write(f"{result}")
        f.write("{% endblock %}")
        f.close()

    return render(request, "RES.html", {})


def aboutme(request):
    return render(request, "test.html", {})