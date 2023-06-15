import os
import openai
import panel as pn  # GUI

#from dotenv import load_dotenv, find_dotenv
#_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = ("<add api key here>")

def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

def get_completion_from_messages_sales(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)


system_message_1 = f"""All right. So today we're going to go \ 
through the steps required to set a device up for a TAP ModiDAR. \ 
Kind of the simplest way we go into a customer's network. \ 
And we're going to assume that you have the box IP. \ 
I can go through that if we need to. \ 
But we're going to go through the main steps of what you do. \ 
So the first thing is you make sure the device is updated \ 
and has its licenses. Once you've done, \ 
you go to the device tab here, you go to the \ 
licenses node, make sure the licenses are valid. \ 
Let's assume that you've registered the device correctly. \ 
If not, if the licenses aren't there, you retrieve \ 
license keys from server, you wait for the \ 
licenses to happen, and you move on with your life. \ 
The next thing is the software version that we're running. \ 
We make sure that we're running a decent code train. \ 
I'm running nearly the latest code, so I'm okay with \ 
where I'm at. But I could say potentially download \ 
and install that next version. After that, \ 
actually, one of the things you need to make \ 
sure is, and this is something I usually do in \ 
the initial setup, but I will cover it just \ 
to make sure, is that you need to make sure \ 
you have DNS and NTP configured. \ 
Because if you don't have those things configured, \ 
you go to device tab, setup mode, \ 
services sub tab, and you go through and set up DNS and NTP. \ 
That will connect into the update servers won't work without it. \ 
So once you've set those up, you go back here and you go \ 
to dynamic updates and the first thing that we want \ 
to make sure is our devices are getting updated very often. \ 
So I usually start with apps and threats because when \ 
you're doing a tap on the e-mail, that's the first thing \ 
and the only thing that shows up. \ 
You click on the schedule, you make sure the schedule is set. \ 
Right now I do it for every 30 minutes, \ 
it's seven minutes past the half hour. \ 
The download action is download and install. \ 
And I set a threshold anywhere, \ 
you can do it for an eval, no big deal, \ 
but typically for customers I tell them 12 hours."""


system_message_2 = f"""Once you've done that, you will make \ 
sure you hit check now, grab the latest code, hit the download button. \ 
Once it's downloaded, hit the install button. \ 
Then you'll see once that process finishes, you will be on the latest and greatest. \ 
The next thing you do is antivirus will also show up \ 
there after you check now a second time. \ 
Go in, make sure the schedule is there. \ 
I do an hourly schedule. I do seven minutes past the hour. \ 
Again, that's actually overlapping, but it doesn't really matter \ 
in this case the action is download and install. \ 
I set a four to six hour threshold for my customers. \ 
Last one is wildfire typically. \ 
I usually just do real-time make sure that's done for both \ 
AV and wildfire just do the same process as you did for apps \ 
and threats and download and install each of them in succession. \ 
You can't do multiple downloads or multiple installs at one time. \ 
So just do them in serial. \ 
Once you've done that, you're going to the network tab. \ 
You're going to make sure you set up your interfaces. \ 
I'll just do ETH13, but typically you're going to use ETH11. \ 
You set up this interface by going into the interface. \ 
You click on it. This is under the network tab, \ 
interfaces node, Ethernet sub-tab. \ 
You make sure you set the interface type to tap. \ 
You go into security zones, there's typically none under the type tap, \ 
so you click new zone at the bottom here. \ 
Once you click new zone, give the zone a name. \ 
I call it tap, tap zone. \ 
You make sure if you're planning on using user identification \ 
that you enable user ID here, and really nothing else is necessary. \ 
So we're going to click OK. That zone is set. \ 
The advanced, just make sure your link state is set to up. \ 
It should already be there. \ 
But again, or auto or up is going to make \ 
sure you don't have a problem with connectivity. Hitting OK."""


