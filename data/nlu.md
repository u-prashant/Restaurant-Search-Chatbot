## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- sounds good
- thanks
- yes, please
- yes. Please
- yes please

## intent:deny
- no
- nope
- no, thanks
- not
- don't send
- don't send email
- not needed
- no need
- no, i don't want
- no thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hello there
- hi
- hi there
- good morning
- good evening
- dear sir
- hola
- hello!

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I need to have food
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [Pune](location)
- i am looking for an [south indian](cuisine)
- search for restaurants
- anywhere in [nashik](location)
- I am looking for [italian](cuisine) food
- I am looking a restaurant in [Mysore](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- Oh, sorry, in [Chandigarh](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican](cuisine) food.
- can you book a table in [lucknow](location) in a [moderate](price:mid) price range with [mexican](cuisine) food.
- [chennai](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [less than 300](price:low)
- [300-700](price:mid) range
- [greater than 700](price:high)
- [moderate](price:mid) price range
- can you show me some [cheap](price:low) places to eat
- [>700](price:high)
- [<700](price:mid)
- [<300](price:low)
- [>300](price:mid)
- [in range of 300 to 700](price:mid)
- [not more than 300](price:low)
- [not more than 700](price:mid)
- [mid](price)
- [low](price)
- [high](price)
- I need food
- [Delhi](location)
- in need food
- i'm hungry
- [hyderabad](location)
- [300-700 range](price:mid)
- I’m hungry. Looking out for some good restaurants
- [bengaluru](location:bangalore)
- I'm hungry
- [Mexican](cuisine)
- Can you suggest some good restaurants in Rishikesh
- [dehradun](location)
- Can you suggest some good restaurants in [kolkata](location)
- [American](cuisine)
- in mumbaim
- in [Mumbai](location)
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- [jaipur](location)
- [surat](location)
- [Less than 300](price:low)
- pataudi
- [gurgaon](location)
- [Italian](cuisine)
- [mid](price)

## intent:email_id
- [abc.xyz@gmail.com](email)
- my email id is [lablab@yahoo.com](email)
- email - [khan@outlook.com](email)
- [prasad.arun88@gmail.com](email)
- my email is [prashant.upadhyay1996@gmail.com](email)
- you can send me mail on [prashant.upadhyay1996@gmail.com](email)
- [prashant.upadhyay1996@gmail.com](email)
- [jsdkh.kdjl223@lf.edu.com](email)
- [sdhjk.djfh@edu.co.in](email)
- [prashantuproject@gmail.com](email)

## synonym:Chennai
- Madras

## synonym:Delhi
- New Delhi

## synonym:Gurgaon
- Gurugram

## synonym:Mumbai
- Bombay

## synonym:bangalore
- bengaluru
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:high
- greater than 700
- >700

## synonym:low
- less than 300
- cheap
- <300
- not more than 300
- Less than 300

## synonym:mid
- moderate
- 300-700
- <700
- >300
- in range of 300 to 700
- not more than 700
- 300-700 range
- average

## regex:email
- ([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## lookup:location
  data/cities/cities.txt
