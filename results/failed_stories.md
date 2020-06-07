## 10. complete path - greet - restaurant_search + invalid location - mail
* restaurant_search{"location": "Hisar"}
    - slot{"location": "Hisar"}
    - utter_invalid_location   <!-- predicted: utter_ask_cuisine -->
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye


## 12. complete path + combined (location + cuisine)
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location   <!-- predicted: utter_invalid_location -->
* restaurant_search{"location": "Pune", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "Pune"}
    - slot{"location": "Pune"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "parth.patel@gmail.com"}
    - slot{"email": "parth.patel@gmail.com"}
    - slot{"email": "parth.patel@gmail.com"}
    - action_send_mail
    - utter_mail_sent


## 14. complete path + combined (location + budget)
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location   <!-- predicted: utter_invalid_location -->
* restaurant_search{"location": "bangalore", "price": "low"}
    - slot{"location": "bangalore"}
    - slot{"price": "low"}
    - slot{"location": "bangalore"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "india@outlook.com"}
    - slot{"email": "india@outlook.com"}
    - slot{"email": "india@outlook.com"}
    - action_send_mail
    - utter_mail_sent


## 16. combined (location + cuisine + budget) 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location   <!-- predicted: utter_invalid_location -->
* restaurant_search{"location": "Lucknow", "price": "low", "cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Lucknow"}
    - slot{"price": "low"}
    - slot{"location": "Lucknow"}
    - slot{"price": "low"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "srk@gmail.com"}
    - slot{"email": "srk@gmail.com"}
    - slot{"email": "srk@gmail.com"}
    - action_send_mail
    - utter_mail_sent


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location   <!-- predicted: utter_invalid_location -->
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "prashant.upadhyay1996@gmail.com"}
    - slot{"email": "prashant.upadhyay1996@gmail.com"}
    - slot{"email": "prashant.upadhyay1996@gmail.com"}
    - action_send_mail
    - slot{"location": "bangalore"}
    - utter_mail_sent


## interactive_story - complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location   <!-- predicted: utter_invalid_location -->
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_mail
* deny
    - utter_goodbye


## interactive_story - complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location   <!-- predicted: utter_invalid_location -->
* restaurant_search
    - utter_invalid_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "sdhjk.djfh@edu.co.in"}
    - slot{"email": "sdhjk.djfh@edu.co.in"}
    - slot{"email": "sdhjk.djfh@edu.co.in"}
    - action_send_mail
    - slot{"location": "Mumbai"}
    - utter_mail_sent


## 3. complete path + invalid location + email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location   <!-- predicted: utter_invalid_location -->
* restaurant_search{"location": "gaya"}
    - slot{"location": "gaya"}
    - utter_invalid_location   <!-- predicted: utter_ask_cuisine -->
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - slot{"location": "Patna"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "arpit.khurana@outlook.com"}
    - slot{"email": "arpit.khurana@outlook.com"}
    - slot{"email": "arpit.khurana@outlook.com"}
    - action_send_mail
    - utter_mail_sent


## 4. complete path + invalid location - email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location   <!-- predicted: utter_invalid_location -->
* restaurant_search{"location": "Panipat"}
    - slot{"location": "Panipat"}
    - utter_invalid_location   <!-- predicted: utter_ask_cuisine -->
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye


## 8. complete path - greet + invalid location - mail
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Satara"}
    - slot{"location": "Satara"}
    - utter_invalid_location   <!-- predicted: utter_ask_cuisine -->
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye


