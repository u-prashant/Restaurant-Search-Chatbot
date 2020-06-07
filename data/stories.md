## 1. complete path + email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}  
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "amrit.kharbanda@gmail.com"}
    - slot{"email": "amrit.kharbanda@gmail.com"}
    - action_send_mail
    - utter_mail_sent

## 2. complete path + email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}  
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "arun.prasad@hotmail.com"}
    - slot{"email": "arun.prasad@hotmail.com"}
    - action_send_mail
    - utter_mail_sent
    
## 3. complete path + invalid location + email 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gaya"}
    - utter_invalid_location
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}  
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "arpit.khurana@outlook.com"}
    - slot{"email": "arpit.khurana@outlook.com"}
    - action_send_mail
    - utter_mail_sent
    
## 4. complete path + invalid location - email 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Panipat"}
    - utter_invalid_location
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}  
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye

## 5. complete path - email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}  
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye

## 6. complete path - email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}  
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye
    
## 7. complete path - greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}  
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "pranav.srivastava@yahoo.com"}
    - slot{"email": "pranav.srivastava@yahoo.com"}
    - action_send_mail
    - utter_mail_sent
    
## 8. complete path - greet + invalid location - mail
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Satara"}
    - utter_invalid_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}  
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye
    
## 9. complete path - greet - restaurant_search + mail
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}  
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "satyam.singh@net.com"}
    - slot{"email": "satyam.singh@net.com"}
    - action_send_mail
    - utter_mail_sent
    
## 10. complete path - greet - restaurant_search + invalid location - mail
* restaurant_search{"location": "Hisar"}
    - utter_invalid_location
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}  
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye
    
    
## 11. complete path - restaurant_search + mail
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}  
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "satyam.singh@net.com"}
    - slot{"email": "satyam.singh@net.com"}
    - action_send_mail
    - utter_mail_sent
    
## 12. complete path + combined (location + cuisine) 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune", "cuisine": "American"}
    - slot{"location": "Pune", "cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}  
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "parth.patel@gmail.com"}
    - slot{"email": "parth.patel@gmail.com"}
    - action_send_mail
    - utter_mail_sent
    
## 13. complete path -greet + combined (location + cuisine) - mail
* restaurant_search{"location": "Kochi", "cuisine": "Chinese"}
    - slot{"location": "Kochi", "cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}  
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye
    
## 14. complete path + combined (location + budget) 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore", "price": "low"}
    - slot{"location": "bangalore", "price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "india@outlook.com"}
    - slot{"email": "india@outlook.com"}
    - action_send_mail
    - utter_mail_sent
    
## 15. complete path + combined (location + budget) 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Lucknow", "price": "low"}
    - slot{"location": "Lucknow", "price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "anthony.gonsalves@gmail.com"}
    - slot{"email": "anthony.gonsalves@gmail.com"}
    - action_send_mail
    - utter_mail_sent
    
## 16. combined (location + cuisine + budget) 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Lucknow", "price": "low", "cuisine": "Italian"}
    - slot{"location": "Lucknow", "price": "low", "cuisine": "Italian"}
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "srk@gmail.com"}
    - slot{"email": "srk@gmail.com"}
    - action_send_mail
    - utter_mail_sent
    
## 17. complete path + combined (location + cuisine) 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Surat", "cuisine": "South Indian"}
    - slot{"location": "Surat", "cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}  
    - action_search_restaurants
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "parth.patel@gmail.com"}
    - slot{"email": "parth.patel@gmail.com"}
    - action_send_mail
    - utter_mail_sent
    
## 18. complete path - greet + combined (location + cuisine) - mail 2
* restaurant_search{"location": "Jaipur", "cuisine": "Italian"}
    - slot{"location": "Jaipur", "cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}  
    - action_search_restaurants
    - utter_ask_mail
* deny
    - utter_goodbye
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "prashant.upadhyay1996@gmail.com"}
    - slot{"email": "prashant.upadhyay1996@gmail.com"}
    - action_send_mail
    - slot{"location": "bangalore"}
    - utter_mail_sent

## interactive_story - complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_mail
* deny
    - utter_goodbye

## interactive_story - complete path + invalid location
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "dehradun"}
    - slot{"location": "dehradun"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "dehradun"}
    - utter_ask_mail
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "jsdkh.kdjl223@lf.edu.com"}
    - slot{"email": "jsdkh.kdjl223@lf.edu.com"}
    - action_send_mail
    - slot{"location": "kolkata"}
    - utter_mail_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_invalid_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "sdhjk.djfh@edu.co.in"}
    - slot{"email": "sdhjk.djfh@edu.co.in"}
    - action_send_mail
    - slot{"location": "Mumbai"}
    - utter_mail_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_mail
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "jaipur"}
    - utter_ask_mail
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_ask_mail
* affirm
    - utter_ask_email_id
* email_id{"email": "prashantuproject@gmail.com"}
    - slot{"email": "prashantuproject@gmail.com"}
    - action_send_mail
    - slot{"location": "surat"}
    - utter_mail_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_invalid_location
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "gurgaon"}
    - utter_ask_mail
* deny
    - utter_goodbye