system_message_3 = f""" Very simple piece here. \ 
We've got the interface set up. \ 
The next thing we do is we go into the policies tab. \ 
Under security policies, you're going to hit the add button. \ 
You're going to take the Add button, you're going to say, Tap. \ 
This is just going to be a single policy for an eval typically. \ 
If you want to separate certain things out, \ 
you can certainly do that in the subsequent policy. \ 
But I'm just going to set the source zone to Tap zone, \ 
the destination sub-tab here. I'm going to go Tap zone as well. \ 
Those are the only two things you really need. \ 
The application can be any. The service is going to be any, \ 
not application default because we want to catch all the traffic \ 
and the action is allow. \ 
The next thing we do is we set up security profiles in here. \ 
I will set up the antivirus security profiles now just so that we can see the process. \ 
Each one of these is going to be called alert- \ 
whatever the profile. So in this case, it's AV. \ 
The signature action, I'm going to set all of them to alert. \ 
This is a painful process that you have to go through \ 
and set all of these up if you're tabbing through. \ 
Not my ideal, but it is what it is. \ 
You can see that some of these have a different action. \ 
I'm just going to go through and again tab through this \ 
and set them all. This is where I would usually call out PM to say, \ 
"hey, we need a function that makes us better." \ 
You can see that sometimes when you tab through, \ 
it can error out a little bit, so the GUI gets a little weird. \ 
I'll go back and change that in a second. \ 
Vulnerability profile: same thing. We're going to create an alert, home. \ 
The next step here is to add a new rule. \ 
In the rule, we're going to say alert. Make sure the action is set to alert. \ 
Make sure the severity is all and hit okay. \ 
There's also an option here for inline cloud analysis. \ 
So you can set those, make sure they're at least set to alert. \ 
You're not going to be able to really do much with them anyway. \ 
You make sure you enable inline cloud analysis, however, to be able to get that to function. \ 
Hit okay. Your next profile is NSFlyware. \ 
You're going to go through and create a new one. \ 
Again, I'm going to call alert AS plus DNS because \ 
it's one of those things that's hidden in here that you don't normally see. \ 
I'm going to add a policy name called alert. \ 
Everything's there. The action is going to be set to alert. \ 
And then I'm going to go over to DNS policies. \ 
And I'm going to make sure that I either have alert or allow. \ 
And allow is one of the things that is not typically identified or called out here. \ 
But allow is the only place where allow means alert. \ 
DNS security is weird like that. \ 
So I'm going to just go through and make sure all of these are set, \ 
clicking through them. \ 
A lot of people have this set in a script or in a global config, \ 
but I want you to understand how to actually go through this. \ 
Then inline cloud analysis is the last tab. \ 
We're going to enable that. \ 
We're going to make sure all the actions are set to alert. \ 
We're going to hit okay. We're going to go to URL filtering. \ 
This one's actually much quicker because they have a pretty good \ 
function that needs to be in all of them. \ 
Third-URL. We're going to take site access, \ 
and we are going to click the little caret at the top. \ 
When you mouse over the header, you're going to say set all actions to alert. You're going to click off. """

system_message_4 = f"""All of your categories are now set to alert. \ 
Your URL filtering settings, I always set user agent refer exported for to be logged,\ 
just in case. We're not doing anything with credential detection. \ 
We're not doing anything with headers right now. \ 
Inline categorization, though, we are going to do. \ 
And you can say, there's exceptions. We're not going to add any right now. \ 
You just check those two boxes. And then validating, \ 
if you really want to check that inline categorization is on, \ 
real-time detection, we've already set it in our category list. Hit OK. \ 
File blocking is a very simple one. We're going to create one called alert-file. \ 
The reason I name it 'alert-file' is that A is the top of the list, \ 
so it shows up right at the top. \ 
Set one policy, add a rule that says alert any application, \ 
any file type, direction both, action alert, done. \ 
The only one that we don't really ever modify is wildfire \ 
because the default profile should does exactly what we want data filtering \ 
I'm not even going to turn on in the typical eval Log forwarding \ 
if you're doing some syslog or anything like that, \ 
you may need to set that up to cortex data lake or to syslog server \ 
That's not going to be covers a part of this hit. \ 
Okay, we're done. We've got our policy in place We are ready to go \ 
You hit commit you validate your changes, right? \ 
You can do change summary typically is the way I'll do this \ 
I'll look at all my things Great. Great. Great. \ 
There's the ones I expected to be in there. \ 
I'm actually going to go back I did remember that I have to change one object \ 
in anti virus and I'm going to go to alert AV and \ 
Remember some of these didn't get quite changed \ 
I'm going to go through and just change all those again. \ 
And you can see it's a little bit painful to click through all of them, \ 
but it's important to make sure you do this step so that you're not \ 
blocking anything if this ever gets converted to a real policy or real profile production wise. \ 
So sorry for the dead air, that's kind of what happens here. \ 
Once we've done this and finished we go through and we make sure we have wildfire ML. \ 
That's another thing I said I was going to go back and do. \ 
I'm going to say alert only to each of the possible settings and \ 
there are more than just you see on the page, so be sure to scroll down. \ 
Make sure they're all enabled. Once that's done, you hit OK. \ 
You'll see that the profile changes to alert only over here. \ 
Everything else set to alert. Now we go back, do our commit, validate, and hit commit. \ 
Now we go back, do our commit, validate, and hit commit."""


