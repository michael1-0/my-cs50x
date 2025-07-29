# Enkrip: All About Cryptography
### March 2024
### Greetings and welcome! This is a presentation of my final project for CS50x from Harvard University. My name is Michael Bagaskoro Edwards, I'm from Indonesia. I'm currently a first-year undergraduate student pursuing Informatics and would like to learn more about computer science outside of my classes with this program.
***
### Video Demo:  <https://youtu.be/E-pLu2GyNuE>
### Description:
This project is a fully responsive mobile friendly light-weight Flask powered website about the field of cryptography, where you can find all sorts of tools and information about ciphers, encryptions; cryptography in general. In this website, I used the Flask framework and Bootstrap for the styling. I first had the inspiration from week 2 Substitution problem set, where I took an interest in how cryptography works. This website includes tools like GPT instructor from OpenAI API that answers most cryptographic questions in detail, and also other types of questions if you wish to ask the AI, I configured the instructor to be cost efficient but still answers in detail. There are also encryptions and decryptions using the Fernet cryptographic recipe from the python Cryptography library. This website also includes ciphers information which people can read how it works, and how secure it is; there is also an articles page that I plan to expand on. In terms of styling, I went with a monochrome theme, the images on this website are all AI generated with Microsoft's Image Creator, including the icon!

This project will serve as the beginning of my cryptographic knowledge journey that I plan to embark on further; the more my knowledge increases in this field, the more I will update this project, so it's kind of like my notes for the cryptography subject.

The goal of this project is to provide the community about cryptography information, as I see not a lot of people have information about this subject; to educate myself and other people through this website. With the rise of quantum computing and AI, I see there is a growing need for people to know more about cryptography. Its significant importance in computer security, makes it an important subject to learn for the sake of the future. I will add an Indonesian translated version of the website also in the future; because majority of Indonesians don't know English very well! If you would like to know more, see the video link above for a full demo.

### `Home Page`
In the home page, there are numerous elements. There is a navbar that user can navigate through the website, this navbar will appear in every page for ease of access, and I made it so it will be fixed to the top even if user decides to scroll down the page. There are also cards that contain buttons user can visit for information/tools, all according to the descriptions of the cards. The first card leads to information about the Atbash Cipher, the second leads to the available tools like encryptions, decryptions and AI instructor (more to come). The third leads to the AI instructor page. And a thank you card for the CS50 team! Lastly, a card that leads to the articles page.

### `Tools Page`
There are 3 tools that are available as of now from this website. The first is an encryptor that uses the python Cryptography library's Fernet recipe, then second is its decryptor; lastly, an AI instructor which uses the GPT-3.5-turbo-instruct model using an API Key loaded from the environment variables (python-dotenv). I will continue adding all kinds of encryptions and decryptions to this in the future, as my cryptographic knowledge increases.

### `Ciphers and Articles Pages`
In the ciphers page, there are all kinds of information about ciphers history and origins; how it works, how secure it is. The ciphers are of 4 types, substitution, transposition, block and stream ciphers, each with examples.

In the articles page, there is currently only one article, I plan to make this article system more dynamic, so that I can add articles easily without needing to alter the file (automation) and to add more articles in the cryptography field. More to come!
***

### Things I Learned
+ I learned about Flask and its structure to create a website, it's very simple; not what I thought it would be, this project has deepened my knowledge in making websites!
+ Modern cryptography knowledge.
+ Cryptography library and its components.
+ I learned how to create a good front-end with only Bootstrap 5 and CSS.
+ OpenAI API knowledge.
+ Image creation with AI and generative AI prompt making in general.

### Thank You
Special thanks to the CS50 team and its community and thank you for inspiring thousands of people about the art that is programming! I highly reccommend CS50 to anybody that wants to learn programming, computer science in general. And thank you for taking the time to read this!
