<h1><b>except4try</b></h1>
 A platform to get your queries solved. 
 except4try :: analogous to the except block in your program :: always there for you to handle the exceptions raised in your   try block.
 Post/Search the queries, get them answered, get the votes.

<h2>Features :</h2>

<b>Post/Search Questions</b>

<b>Answer/get answered</b>

<b>Vote Questions, Answers and comments and get your content voted too</b>

<b>Rest API support to : get all the available questions,get all the answers specific to a question, programatically post a question, get upvoters/downvoters list</b>



<b><h3>Live demo Link: <a href="http://except4try.pythonanywhere.com/">http://except4try.pythonanywhere.com/ </a></h3><b> 
<b>
<hr>


<b><h2>Tech Stack</h2></b>
1. Python<br>
2. Django<br>
3. Javascript/Jquery<br>
4. Elastic Search + Haystack<br>
5. Bootstrap 4<br>
6. Django Rest Framework<br>


<b><h2>Instructions for Execution:</h2></b>
1. Download and install elastic search in your system to get the search feature working. 
 Refer :<a href="https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-16-04">https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-16-04</a>
2. pip3 install -r requirements.txt<br>
3. ./manage.py collectstatic<br>
4. ./manage.py makemigrations<br>
5. ./manage.py migrate<br>
6. ./manage.py runserver<br>

<b><h2>Demo API requests :</h2></b>
<br>
1) Post a question :
<br>
<pre>
import requests

url="http://except4try.pythonanywhere.com/api/ask_question/"
data={'topic':'Template custom filters in Django','detail':'library not found error being displayed','tags_list':['Python','Django']}
r = requests.post(url,auth=('jesin', 'jesin'),data=data)
print(r.json())
</pre>
<br><br>

2) Get all the available questions :
<br>
<pre>

import requests

url="http://except4try.pythonanywhere.com/api/all_questions/"
r = requests.get(url)
print(r.json())

</pre>
<br><br>
3) Get all the answers corresponding to given question :
<br>
<pre>
import requests

url="http://except4try.pythonanywhere.com/api/answers/2"
r = requests.get(url)
print(r.json())
</pre>


<b><h2>Demo Login credentials :</h2></b>
<br>
username : jesin<br>
password : jesin
