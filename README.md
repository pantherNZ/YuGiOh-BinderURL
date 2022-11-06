# YuGiOh-BinderURL
Basic Flask site for generating smaller/consistent urls specifically used by the [YuGiOh-Portfolio App](https://github.com/pantherNZ/YuGiOh-Portfolio) to share binders to friends.

The app embeds all the data for a specific binder in a compressed URL but can still vary quite a lot with length due to the amount of variance in binder data (# cards, data for each card etc.).

Using this URL generator we store full binder URL data in a Postgres DB and return a 10 char appended url to the host site which forwards to the binder.

https://oddreflex.pythonanywhere.com/

### Usage
The server handles a POST request with a 'url' data param set to the desired url to be made shorter/into a short binder URL.  
The server forwards any other GET urls to the stored internal site they point to (if valid).

#### Example
Create a link to this Gtihub repo:  
`curl -d "url=https://github.com/pantherNZ/YuGiOh-BinderURL" OddReflex.pythonanywhere.com/`  
Result:  
`http://oddreflex.pythonanywhere.com/JWeQUIWw`


### Implementation
* Python 3.9
* Postgres DB
* Flask
* pipenv
* Pythonanywhere for hosting

### Setup
* Clone repo
* pipenv install
* pipenv shell
* flask run
* Navigate to http://127.0.0.1:5000 (localhost:5000)
