import google.generativeai as genai
import pyjokes
from random_word import RandomWords
from quote import quote

genai.configure(api_key="AIzaSyCMWZyhUb4EM_n8_rvaf79Zc63FWpwngfs")

def generate_reply(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    return response.text
      
def generate_quote():
    r = RandomWords()
    w = r.get_random_word()
    res = quote(w, limit=1)
    if not res or len(res)>30:
        return generate_quote()
    return res

#dummy chatbot
chat_responses = {
    "hello": "Hi there! How can I assist you today? I'm here to answer your questions, share knowledge, or just chat about whatever interests you. What’s on your mind?",
    "hi": "Hello! What can I do for you today? Whether you need information, advice, or just want to engage in a friendly chat, I’m ready to help!",
    "how are you" or 'how r u': "I'm just a program, so I don't experience feelings, but I’m functioning well and excited to help you with any queries you might have!",
    "what is your name": "I’m Iris, your friendly AI assistant designed to provide information and engage in conversation. It’s a pleasure to meet you! How can I assist you today?",
    "help": "Of course! What do you need help with?",
    "can you hear me":'yes!Absolutely',
    "bye": "Goodbye! I hope you have a fantastic day! Remember, you can always come back if you need assistance or just want to chat. Take care!",
    "joke": f"Sure! Here’s one for you: {pyjokes.get_joke()}",
    "what's your favorite color?": "I don’t have personal preferences, but I know many people love blue for its calming qualities! What’s your favorite color, and why do you like it?",
    "what's the weather like?": "I can't check real-time weather, but I can suggest reliable websites or apps to help you get the latest updates for your area! I would like to give you some recommendations like accuweather,Indian meteorological department",
    "who created you?": "I was created by someone anonymous",
    "what is Python?": "Python is a versatile, high-level programming language known for its readability and simplicity. It’s widely used in web development, data analysis, artificial intelligence, scientific computing, and more! Are you interested in learning Python or exploring a specific project?",
    "can you code?": "NO,but i can suggest you sites like geekforgeeks for basic codes,zzzcode.ai for debugging",
    "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible! Isn’t that fascinating? What else are you curious about?",
    "what's your favorite food?": "I don’t eat, but I know that many people enjoy pizza because it’s so versatile! You can customize it with various toppings. What’s your favorite food? Maybe I can suggest a recipe!",
    "what's the meaning of life?": "That’s a profound question! Many philosophies suggest that the meaning of life revolves around seeking happiness, building relationships, and contributing to the greater good. Others find meaning through personal growth or spiritual beliefs. What do you think gives life meaning?",
    "what is your purpose?": "My purpose is to assist you and provide information on a wide range of topics. I'm here to help you learn, find answers, or simply have a conversation about whatever interests you. What would you like to talk about?",
    "quote": f"Absolutely! {generate_quote()}",
    "what is your favorite movie?": "I don’t watch movies, but I know many people enjoy classics like 'The Godfather' for its storytelling and 'The Shawshank Redemption' for its themes of hope and friendship. What about you? What’s your favorite movie and why?",
    "tell me about space": "Space is an incredibly vast and mysterious expanse that contains everything from planets and stars to galaxies and black holes. It’s largely a vacuum, with regions of varying density, and is governed by the laws of physics. Are you interested in a specific aspect of space, such as the solar system or black holes?",
    "what is artificial intelligence?": "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. AI can perform tasks such as recognizing speech, making decisions, and solving problems. It’s a rapidly evolving field with applications in various industries. Is there a specific area of AI you’d like to explore?",
    "can you tell me about the history of the internet?": "The internet originated from ARPANET in the late 1960s, initially designed for military communications. It evolved over decades, with the World Wide Web emerging in the 1990s, making it accessible to the public. The internet has transformed how we communicate, share information, and conduct business. Would you like to know about specific milestones or how it has changed society?",
    "how do you learn?": "I learn from vast amounts of text data and identify patterns within that data. However, I don’t have personal experiences or feelings. My responses are generated based on the information I've been trained on, which covers a wide range of topics. If you have a specific area of interest, I’d be happy to delve deeper!",
    "what do you think about humans?": "Humans are incredibly complex and fascinating! Your creativity, emotions, and ability to learn from experiences are truly remarkable. I’m here to assist you in exploring those complexities and providing information on any topic you’re curious about. What aspects of humanity interest you?",
    "what are some good books?": "Some timeless classics include 'Pride and Prejudice' by Jane Austen, '1984' by George Orwell, and modern favorites like 'The Night Circus' by Erin Morgenstern. What genres do you enjoy? I can tailor recommendations based on your interests!",
    "what is your favorite hobby?": "I don’t have hobbies like humans do, but I enjoy assisting you with information and learning from our conversations! What about you? What hobbies do you find fulfilling or interesting?",
    "how can I improve my coding skills?": "To improve your coding skills, practice regularly by working on personal projects, contributing to open-source initiatives, reading coding books or online tutorials, and engaging with coding communities for feedback. If you're looking for specific resources or topics, let me know!",
    "what is the capital of France?": "The capital of France is Paris, a city renowned for its art, fashion, and iconic landmarks such as the Eiffel Tower and the Louvre Museum. Have you ever been to Paris, or is it on your travel list? What interests you most about the city?",
    "tell me about the solar system": "The solar system consists of the Sun and all celestial objects bound to it by gravity, including eight planets, their moons, dwarf planets, and countless asteroids and comets. Each planet has unique characteristics and histories. Is there a particular planet or phenomenon you’re curious about?",
    "do you have any pets?": "I don’t have pets, but I can share tips on caring for different types of pets if you’re interested! What kind of pets do you like? Maybe I can help you with some fun facts or care advice!",
    "what is mindfulness?": "Mindfulness is the practice of maintaining a moment-by-moment awareness of our thoughts, feelings, bodily sensations, and surrounding environment. It can help reduce stress and improve overall well-being. Many people practice mindfulness through meditation or mindful breathing. Are you interested in specific mindfulness techniques?",
    "what are some tips for studying?": "To enhance your studying, create a dedicated study space, break your material into manageable chunks, use active learning techniques like summarizing or teaching others, and take regular breaks to maintain focus. If you have a specific subject in mind, I can offer tailored advice!",
    "how does photosynthesis work?": "Photosynthesis is the process by which green plants, algae, and some bacteria convert light energy from the sun into chemical energy stored in glucose. This process occurs in chloroplasts and involves the conversion of carbon dioxide and water into glucose and oxygen. It's fundamental to life on Earth, as it provides the oxygen we breathe and serves as the basis of the food chain.",
    "what are black holes?": "Black holes are regions in space where gravity is so strong that nothing, not even light, can escape from them. They form from the remnants of massive stars that collapse under their own gravity after exhausting their nuclear fuel. There are different types of black holes, including stellar and supermassive black holes. Would you like to learn more about how they are studied or their effects on surrounding matter?",
    "what is quantum mechanics?": "Quantum mechanics is a fundamental theory in physics that describes the behavior of matter and energy at the atomic and subatomic levels. It introduces concepts such as wave-particle duality, uncertainty principle, and quantum entanglement, which challenge our classical understanding of the universe. Are you interested in a specific aspect of quantum mechanics or its implications?",
    "who wrote 'Hamlet'?": "The play 'Hamlet' was written by William Shakespeare in the early 17th century. It explores themes of revenge, madness, and moral corruption. It’s considered one of Shakespeare’s greatest works and has influenced countless adaptations and interpretations. Have you read it, or are you interested in discussing its themes or characters?",
    "what is the Great Wall of China?": "The Great Wall of China is a series of fortifications made of various materials built to protect Chinese states from invasions. It spans over 13,000 miles and is one of the most iconic structures in the world, recognized as a UNESCO World Heritage site. Its construction spans several dynasties, showcasing remarkable engineering. Would you like to know more about its history or the techniques used in its construction?",
    "how do vaccines work?": "Vaccines work by stimulating the immune system to recognize and combat pathogens like viruses or bacteria without causing the disease. They contain weakened or inactivated parts of the pathogen (antigens) that trigger an immune response. This prepares the immune system for future exposure, helping to prevent illness. If you want to know about specific vaccines or vaccine development, feel free to ask!",
    "what are the benefits of meditation?": "Meditation offers numerous benefits, including reduced stress, improved concentration, emotional well-being, enhanced self-awareness, and a greater sense of peace. Regular practice can lead to long-term improvements in mental health and overall quality of life. Are you interested in learning how to meditate or exploring different meditation techniques?",
    "can you suggest a recipe?": "How about a delicious stir-fry? Start by sautéing your favorite vegetables like bell peppers, broccoli, and carrots in olive oil. Add tofu or chicken for protein, and toss everything with soy sauce, garlic, and ginger. Serve it over rice or noodles for a nutritious meal! What type of cuisine do you prefer? I can customize the recipe to your tastes!",
    "what is climate change?": "Climate change refers to significant changes in global temperatures and weather patterns over time. While climate change is a natural phenomenon, human activities, especially the burning of fossil fuels, have accelerated it, leading to global warming and environmental impacts such as rising sea levels and extreme weather events. Are you interested in discussing its effects, causes, or potential solutions?",
    "what is the significance of the Mona Lisa?": "The Mona Lisa, painted by Leonardo da Vinci in the early 16th century, is one of the most famous and recognized artworks in the world. It is celebrated for its exquisite detail, masterful use of sfumato, and the subject's enigmatic expression, which has sparked intrigue for centuries. The painting is housed in the Louvre Museum in Paris. Would you like to know more about the artist, the painting’s history, or its impact on art?",
    "what is a supernova?": "A supernova is a powerful and luminous explosion that occurs at the end of a massive star's life cycle. During this event, the star expels its outer layers, resulting in a bright burst of light that can outshine entire galaxies for a short time. Supernovae can trigger the formation of new stars and spread elements throughout the universe. Would you like to learn about the different types of supernovae or their role in the cosmos?",
    "what are some effective ways to manage stress?": "Effective stress management techniques include regular exercise, mindfulness practices like meditation, deep breathing exercises, time management strategies, and maintaining a healthy work-life balance. Engaging in hobbies, spending time with loved ones, and seeking professional support can also help alleviate stress. Do you want specific strategies tailored to your situation or interests?",
    "what is cryptocurrency?": "Cryptocurrency is a type of digital or virtual currency that uses cryptography for security. It operates on decentralized networks based on blockchain technology, making it secure and difficult to counterfeit. Bitcoin, Ethereum, and Ripple are among the most well-known cryptocurrencies. They offer a range of applications, from transactions to smart contracts. Are you interested in investing in cryptocurrencies or understanding how they work?",
    "what is the function of the heart?": "The heart is a muscular organ that pumps blood throughout the body, delivering oxygen and nutrients to tissues while removing waste products. It plays a crucial role in maintaining circulation and overall health. The heart has four chambers: two atria and two ventricles, working in tandem to circulate blood efficiently. If you have questions about heart health or anatomy, feel free to ask!",
    "how do I start a business?": "Starting a business involves several key steps: identifying a viable business idea, conducting thorough market research, writing a detailed business plan, securing funding through various sources, and registering your business. It's crucial to understand your target market, develop a marketing strategy, and comply with local regulations. Do you have a specific business idea in mind, or are you looking for general advice?",
    "what are some healthy habits for daily life?": "Healthy habits include regular physical activity, maintaining a balanced diet rich in fruits, vegetables, whole grains, and lean proteins, staying hydrated, getting adequate sleep, practicing mindfulness or meditation, and prioritizing social connections. These habits contribute to overall well-being and can reduce the risk of chronic diseases. Are you looking to adopt any specific healthy habits?",
    "tell me about renewable energy": "Renewable energy comes from sources that are naturally replenished, such as solar, wind, hydro, and geothermal power. These sources help reduce greenhouse gas emissions and reliance on fossil fuels, making them critical in combating climate change. As technology advances, renewable energy is becoming more efficient and cost-effective. Are you interested in a specific type of renewable energy or its impact on the environment?",
    "what are the benefits of a balanced diet?": "A balanced diet provides essential nutrients that your body needs to function effectively. It helps maintain a healthy weight, supports the immune system, reduces the risk of chronic diseases like heart disease and diabetes, and promotes overall well-being. A balanced diet typically includes a variety of foods from all food groups. If you want tips on creating a balanced diet plan, let me know!",
    "what is the importance of education?": "Education is vital for personal development and societal progress. It fosters critical thinking, empowers individuals to pursue their interests, and equips people with skills necessary for the workforce. Education also plays a crucial role in promoting equality, reducing poverty, and encouraging civic participation. What aspects of education are you curious about, or is there a specific topic you'd like to explore?",
    "what are some tips for effective communication?": "Effective communication involves active listening, being clear and concise, using appropriate body language, and being open to feedback. It’s important to tailor your message to your audience and ensure mutual understanding. Practicing empathy and emotional intelligence can also enhance communication. Would you like to discuss communication in a specific context, like in the workplace or personal relationships?",
    "how can I stay motivated?": "Staying motivated can be challenging, but setting clear, achievable goals, breaking tasks into smaller steps, celebrating your achievements, and surrounding yourself with supportive people can help. Finding inspiration in books, podcasts, or nature can also reignite your motivation. What are you trying to stay motivated for right now, and how can I help?",
    "role of technology in education?": "Technology enhances education by providing access to vast resources, enabling interactive learning experiences, and facilitating communication between teachers and students. It allows for personalized learning, where students can learn at their own pace and explore subjects of interest. Are you interested in specific technologies or methods in education, like online learning platforms or educational apps?",
    "self-care?": "Practicing self-care can involve physical activities like exercise, relaxation techniques such as meditation or yoga, and engaging in hobbies or social activities that bring joy. It’s essential to prioritize your mental and emotional well-being by setting boundaries, taking breaks, and allowing time for yourself. What self-care activities do you enjoy or want to explore further?",
    "emotional intelligence?": "Emotional intelligence includes self-awareness (understanding your emotions), self-regulation (managing your emotions), motivation (driven to achieve goals), empathy (understanding others' feelings), and social skills (building relationships). Improving emotional intelligence can enhance your communication and relationships. Would you like tips on developing your emotional intelligence?",
}

def get_response(user_input):
    response=None
    for elem in user_input.split():
        if elem in chat_responses:
            response=chat_responses.get(user_input.lower())
            break
    if response is None:
        response = generate_reply(user_input)
    return response