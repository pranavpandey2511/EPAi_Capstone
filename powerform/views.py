""" To generate views for our web app
"""

from django.http import HttpResponse
from friends.models import Friend
from django.template.loader import render_to_string, get_template

# def friends_view(request):
#     """ Generate the friends page
#     """
#     return HttpResponse(f"<title> Pranav Pandey </title> \n <h1>Friends</h1>")
#     # return render(request, 'powerform/friends.html')
def home_view(request):
    """ Generate the home page
    """

    all_friends = Friend.objects.all()
    context = {
        "title": 'Pranav Pandey',
        "all_friends": all_friends,
    }
    print("all_friends:", all_friends)
    HTML_STRING = render_to_string("home_view.html", context=context)
    return HttpResponse(HTML_STRING)
    # return render(request, 'powerform/home.html')

def update_view(request):
    """ Update the friends information.
    """
    if request.method == 'GET':
        # Get the data from the POST request
        data = request.POST
        # Get the friend object
        # friend = Friend.objects.get(pk=data['friend_id'])
        # Update the friend
        # friend.name = data['name']
        # if data['age']:
        #     friend.age = data['age']
        # friend.save()
        # # Return the updated friend
        # return HttpResponse(friend)
        return HttpResponse("<h1>UPDATE</h1>")
    else:
        # Return the friend
        pass
        # return HttpResponse(Friend.objects.all())