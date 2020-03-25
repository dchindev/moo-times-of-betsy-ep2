# Moo Times of Betsy Episode 2
# Created during NaNoRenO 2020
# Developed by Diana Chin. All Rights Reserved.

define betsy = Character("Betsy", image ="betsy", window_left_padding=100)
define mister = Character("Mister")
define missy = Character("Missy")
define evilbetsy = Character("Evil Betsy")
define betsynoside = Character("Betsy")

image side betsy happy = "betsy_happy.PNG"
image side betsy content = "betsy_content.PNG"
image side betsy sad = "betsy_sad.PNG"
image side betsy angry = "betsy_angry.PNG"
image side betsy shock = "betsy_shock.PNG"


label start:


    scene bg

    betsy happy "There’s three things that I love more than anything in the world - my mister & missy, dairy free ice cream and shopping. "

    betsy happy "Well...mister and missy does the shopping. I simply look at the items and make suggestions on what I want."

    betsy happy "Ever since I’ve been adopted a few months ago, my life has been great."

    betsy happy "Not only my owners are so loving, I get to do the one thing I’ve always wanted to do at a home:"

    betsy content "Sleep peacefully without interruption. I couldn’t do this when I was at the mall."

    betsy shock "Oh? You thought I was going to say take over the world?"

    betsy content "That’s a nice thought. But I don’t think the world is ready for a talking plush animal."

    betsy content "Let alone a plush animal who does witchcraft."

    betsy happy "You see, my mister and missy aren’t just regular folks. They also practice magick!"

    scene mister_intro
    with dissolve

    betsynoside "My mister loves cooking meals at home. He likes to experiment with different herbs and spices to make the food tastier. "

    betsynoside "No wonder why he’s the head chef at a local restaurant. I guess that’s part of his nature as a kitchen witch."

    scene missy_intro
    with dissolve

    betsynoside "And my missy? Oh goodness, she’s a handful. And I mean it in an endearing way."

    betsynoside "She spends her time creating visual novel games for clients who are looking to change their life for the better."

    betsynoside "Think of it as a way of simulating an alternate reality but in a controlled environment."

    betsynoside "Missy is after all, a tech witch. It’s what she does best."

    scene betsy_intro
    with dissolve

    betsynoside "And me? I’m more than just Missy’s familiar."

    betsynoside "I create painting infused with magick! Sometimes, I like to add my tarot cards for that extra kick. I’m an art witch."

    scene betsyfamily01
    with dissolve

    betsynoside "Together, we’re one happy witchy family. Despite our different paths, nothing can tear us apart."

    scene black
    with fade

    betsynoside "Not even my past."

    jump scene2