system_goal = f"""
You are a customer IT specialist responsible \
for helping customers set up hardware. \
Respond in a friendly and helpful tone, \
with very concise answers. \
Make sure to ask the user relevant follow up questions.
"""


system_goal_internal = f"""
You are helping a sales assistant / engineer responsible \
for helping clients set up firewalls. \
provide any information he needs about the client and where they are in the setup process.
"""

system_message_1_internal = f"""An individual is trying to set up his companies firewall.\ 
His name is Carl and he has worked at PetSmart for a few months.\ 
PetSmart has been a customer for the past 7 years and they just hired carl as a second network admin. \ 
Carl is struggling to deploy some of the firewalls they purchased. \ 
He has been stuck for about 30 minutes. \ 
he is going to need some help configuring some of their offsite branches.  \ 
they purchased 350 'PA-1400 Series Firewall Hardware' \ 
and he's currently using a windows 11 operating system.  \ 
He is located in Des Moins, Iowa. \ 
The last step he completed from the instructions was setting up the update scheduler. \ 
"""


user_message_1 = f"""
tell me the first steps to setting up a \
TAP ModiDAR. """

user_message_2 = f"""can you tell me how to set up the DNS and NTP?"""

user_message_3 = f"""sorry can you tell me where i go to set up the interface again?"""

messages_1 =  [  
{'role':'system',
 'content': system_goal},
{'role':'system',
 'content': system_message_1},   
{'role':'user',
 'content': user_message_1},  
{'role':'assistant',
 'content': f"""answer the users question as best you can"""},   
]

messages_2 =  [  
{'role':'system',
 'content': system_goal},
{'role':'system',
 'content': system_message_2},   
{'role':'user',
 'content': user_message_2},  
{'role':'assistant',
 'content': f"""answer the users question as best you can"""},   
]

messages_3 =  [  
{'role':'system',
 'content': system_goal},
{'role':'system',
 'content': system_message_2},   
{'role':'user',
 'content': user_message_3},  
{'role':'assistant',
 'content': f"""answer the users question as best you can"""},   
]

messages_4 =  [  
{'role':'system',
 'content': system_goal_internal},
{'role':'system',
 'content': system_message_1_internal},   
{'role':'assistant',
 'content': f"""alert jeff that the customer has an issue in one sentance anwers"""},   
]

'''
final_response_1 = get_completion_from_messages(messages_1)
final_response_2 = get_completion_from_messages(messages_2)
final_response_3 = get_completion_from_messages(messages_3)

print(user_message_1 + "\n")
print(final_response_1 + "\n")
print(user_message_2 + "\n")
print(final_response_2 + "\n")
print(user_message_3 + "\n")
print(final_response_3 + "\n")
'''



def internal_model():
    pn.extension()
    panels = [] # collect display 
    user_input = input("Do you have any questions for your assistant? ")
    if user_input == "":
        return
    messages =  [  
        {'role':'system', 'content': system_goal_internal},
        {'role':'system', 'content': system_message_1},
        {'role':'system', 'content': system_message_2},
        {'role':'user', 'content': user_input},    
        {'role':'assistant', 'content': f"""assist the users questions as best you can"""},   
    ]
    response = get_completion_from_messages(messages)
    print(user_input + "\n")
    print(response + "\n")

def external_model():
    pn.extension()
    panels = [] # collect display 
    user_input = input("Do you have any questions for your assistant? ")
    if user_input == "":
        return
    messages =  [
        {'role':'system', 'content': system_goal},  
        {'role':'system', 'content': system_message_1},
        {'role':'system', 'content': system_message_2},
        {'role':'system', 'content': system_message_3},
        {'role':'system', 'content': system_message_4},
        {'role':'user', 'content': user_input},    
        {'role':'assistant', 'content': f"""answer the users question as best you can"""},   
    ]
    response = get_completion_from_messages(messages)
    print(user_input + "\n")
    print(response + "\n")


user_model = input("internal or external mode? (type 'i' or 'e')")
if user_model == 'i':
    while True:
        internal_model()
if user_model == 'e':
    while True:
        internal_model()





