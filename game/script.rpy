#Date With Math Chan
#By Jacob Rowland (jrow952)

#Initialised Variables
default complement = None

#Characters
define m = Character("Math Chan", colour="#FFFFFF")
define u = Character('You', color="#0066FF")

# The game starts here.
label start:
    stop music fadeout 1.0
    play music "theelevatorbossanova.mp3" loop fadein 1.0
    scene bg lecturehall with fade

    "Another Maths 102 lecture complete!"
    "About time too. An hour is all my brain can take before it all starts passing me by."
    "I begin to hear the rush of students fleeing the scene."
    "The site looking remarkably similar to a certain scene from a Disney classic about wild animals."
    "I'm in no rush today, however, as I think it is finally time that I make a move."
    scene black with fade
    "Today is the day I ask out Math Chan."
    "But where is she?"
    "She must have left already. I've got to find her!"
    scene bg oggb_inside with fade
    "I spot her in the distance making her way outside OGGB as I exit the lecture theatre."
    "It seems like everyone is intersecting my path today! Why can't we all just move in parallel?"
    u "Hey, Math Chan! Wait up a minute!"
    "She looks around and spots me."
    show mathchan smile with dissolve
    stop music fadeout 1.0
    play music "november.mp3" loop fadein 1.0
    m "Hey, whats up? How did you find that lecture?"
    u "Yeah, not too bad. Not sure how circles and triangles are really related. Heh."
    "I can feel my voice tremble. My anxiety is unreal."
    "I can't breath."
    m "Like just how many triangles can there be?"

    menu:
        "Ignore the question":
            u "Yeah. Yeah. Crazy right?"
            "I didn't catch her question but it is now or never."
            u "Sorry if this seems like it is coming out of nowhere but..."
            "My heart begins to exponentially rise."
            "It feels as if soon I'll no longer be able to function."
            u "...would you want to go on a date with me, Math Chan?"

    "She pauses for a moment, as if she has just lost her train of thought."
    m "Wi..with me?"
    "She seems surprised."
    u "Yeah :3"
    show mathchan sad with dissolve
    m "Oh...I don't know...I have quadratics to factorise."
    "I thought this would be more linear."
    "She seems quite cold and reserved? What did I do wrong?"
    u "Oh. I see. Uhm. How about just a stroll through the park on your way home after uni?"

    stop music fadeout 1.5
    scene black with fade

    m "Ok, I can do that."
    jump date

label date:
    "{b}A few hours later...{/b}"

    scene bg park with fade

    "I've been waiting here at Albert Park for what seems like an eternity. Did Math Chan stand me up?"
    "{b}A few moments pass...{/b}"

    play music "romantic.mp3" loop

    "The corner of my eye is caught by a dazzling sight."
    "The sight becomes ever clearer as I focus in."
    "It's Math Chan!"
    "I see her as she makes her way over from the quad towards the park."
    "Her beauty shining upon me like the Sun upon the Earth."
    "Her steps as soft as an angel."
    "She truly is a sight to behold."
    show mathchan smile with dissolve
    "Quick. I need something nonchalant to say so that I can break the ice."
    u "Hey."
    m "Hi."
    u "Uhm. How are you?"
    m "Good. You?"
    u "Same. Same."
    u "How was the rest of your day?"
    m "Eh. It was alright. Nothing special."
    "She appears to be holding back."
    u "Oh o-"
    show mathchan uneasy with dissolve
    "She cuts me off."
    m "So uhm...may I ask..."
    "She seems quite nervous."
    m "I was just wondering..."
    m "...what made me stand out to you?"
    m "W-why do I appeal to you?"
    "I nervously blush."
    menu:
        "I really like your special angles":
            $ complement = "I really like your special angles"
            jump response
        "You are just such a cutie pi":
            $ complement = "You are just such a cutie pi"
            jump response
        "You aren't derivative":
            $ complement = "You aren't derivative"
            jump response

