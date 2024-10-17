from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json
import datetime


def print_to_log(text):
    with open('temp_log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{text}\n')


# note_template ----------------------------


def template(request):
    text = "This is a note from the template view function."
    context = {"note": text}

    return render(request, 'note_template.html', context)




# polaris (login and Register) -----------

def polaris(request):
    return render(request, 'polaris.html')


@csrf_exempt
def login(request):
    from app01.middleware.SQLConn import polaris_db

    if request.method == 'POST':

        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        with open('credentials.txt', 'a') as f:
            f.write(f'{username} {password}\n')

        credential = polaris_db(f"SELECT uid FROM users WHERE user_name='{username}' AND password='{password}';")
        print_to_log(credential)
        if credential:
            uid = credential[0][0]

            print_to_log(f'User {username} logged in. UID: {uid}')
            print_to_log(uid)

            # response = HttpResponseRedirect(f'http://127.0.0.1:8000/app01/polaris/template/{uid}')
            # response.set_cookie('uid', uid, max_age=3600)
            # return response
            return JsonResponse({"uid": uid})

        else:
            return JsonResponse({"message": 'Unmatched username or password!'})

    else:
        return JsonResponse({"message": 'Login Failed'})


# dashboard -------------------------------

def dashboard(request, uid):

    return render(request, 'dashboard.html', {"uid": uid})



# write_note -----------------------------

def write_note(request, uid):
    from app01.middleware.SQLConn import polaris_db

    username = polaris_db(f"SELECT user_name FROM users WHERE uid='{uid}';")[0][0]

    context = {"username": username, "uid": uid, "sys_info": {"time": datetime.datetime.now()}, }
    return render(request, 'write_note.html', context)


# my_space ---------------------------------

def my_space(request, uid):
    from app01.middleware.SQLConn import polaris_db

    print_to_log("1")
    
    username = polaris_db(f"SELECT user_name FROM users WHERE uid='{uid}';")[0][0]

    res = polaris_db(f"SELECT title, content, dir_link FROM notes WHERE uid='{uid}';") 
    
    print_to_log(res)

    notes = []
    for each in res:
        title, abstract, content = each[0], str(each[1])[0:20] + "...", each[1]
        
        try:
# linux version
            # md_path = "app01/data" + each[2]
            # with open(md_path, 'r', encoding='utf-8') as md_file:
            #     md_content = md_file.read()

# windows version
# example: Polaris\app01\data\Anyuegogogo\axios请求拦截，token失效，多个请求报错导致多次显示弹框的问题.md
            md_path = "/home/ubuntu/Polaris/Polaris/app01/data" + each[2]
            with open(md_path, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()
        except FileNotFoundError:
            md_content = f".md not found {md_path}" + "\n" +content
        
        note = {"title": title, "abstract": abstract, "content": content, "md_content": md_content}
        notes.append(note)

    context = {"username": username, "uid": uid, "sys_info": {"time": datetime.datetime.now()}, "notes": notes,}
    return render(request, 'my_space.html', context)


# example --------------------------------

def example(request):

    context = {"sys_info": {"time": datetime.datetime.now()}}

    return render(request, 'example.html', context)


@csrf_exempt
def get_suggestion(request, text):
    from app01.middleware import baidu_api

    print_to_log("run")
    
    data = {
        "suggested_text": str(baidu_api.call_baidu_wenxin(text))
    }

    return JsonResponse(data)


@csrf_exempt
def process_json(request):
    if request.method == 'POST':
        try:
            received_data = json.loads(request.body)
            print("Received JSON Data:", received_data)
            return JsonResponse({"message": "Data received successfully"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data received"}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)