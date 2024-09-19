#!/usr/bin/env python
# coding: utf-8

# #1
# 
# https://chatgpt.com/share/66ea7057-df64-8004-b7d9-40441200334f
# Above is the link to the conversation I had with chatgpt which explained each part of the Monte Hall problem for me.

# #2
# https://chatgpt.com/share/66ea7057-df64-8004-b7d9-40441200334f
# This is the conversation I had with chat regarding making the Monte Hall Code simpler.

# In[2]:


#3

import numpy as np

# Parameters
# The choices the player has
doors = {1, 2, 3}
# The number of times the game goes on
reps = 100000
# Win counter
wins = 0

for _ in range(reps):
    # Randomly choose the winning door and the player's initial choice (at the very beginning of the game)
    winning_door = np.random.choice(list(doors))
    player_choice = np.random.choice(list(doors))
    
    # Host reveals a goat door (a losing door that's not the player's choice or winning door)
    goat_door = np.random.choice(list(doors - {winning_door, player_choice}))
    
    # Player switches to the other unopened door using set difference
    player_choice = (doors - {player_choice, goat_door}).pop()
    
    # Check if the player won after switching
    wins += (player_choice == winning_door)

# Calculate win rate
win_rate = wins / reps
win_rate


# In[1]:


# Markov Chains and Text Generation
from IPython.display import YouTubeVideo
YouTubeVideo('56mGTszb_iM', width = 550)


# 4.
# https://chatgpt.com/share/66eb6650-dd88-8004-b9c4-4a04b434b35d
# 
# The link above is the continued conversation I had with chat. It explained each part of the markov code to me. 

# 5.
# https://chatgpt.com/share/66eb6650-dd88-8004-b9c4-4a04b434b35d
# Chatgpt understood the extensions and used to word "Bigram."
# 
# https://chatgpt.com/share/66eb68d7-5798-8004-81a6-2b2143f209f9
# In this new chat, I provided the original code and then the extension to Chatgpt and asked it to explain each part to me.

# 6.
# 
# 1. The Chatbot (specifically ChatGPT) was quick when helping me understand the Monte Hall problem and Markovian Chatbot codes as it automatically assumed I was asking it to explain what the code does as a whole. I was also able to prompt it to explain each line of the code and it did so by explaining the different python functions and why they were important to the code's functionality. 
# 
# 2. The only time it was frustrating to interact with Chat was when I asked it to explain the second extension. This was frustrating because it gave me very lengthy explanations in the very beginning instead of one direct concise sentence at the start. Since I was confused, I was able to ask it if my interpretation was right. 
# 
# 3. I believe it is a very useful tool because it gives in-depth/general explanations to code. I was also able learn what each code line meant and why it was important to the program.

# 7. I doubted Chatbots and AI driven assistance tools before entering this course as there was a never time in high school where I was encouraged to properly use chatgpt. I've only heard negative things about it, like how students use it to write English essays. But after entering this course, I see how it is useful to learn quickly as opposed to searching concepts up on google.

# 8.
# (1 and 2)
# https://chatgpt.com/share/66eb8c07-b6c4-8004-8ee8-8adb4e7e9b3b
# Above is the link of the conversation I had with chatgpt regarding skills in the data science industry and what skills I need for the career choice I want to pursue. Below is the summary it provided.
# 
# 3.
# Essential Skills in Data Science:
# 
# We discussed core skills required in data science, including programming (Python, R, SQL), machine learning, data visualization, big data technologies, and statistical knowledge. Additionally, soft skills like communication, collaboration, business acumen, and a commitment to continuous learning were highlighted as essential.
# Adaptability in Data Science:
# 
# You emphasized the importance of being adaptable and open to new learning techniques, which I agreed with. In a rapidly evolving field like data science, the ability to learn new tools, methods, and technologies is crucial.
# Possibility of Being a Data Scientist Without Coding:
# 
# We explored whether one could be a data scientist without coding or data analysis. While coding is central to the role, it’s possible to work in adjacent roles such as data science management, consulting, or theoretical statistics that may involve less coding, depending on the specific responsibilities.
# Key Skills for Data Science in Healthcare and Economics:
# 
# For healthcare: Key skills include biostatistics, machine learning for healthcare, clinical trial analysis, and understanding regulations like HIPAA. Soft skills like collaborating with medical professionals and ethical decision-making are also essential.
# For economics: Important skills include econometrics, time-series analysis, economic theory, and policy impact analysis. Familiarity with platforms like Stata and Bloomberg, as well as strong communication skills for policy translation, are crucial.
# 
# 4.
# I aim to pursue a career in the healthcare or economics field as a data scientist/analyst. In order to do that, I hope to complete in math, statistics and data science courses in undergrad, and a few economics courses if possible. This will help me build a foundation in the data science skills I need, such as learning python, SQL, R, and statistical analysis. Then, I hope to pursue a master's degree that is focused in data science and economics/finance, so I could dig deeper into economic theory and how to model macroeconomic models. 
# 
# 5.
# Chatting with Chatgpt was neither underwhelming/overwhelming as every piece of information and advice was organized quite well with helpful headers and separating the different types of skills needed. To continue this conversation, I would ask what specific courses I should take, what type of internships I should look out for, and what graduate schools in the USA or Canada are specifically good for data science and economics. 
