from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(bot)

trainer.train([
        'What are the symptoms of actinic keratoses?',
        "Rough, dry or scaly patch of skin, usually less than 1 inch in diameter, Color variations including pink, red or brown, Itching, burning, bleeding or crusting, New patches or bumps on sun-exposed areas of the head, neck, hands and forearms",
        'What are the preventive measures of actinic keratoses ?',
        'Limit your time in the sun. Especially avoid time in the sun between 10 a.m. and 2 p.m. And avoid staying in the sun so long that you get a sunburn or a suntan, Use sunscreen, Avoid tanning beds'])

trainer.train([
        'What are the symptoms of basal cell carcinoma ?',
        "Basal cell carcinoma usually develops on sun-exposed parts of your body, especially your head and neck, It appears as a change in the skin, such as a growth or a sore that won't heal, Fragile and can bleed easily",
        'What are the preventive measures of basal cell carcinoma ?',
        'Wear sunscreen year-round, Avoid the sun during the middle of the day, Check your skin regularly and report changes to your doctor, Avoid tanning beds'])

trainer.train([
        'What are the symptoms of benign keratosis?',
        'waxy brown, black or tan growth and slightly elevated appearance, often appear on the back or chest, but can occur on any part of the body, Ranges in size from very small to more than 1 inch across, may itch',
        'What are the preventive measures of benign keratosis?',
        'In many cases, you don’t need treatment. However, your doctor may decide to remove any growths that have a suspicious appearance or cause physical or emotional discomfort.'])

trainer.train([
        'What are the symptoms of dermatofibroma ?',
        "a round bump that is mostly under the skin, about the size of the tip of a ballpoint pen to a pea, and it usually remains stable, may be pink, red, gray, light brown or purple, commonly found on the legs, but sometimes on the arms, trunk, and less common elsewhere on the body, When pinched  it will dimple inward on itself",
        'What are the preventive measures of dermatofibroma ?',
        'localized corticosteroid injection, shaving the top to flatten the growth, Any growth that is changing size, shape, or color and follows an irregular pattern, bleeds, becomes painful, itches or grows rapidly should also be reported to a doctor'])

trainer.train([
        'What are the symptoms of melanoma ?',
        "Spread of pigment from the border of a spot into surrounding skin, itchiness, tenderness, or pain, moles with two very different-looking halves, more than 50 ordinary moles on your body, oozing, bleeding, hard or lumpy",
        'What are the preventive measures of melanoma ?',
        "Avoid the sun during the middle of the day, Avoid tanning lamps and beds, Become familiar with your skin so that you'll notice changes. Make an appointment with your doctor if you notice any unusual skin changes"])

trainer.train([
        'What are the symptoms of melanocytic nevi ?',
        "brown, tan, pink or black spots on the skin, bumpy texture, dark, coarse hair, 30 and 40 moles, size increased with age, bleeding",
        'What are the preventive measures of melanocytic nevi ?',
        'Wear a hat, long sleeves and a long skirt or trousers, Apply sunscreen to areas you cant cover when outdoors, Make an appointment with your doctor if a mole looks unusual, grows or changes'])

trainer.train([
        'What are the symptoms of vascular lesions ?',
        "When found at the skin or mucosal level (often in the mouth) they can cause problems with weeping and pain, appear as deeper-seated, softer compressible masses often in the neck or axilla with overlying bluish skin discoloration, overgrowth or enlargement of blood vessels",
        'What are the preventive measures of vascular lesions ?',
        'Laser treatment is usually the best option for vascular lesions of the face, Cold compresses can help with redness and swelling, Avoid having tanned skin'])

def medical_bot(user_input):
    print(user_input)
    bot_response = bot.get_response(user_input)
    print(bot_response)
    return bot_response
#print(medical_bot('What are the symptoms of melanocytic nevi ?'))
