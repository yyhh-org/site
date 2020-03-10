---
Title: How to save millions per year for your newspaper?
Date: 2008-04-20 07:45
Author: Yunyao
Category: opinion
Tags: Politics
Slug: how-to-save-millions-per-year-for-your-newspaper
Alias: /blog/2008/04/how-save-millions-year-your-newspaper
Lang: en
---

Dear CEO of XXX News:

 

I am writing in regard to an automatic news article writer (NAW) that can ** **save your company millions of dolloar per year (see appendix below for peudo code). The basic idea of NAW is to be able to automatically generate news articles with comparable quality to news articles written by actual human reporters by your company.

 

As a proof of concept, I have conducted a comprehensive comparison study. The results show that on issues with regard to Olympic Torch Relay 2008,  the similarity of the automatically generated news articles and those manually written by human reporters is higher than 99%, making them undistinguishable by any of your valuable readers. With a click of a button, you can generate news articles using NAW at your wish anytime anywhere. More importantly, your readers will not realize the differences.

 

Since issues with regard to the Olymipic Torch Relay 2008 refect most if not all the issues about China, the above result safely indicates that NAW can be used to replace your news reporters on any issues with regard to China, thus allowing them to concentrate on more important issues such as Iraq, human right issues in US inner cities, independent requests from Hawaii, Porto Rico and Alaska, and so on.

 

Assume that your news paper needs one report with regard to China about every other day. That is about 180 news articles each year. Assume the cost of writing each news articles, including transportation, lodging, meals, salary for your news reporter and his/her crew members, is merely $8000. By investing on this software, with a fix cost of $500 and no operating cost (since it can work on any of the existing computers of your company), you can save nearly $1.5 millions per year from now on!

 

More importantly, with a little more input from human reporters, NAW can be adopted to report issues on many other countries. That is again over millions of saving each year!

 

Thank you very much for your time. Please do let me know should you have any questions. I am looking forward to discuss you next steps.

 

Best regards,

 

an inventor

 

--------------------------------------------------

Appendix:

```
Input:   

$event:      event name
$location:   event location
$date:       event date
           

Output: 

$news:       new article

 
Function:

NewsArticleWriter (event, location, date)

  Begin:

    Let $numProtester = a random number between 3000 to 10000

    Let $numSupporter = numProester/10

    Let $issues = {"Tibet", "FLG", "AgainstChinaMade", "HumanRightIssues", "Free $ProvinceName", $AnyOtherCurrentHotIssue}

    Let $typesProtesters= a random subset from 

    Let $typesSupporters =  {aggressive males bused in and paid by Chinese consolate or by Pro-China organization}

    Let $name = a random popular Chinese name

    Let $locations = an array of nearby locations of $location


    news +=  Write(event, location, date)

    news +=  Write(event, typesProtesters)

    news +=  Write(numProtester, numSupporter)

    // a function writing elaborated version on 
    // predefined topics for each types of protesters
    news +=  WriteMore(typesProtesters) 
   

    for $i between 1 and lengthOf($locations)
       news += Write($location[i], $typesProtesters)

    news +=  Write(name, typesSupporters)

  End

```

 
