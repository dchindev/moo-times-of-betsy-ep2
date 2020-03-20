# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define betsy = Character("Betsy")
define mister = Character("Mister")
define missy = Character("Missy")
define evilbetsy = Character("Evil Betsy")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show betsy happy

    # These display lines of dialogue.

    betsy "There’s three things that I love more than anything in the world - my mister & missy, dairy free ice cream and shopping. "

    "Well...mister and missy does the shopping. I simply look at the items and make suggestions on what I want."

    "Ever since I’ve been adopted a few months ago, my life has been great."

    "Not only my owners are so loving, I get to do the one thing I’ve always wanted to do at a home:"

    "Sleep peacefully without interruption. I couldn’t do this when I was at the mall."

    "Oh? You thought I was going to say take over the world?"

    "That’s a nice thought. But I don’t think the world is ready for a talking plush animal."

    "Let alone a plush animal who does witchcraft."

    "You see, my mister and missy aren’t just regular folks. They also practice magick!"

    "My mister loves cooking meals at home. He likes to experiment with different herbs and spices to make the food tastier. "

    "No wonder why he’s the head chef at a local restaurant. I guess that’s part of his nature as a kitchen witch."

    "And my missy? Oh goodness, she’s a handful. And I mean it in an endearing way."

    "She spends her time creating visual novel games for clients who are looking to change their life for the better."

    "Think of it as a way of simulating an alternate reality but in a controlled environment."

    "Missy is after all, a tech witch. It’s what she does best."

    "And me? I’m more than just Missy’s familiar."

    "I create painting infused with magick! Sometimes, I like to add my tarot cards for that extra kick. I’m an art witch."

    "Together, we’re one happy witchy family. Despite our different paths, nothing can tear us apart."

    scene black

    "Not even my past."

    jump scene2