label response:
    show mathchan blush with dissolve
    "*Math Chan blushes*"
    m "Aww. Hehe. How sweet. You're making me blush."
    "I'm glad she thinks so..."
    "...since I sense so much sadness behind those eyes."
    show mathchan sad with dissolve
    "From her reaction you'd think this was the first time she'd been complemented like this."
    "There is sadness behind those eyes."
    m "Sometimes people take one look at me and turn away in terror..."
    m "...like I'm just some big obstacle standing in their way that they can't overcome."
    m "But people just need to get to know me and understand me so that I can open up to them. You know?"
    "She pauses for a moment. As if she is suddenly in a deep introspection."
    u "Yea-"
    "Before I can get a word out she interrupts me again."
    m "I'm sorry, I don't know where that came from."
    "I stand there slightly confused and guilty."
    "I once was that person."
    "I turned around at the first sign of difficulty."
    u "Yeah...I get that. Some people just won't put in the work."
    u "But I am willing to go that extra mile..."
    u "...with you."
    show mathchan smile with dissolve
    m "I knew you would. I wish I had approached you sooner."
    u "The feeling is mutual."
    show mathchan blush with dissolve
    m "I've had the biggest crush on you since when we were both in primary school."
    m "You might not even recognise me from back then."

    menu:
        "I don't recognise you.":
            show mathchan sad with dissolve
            m "Oh. I don't blame you for not remembering me."
            m "I wasn't good at expressing or explaining myself back then."
        "I recognise you.":
            "I didn't even realise. Was that the same girl from all those years at school? How did I not realise?"
            u "OMG! Math Chan! How did I not remember you?"
            u "Wait? I'm suddenly feeling some deja vu."
            u "Have we been here before?"
            m "Yeah, a long time ago when we were younger..."
            u "I see."
            m "Maybe you just weren't ready then."

    show mathchan smile with dissolve
    m "Regardless..."
    m "We just have to take it slow and learn to walk before we can run."

    u "I'd like that."
    m "I'd like that too."

    m "Can we sit together in the lecture tomorrow?"
    u "Sure thing."
    u "I'll see you tomorrow. If you have any trouble with that algebra assignment just flick me a text, ok?"
    m "Hehe ok."
    "Math Chan begins a full revolution around to leave and stops..."
    m "One more thing."
    m "I like you. I see a long road ahead for us."
    "Math Chan wanders off towards Britomart Station."
    hide mathchan smile with fade
    "That didn't go quite as expected..."
    "...however, it has made me think that I wish I had put in more effort earlier."
    "I should've been at this point years ago! If only I wasn't so afraid of the unknown..."
    "...of failure..."
    "...and rejection."

    show black with fade
    stop music fadeout 1.5
    play music "tenderness.mp3" loop fadein 1.0

    "Over the coming semester Math Chan and I grew closer and closer."
    "Our relationship blossomed to greater heights than I had ever experienced or expected."
    "Then came the day were I finally asked her to be my coefficient."
    "Sure, some parts where rocky, but that is to be expected with every relationship."
    "But the power we share is exponential."
    "I've learnt that with time and patience every obstacle can be overcome."
    "You just have to put the effort in."
    "Thats the real solution."

    scene bg oggb with fade
    "Math Chan should be meeting me here before class."
    show mathchan smile
    m "Boo!"
    m "Haha gotcha!"
    m "We should probably head over to that lecture soon."
    u "Yeah! Totally! I finally think I'm starting to get it."
    m "Yay! Hehe."
    show mathchan blush with dissolve
    m "So how are you doing today baby? :3"

    menu:
        "Yeah, I'm good. Things are looking up. :)":
            m "Hehe. Good :3"
        "All the better now that you're here.":
            show mathchan uwu with dissolve
            m "uwu"

    m "You're mighty acute today ;)"
    m "[complement]."

    show black with fade

    "Math Chan leans in..."
    "...and gives me a soft peck on the cheek."

    "{b}The End{/b}"

    # This ends the game.

    return
