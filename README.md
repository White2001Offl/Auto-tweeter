[![Run on Repl.it](https://repl.it/badge/github/White2001Offl/Auto-tweeter)](https://repl.it/github/White2001Offl/Auto-tweeter)

# Auto-tweeter
**Automatically Tweets through random words with your account**

## Diclaimer
**This Script is only made for educational purposes. I'm not responsible for any type of misuse regarding this**

### Working
* Generates Random words from a API and Attaches to a String (I Used 15 words, if you want you can change in API Link)
* Gather Required Data from user i.e., **Auth Token , CSRF Token and Cookies** and Then Attaches to Header JSON Object
* Sends a Request to **Twitter Tweet Post API** with that Data and Captures the Response
* Handled All Errors which occurs in defualt environment 
* Like This It Posts 60 Tweets with your account. You can change your count in while loop

### Limitations of Twitter
* Per Day **2400 Tweets**
* Each 2 and half hours you can post **250 Tweets**, If you post **250 Tweets** in  a span of minutes you need to wait for next two hours

## Functioning
##### First Gathering Data
* To Gather the required data we need to go to [twitter.com](https://twitter.com) website
* **If you're not logged in, login with your account**
* **Then Hit `Ctrl+Shift+I` in your browser**
* **Then head to network Tab Like this**
* <img src="https://i.gyazo.com/e2aafbd97fe0e7bd0aecfd42c1041a2c.png">


* **Then Click on Create a Tweet Button and Write something**


* <img src="https://i.gyazo.com/e575b438c87d47afe1cf718da5295264.png">


* **Click on Tweet and check for a link which looks like this**


* <img src="https://i.gyazo.com/2634e3e51f75a6665b2a8bf41fcbad6d.png">


* **Now Scroll Down to Request Headers and Click on Raw to copy those**


* <img src="https://i.gyazo.com/b263d69991db3089c77003d70ea9f455.png">


* **Now we need only 3 data i.e., `authorization` , `x-csrf-token` , `Cookie`.** 
* So The Data is 
```
authorization - AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnB
x-csrf-token - 95acf22f0a7d8fd02d459d98d0d66a78
Cookie - _ga=GA1.2.1885713541.1596639359; _gid=GA1.2.368891427.1596872199; kdt=ml9trkPqlkX7LpS4BYsOcvcGUaWnK16y5l3AonNA; remember_checked_on=1; eu_cn=1; gt=1292830647749353478; _sl=1; personalization_id="v1_5GYJjAXSKnXDtgYgx18Hgg=="; guest_id=v1%3A159706997164216568; ct0=95acf22f0a7d8fd02d459d98d0d66a78; ads_prefs="HBERBAA="; twid=u%3D3098023532; auth_token=cda8667f94cdcd9dd60de8b2153f0a92eb52be00; lang=en
```

##### Working with Data
* After Gathering Data Just Copy and Paste in Script. This Script creates a File and stores in your PC so, you dont need to enter again and again


* At Hashtag/Mention You can speficy any Hashtag with #TwitterBack and with mention @MentionName. You can Add Basically anything. Its like Custom Text


* After Giving all values the script should start working


* <img src="https://i.gyazo.com/c4edfbb016da71149d71529c38229aaa.png">


* <img src="https://i.gyazo.com/77fda68db83d918a366b8ead6807f1c2.png">


* **I Didn't Added any delay in any tweets, If you want you can add a bit of code to your script**


### Conclusion
**I'll Be happy for any forks.**
**Let me know if there is anything wrong in issues, I'll be happy to check those**
