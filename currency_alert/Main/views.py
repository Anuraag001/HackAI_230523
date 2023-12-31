from .models import Customer,Alert,User_Agent
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from .utils import send_mail_
from uagents import Agent, Context,Bureau
from django.shortcuts import get_object_or_404, redirect
import time
import os
import fnmatch
import requests
import asyncio
from threading import Thread
from django.contrib.auth.views import PasswordResetConfirmView
from all_agent import *
from django.conf import settings
from django.http import JsonResponse
#from django.auth.models import User
# Create your views here.
currencies=['SGD', 'MYR', 'EUR', 'USD', 'AUD', 'JPY', 'CNH', 'HKD', 'CAD', 'INR', 'DKK', 'GBP', 'RUB', 'NZD', 'MXN', 'IDR', 'TWD', 'THB', 'VND']
boolean=True
first_string=f'''from uagents import Agent, Context,Bureau
import requests
bureau=Bureau()
from Main.utils import *
from django.conf import settings
'''
def remove():
    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

# Navigate to the parent directory
    parent_directory = os.path.join(script_directory, '..')

# Pattern to match filenames (e.g., files starting with "agent")
    pattern = 'agent*'

# Get a list of files matching the pattern in the parent directory
    matching_files = fnmatch.filter(os.listdir(parent_directory), pattern)

# Iterate through the matching files and delete them
    for file_name in matching_files:
        file_path = os.path.join(parent_directory, file_name)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {str(e)}")
    
def front(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.get(email=email)
        if check_password(password, user.password):
            remove()
            with open("all_agent.py", "w") as file:
                file.write(first_string)
            file.close()
            all_agents=User_Agent.objects.filter(user=user)
            for agent in all_agents:
                check(agent,email)
        
            print("user logged in")
            boolean=True
            return redirect('currency',user_id=user.id)
    return render(request,"temp.html")

def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        repeat_password=request.POST.get('repeat_password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number=request.POST.get('phone')
        user=User.objects.create_user(email=email,password=password,first_name=first_name,last_name=last_name,username=email)
        customer=Customer(email=email,password=password,first_name=first_name,last_name=last_name,phone_number=phone_number)
        customer.save()
        user.save()
        print("user created")
        remove()
        with open("all_agent.py", "w") as file:
                file.write(first_string)
        file.close()
        boolean=True
        return redirect('currency',user_id=user.id)
    return render(request,"signup.html")


def currency(request, user_id):
    return render(request, "currency.html", {'user_id': user_id, 'currencies': currencies})

def send_Mail(email):
    send_mail_(email)
    return render(request,"temp.html")

def convert(request,user_id):
    url = "https://currency-exchange.p.rapidapi.com/listquotes"

    headers = {
	'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers)

    print(response.json())
    return render(request,"currency.html",{'user_id':user_id})

def alert(request):
    return render(request,"alert.html",{"currencies":currencies})


async def do():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)  # Simulate some asynchronous work

async def do2():
    for i in range(10):
        print(i*10)
        await asyncio.sleep(2)

async def main_async(loop):
    f1 = loop.create_task(do()) 
    f2 = loop.create_task(do2()) 
    await asyncio.wait([f1, f2]) 
    loop.close()

# Your Django view
def create_alert(request):
    if request.method == 'POST':
        base_currency = request.POST.get('base_currency')
        min_amount = request.POST.get('min_amount')
        max_amount = request.POST.get('max_amount')
        to_currency = request.POST.get('to_currency')
        
        print(min_amount)
        print(max_amount)
        print(base_currency)
        print(to_currency)
        
        alert = Alert(base_currency=base_currency, min_amount=min_amount, max_amount=max_amount, to_currency=to_currency)
        alert.save()
        return redirect('screen')

    return render(request, 'create_alert.html')

def remove_agent(request, agent_id):
    try:
        agent = User_Agent.objects.get(pk=agent_id)
        agent.delete()
        return JsonResponse({'success': True})
    except User_Agent.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Agent does not exist'}, status=404)

def screen(request):
    return render(request, 'success.html')

def add_to_bureau(name):

    new_agent = Agent(name=name, seed=f"{name} recovery phrase")
    @new_agent.on_interval(period=2.0)
    async def say_hello(ctx: Context):
        ctx.logger.info(f'hello, my name is {ctx.name}')

    def run_agent():
        new_agent.run()

    my_thread = Thread(target=run_agent)
    my_thread.start()
    bureau.add(new_agent)
    return 

def check(agent,email):
    
    my_string = f'''
{agent.name} = Agent(name="{agent.name}", seed="{agent.name} recovery phrase")

@{agent.name}.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {{"from": "{agent.base_currency}", "to": "{agent.foreign_currency}", "q": "1.0"}}

    headers = {{
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }}

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", {agent.max_value})
    ctx.storage.set("min_value", {agent.min_value})
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\\033[91mNot in range\\033[0m')
        if not boolean:
            agent_mail("{email}","{f'Your agent {agent.name} has found out that the value of {agent.base_currency} has is not in between {agent.min_value}{agent.foreign_currency} and {agent.max_value}{agent.foreign_currency}'}")
            ctx.logger.info(f'\\033[93mMail sent out of range\\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\\033[94mIn range\\033[0m')

def run_{agent.name}():
    {agent.name}.run()
bureau.add({agent.name})
'''
    print(my_string)
    with open("all_agent.py", "a") as file:
        file.write(my_string)
    file.close()
    return

def run_bureau():
    bureau.run()

my_thread = Thread(target=run_bureau)

def threshold(request,user_id):
    user=User.objects.get(id=user_id)
    if request.method == 'POST':
        name=request.POST.get('name')
        base_currency = request.POST.get('base_currency')
        min_amount = request.POST.get('min_value')
        max_amount = request.POST.get('max_value')
        to_currency = request.POST.get('to_currency')

        agent=User_Agent.objects.create(user=user,name=name,base_currency=base_currency,min_value=min_amount,max_value=max_amount,foreign_currency=to_currency)
        agent.save()
        email=User.objects.get(id=user_id)
        #my_thread.start()
        check(agent,email)
        #add_to_bureau(name)
        #add_to_bureau(name)
    Boolean=boolean
    all_agents=User_Agent.objects.filter(user=user)
    return render(request, 'threshold.html',{'user_id': user_id, 'currencies': currencies,'all_agents':all_agents,'boolean':Boolean})

def run(request,user_id):
    if request.method == 'POST':
        my_thread.start()
        print(bureau)
    boolean=False
    user=User.objects.get(id=user_id)
    all_agents=User_Agent.objects.filter(user=user)
    return render(request, 'threshold.html',{'user_id': user_id, 'currencies': currencies,'all_agents':all_agents,'boolean':boolean})

def forgot_password(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            token = str(uuid.uuid4())
            send_mail_(email , token)
    return render(request,'forgot_password.html')

def password_reset_email(request):
    render(request,"password_reset_email.html")

def password_reset_confirm(request):
    return render(request, "password_reset_confirm.html")


def nice(request):
    return render(request, "nice.html")

def nice1(request):
    return render(request, "nice1.html")
