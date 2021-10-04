# My own social media analyzer

### 1. User story and the MVP
>* ### user story  
>> I can use the analyzer to get someone's Twitter account information, including the date of register, discription of the account, accound ID, and username.  
>> I can get sentiment analysis results abuot twitter texts of one user from the analyzer.   
>* ### MVP
>> People can get basic twitter account information, and get the analysis results of twitter text from the analyzer.  

###2. Modular Design
>> 1. Use twitter api to search basic information of a user. 
>> 2. the analyzer get timeline of the twitter text of the user through twitter api
>> 3. put the twitter text from twitter api into a json file
>> 4. use google-NLP-API to analyze the json file to get the result of analyze_sentiment, nalyze_text_entities, analyze_text_syntax functions and classify_text
>> 5. the final results will display by numbers in a table.

###3. Who will be my user
>> My user will be someone who has interests to analyze others. For example, people can get information from the analyer to konw what his/her new friends likes. 

###4. Basic usr story
>> people want to get infromation from twitter text in order to know others better.  
 
