""" 
this code is just a simple example of how you could manage user registration
using their email, where they don't have to manually input their usernames. 
it only requires the user's email to generate a unique username using recursion

"""

from django.contrib.auth.models import User
def username_generator(email, username = "" , val = 0):
    email_split = email.split('@')[0]
    val = str(val)
    username = email_split + val
    username_stat = User.objects.filter(username = username).exists()
    
    if username_stat:
        val = int(val)
        val += 1
        val = str(val)
        username = email_split + val
        val = int(val)
        return username_generator(email = email, username = username, val = val)
    else:
        return username