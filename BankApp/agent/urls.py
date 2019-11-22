from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import add_agent,all_agents,agent_details,update_agent

urlpatterns = [
    path("add/",add_agent,name= "add_agent"),
    path("all/",all_agents,name="all_agents"),
    path("view/<int:pk>/", agent_details, name="agent_details"),
    path("update/<int:pk>/", update_agent,name="update_agent"),
]
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)