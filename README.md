
## Because I accidentally committed the MongoDB URL, I replaced it.</br>Don't bother trying to use it.</br>both git rm --cached and git filter-branch aren't working for me for some reason right now, I know they can help


yudbeit9Bot


## - keywords tree based answers for minimal response time </br>- conversational</br>- hebrew and english</br>- db functionality </br>- easy to deploy & start using
  
This is a bot that supports both English and Hebrew commands. You can ask it for the time, weather updates, stories,
jokes, create lists of ideas and notes (stored with mongo db) and similar things. It's also designed to hold conversations, responding to a wide range of situations.
The bot doesn’t have a traditional menu (except the db functionality , you can see menu by saying "bot db menu"),
as it's mainly focused on conversational interaction.
For more rare commands, such as asking about the weather, the bot doesn’t require the word "bot" to be included in the sentence, 
since these requests are less common in everyday conversation and probably directed to the bot.
However, for more common responses, the bot will only trigger response if the word "bot" is present in the sentence.

It's generally supposed to be somewhat annoying, so it also responds to semi-common sentences, even when 'bot' isn't mentioned.
However, it should avoid responding to very common sentences

To improve response time, I’ve categorized input into keywords and linked them to specific questions or functions related to those words.
This makes the bot’s processing more efficient. Additionally, I’ve accounted for common filler words people often include
when talking to the bot, so the system can better handle natural language.

The input is first converted to lowercase and all regex are removed before generating answer.

### If you encounter incomplete words in the code, this may be the reason: when searching for words,</br>if I determine that a word is still recognizable without its first or last one or two letters, I search for it without those letters. This approach allows for minor typos while maintaining clarity, though it may not cover every possibility—it's a step toward improvement nonetheless.

#### I use Railway.app with docker and highly recommend it.</br>you can cancel db functionality changing the env var "IS_USING_MONGO_DB" to anything else but 'using mongo db'

todo:
    more testing
    add more responses to more situations



אם חיפשתם בוט סביר לשרת שלכם ללא מאמץ, אתם מזומנים להשתמש בקוד הזה, יש פה גם פקודות בעברית וגם באנגלית, והקוד קל להבנה, כך שתוכלו להוסיף בקלות
כל מה שאתם רוצים! 



<br>
<br>
<br>
hebrew discord bot hebrew bot discord hebrew and english discord bot בוט לדיסקורד בעברית בוט בעברית לדיסקורד בוט בעברית לדיס בוט לדיס בעברית בוט לדיסקורד בוט מוכן לדיסקורד הבוט של יב9
