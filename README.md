# 🌟 **Fun Discord Bot** 🌟  
`discord bot` `discord` `bot` `fun bot` `smart` `Hebrew Discord Bot` `Hebrew Bot` `Discord` `Hebrew and English Discord Bot` 

![Discord](https://img.shields.io/badge/Discord-Bot-blue)
![Fun](https://img.shields.io/badge/Fun-Bot-yellow)
![Smart](https://img.shields.io/badge/Smart-Bot-green)
![Hebrew](https://img.shields.io/badge/Hebrew-Bot-orange)
![Language](https://img.shields.io/badge/Language-Hebrew%20%26%20English-red)
### A conversational Discord bot designed to fit perfectly into your server.

---

- 🗨️ **Talks Smart**: Handles conversations and responds well to various situations.  
  - Features **tree-based answers** for **fast response times**.  
  - Easily customizable to suit your needs—recode it however you like!  
- 📚 **DB functionality for the Fun**: Lets users add **notes**, create **lists**, and handle database functionality for server-wide fun (mongoDB).  
- 🎭 **All the Basics**: Tells **jokes**, **stories**,  **weather updates**, etc .  
- 🌍 **Multilingual**: Built for **English**, with added **Hebrew support** , great for Israeli servers 🇮🇱. (you can disable it easily in responses.py)  

---

#### **Deployment**  
Deploying is easy with **Docker** and **Railway**:  
- Use the provided **Docker configuration** for quick setup.  
- Highly recommend **Railway** for hassle-free deployment ([check them out](https://railway.app)).  

---

---
notes:
 - 
####  If you encounter incomplete words in the code, this may be the reason: <br/><br/> when searching for words, if I determine that a word is still recognizable without its first or last one or two letters, I search for it without those letters. This approach allows for minor typos while maintaining clarity, though it may not cover every possibility—it's a step toward improvement nonetheless.


- The bot doesn’t have a traditional menu (except the db functionality , you can see menu by saying "bot db menu"),
as it's mainly focused on conversational interaction. For more rare commands, such as asking about the weather, the bot doesn’t require the word "bot" to be included in the sentence, since these requests are less common in everyday conversation and probably directed to the bot. However, for more common responses, the bot will only trigger response if the word "bot" is present in the sentence.

 - It's generally supposed to be somewhat annoying, so it also responds to semi-common sentences, even when 'bot' isn't mentioned. However, it should avoid responding to very common sentences

- To improve response time, I’ve categorized input into keywords and linked them to specific questions or functions related to those words. This makes the bot’s processing more efficient. Additionally, I’ve accounted for common filler words people often include when talking to the bot, so the system can better handle natural language.

 - The input is first converted to lowercase and all regex are removed before generating answer.

