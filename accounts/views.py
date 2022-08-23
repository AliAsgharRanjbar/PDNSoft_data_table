from django.shortcuts import render

# Create your views here.


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth























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




s = 0
fa = 0
r = 0
war = 0
wai = 0

status_list = []








with open("C:/Users/Ali/Desktop/pooyesh/pdn/statics/sample.json", 'r') as f:
    data = json.loads(f.read())

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
styled_suc = status_df_success.style.hide(axis="index").set_table_styles(styles_success)

result_success = styled_suc.render()





status_data_failure = dict(Failure=fa)
status_df_failure = pd.DataFrame(status_data_failure, index=[0])
styled_fail = status_df_failure.style.hide(axis="index").set_table_styles(styles_failure)
result_fail = styled_fail.render()



status_data_running = dict(Running=r)
status_df_running = pd.DataFrame(status_data_running, index=[0])
styled_run = status_df_running.style.hide(axis="index").set_table_styles(styles_running)
result_run = styled_run.render()



status_data_warning = dict(Warning=war)
status_df_warning = pd.DataFrame(status_data_warning, index=[0])
styled_warn = status_df_warning.style.hide(axis="index").set_table_styles(styles_warning)
result_warn = styled_warn.render()



status_data_waiting = dict(Waiting=wai)
status_df_waiting = pd.DataFrame(status_data_waiting, index=[0])
styled_wait = status_df_waiting.style.hide(axis="index").set_table_styles(styles_waiting)
result_wait = styled_wait.render()





















def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password,
                                                email=email, first_name=first_name, last_name=last_name)
                user.save()

                return redirect('login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)


    else:
        return render(request, 'registration.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')



    else:
        return render(request, 'login.html')


def home(request):
    styled = df.sort_values("Start", ascending=False).style.hide_index(). \
        set_table_styles(styles).applymap(background_color_changer). \
        set_caption("Most recent jobs status")

    '''styled = df.sort_values("Start", ascending=False).style.hide_index().\
        set_table_styles(styles).applymap(background_color_changer).\
        set_caption("Most recent jobs status")'''

    result = styled.render()
    # result = styled.to_html("C:/Users/Ali/Desktop/pooyesh/pdn/templates/RES.html")
    with open("C:/Users/Ali/Desktop/pooyesh/data_table/templates/RES.html", "w") as f:
        f.write("""<head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                    </head>
                    <style>
                    table{
                    float:left;
                    margin-left: 56px;
                    }
                    </style>""")

        f.close()

    with open("C:/Users/Ali/Desktop/pooyesh/data_table/templates/RES.html", "a") as f:
        # f.write("{% endblock %}")

        f.write(f"{result_success}")
        f.write(f"{result_fail}")
        f.write(f"{result_run}")
        f.write(f"{result_warn}")
        f.write(f"{result_wait}")
        f.write(f"{result}")
        f.close()
    return render(request, "RES.html")


def logout_user(request):
    auth.logout(request)
    return redirect('login_user')