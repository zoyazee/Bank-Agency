from django.shortcuts import render
from .forms import AgentForm
from .models import Agent

# Create your views here.
def add_agent(request):
    if request.method == "POST":
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AgentForm()

    return render(request,"add_agent.html",{"form":form})

def all_agents(request):
    agents = Agent.objects.all()
    return render(request,"all_agents.html",{"agents":agents})

def agent_details(request,pk):
    agent = Agent.objects.get(pk=pk)
    return render(request,"agent_details.html",{"agent":agent})

def update_agent(request,pk):
    agent = Agent.objects.get(pk=pk)
    if request.method=="POST":
        form = AgentForm(request.POST,instance=agent)
        if form.is_valid():
            form.save()
        return redirect("all_agents")
        
    else:
        form=AgentForm(instance=agent)
    return render(request,"update_agent.html",{"form":form})
