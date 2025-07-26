# story_data.py

# --- Story Segments ---
# Each key in the STORY_CONTENT dictionary represents a unique point in the story.
# The value is a list of strings, where each string is a line of dialogue/narration.

STORY_CONTENT = {
    "prologue_start": [
        "Human and demon can't coexist. That is one rule that is bound in this world.",
        "However, there is a young couple who defies that law. Bound by forbidden love, they eloped to a secluded village.",
        "Though the village was unsettled with their arrival, they still lived happily and even had a child whose very existence defied the rule of their world."
    ],
    "yvonne_childhood": [
        "The child's name was Yvonne. She had black hair and purple eyes like her father, and a face that resembled her mother.",
        "The child was born half human and half demon. They accepted her for who she was, believing that she wasn't a mistake or an anomaly, but a proof of their eternal love.",
        "And thus, several years later, Yvonne is 6 years old.",
        "Yvonne is a cheerful and energetic girl. However, her existence itself was a taboo. Born as half human and demon from the legacy of a love the world refused to accept, the other children kept their distance toward her.",
        "\"Look at her, my mother said she was a cursed child who brings misfortune to this village.\" Said the first boy.",
        "\"That's true! My mother said so, she was born half human and demon.\" Said the first girl.",
        "\"That's terrifying! Why would she be here, playing like she's one of us?\" Said the second girl.",
        "The second boy said. \"Don't come near us, demon girl! She doesn't belong here\". He picked up a stone and hurled toward her. It struck her head, making her bleed.",
        "\"Please stop it!\" Yvonne cried. \"I didn't do anything!\"",
        "The children ignored her words. \"Go back where you belong, you monster!\" shouted the children, and they threw another stone towards her.",
        "Filled with sadness and pain, Yvonne ran toward her home.",
        "Her mother noticed Yvonne crying. \"I'm sorry mom, I didn't do anything but the children hated me and threw stones toward me,\" said Yvonne while crying.",
        "Her mother knelt and gently wiped the blood from Yvonne's forehead.",
        "\"My poor sweetheart,\" she whispered, hugging Yvonne in her arms. \"You've done nothing wrong. People fear what they don't understand. You are not a mistake but a miracle for us\".",
        "Yvonne’s sobs faded as her mother’s gentle words and warm embrace wrapped her in comfort."
    ],
    "village_turns": [
        "Several months later. The season turned harsh, crops failed, many livestock died, and thus a strange sickness spread across the village.",
        "The villagers whispered that this crop failure and strange sickness were the cause of Yvonne's family.",
        "And thus the villagers began to accuse Yvonne's family of bringing this misfortune to the village.",
        "\"They brought this,\" spat one villager. \"They are bringing misfortune toward our village! We must take out their family!\" Fear boiled into their hatred.",
        "At night, the villagers gathered together and stormed toward Yvonne's home with torches and makeshift weapons.",
        "Inside, Yvonne awoke from sleep, her eyes wide with dread. Her mother rushed to her side and pulled her close. \"Shh... it's okay sweetheart, everything's going to be okay. Let your father handle this matter.\"",
        "Her father went outside the house and stood in front of the crowd. \"What's the ruckus of all this? Why are you gathering around my house with the torches and weapons?\" said Yvonne's father with a fierce look.",
        "One of the men stepped forward. \"You brought ruin upon us! Your family is tainting this land. Demon and human can't coexist, and thus such famine and illness are spread across our village!\" shouted the man angrily.",
        "Another voice shouted, “The war blocks our food. Demons mark our fields. And you brought the spawn of their kind!”",
        "Their cries grew louder, losing reason with each word. The mob surged forward."
    ],
    "attack_and_awakening": [
        "Realizing reason had failed, the father bolted back inside. “We have to go, now!”",
        "He grabbed Yvonne, his wife weaving her hands in ancient patterns. Magic pulsed from her fingers, forming a protective veil, a shimmering dome of violet light.",
        "The villagers struck the barrier with blades and stones. The mother’s breath grew shallow, her strength waning.",
        "“I won't hurt them,” she whispered to her husband. “No matter what they do. That’s not who I am.”",
        "A crack split through her shield. Then another. The dome shattered like glass.",
        "She lunged forward, forming one last spell, but it was too late, spears pierced her side. She collapsed at the doorstep, gasping, reaching out toward Yvonne.",
        "“Run... Yvonne... please... live,” she murmured, eyes fading like stars.",
        "Yvonne stood frozen, watching her world burn.",
        "Her father's voice called out, trying to reach her, but everything was distant now. He was slashed by the sword. Meanwhile, her mother lay broken. Her home was ablaze.",
        "She couldn’t scream. She couldn’t move. Then, a voice—faint, echoing—rose from deep within her. “Poor child. Let me deal with this.”",
        "Something inside Yvonne snapped open. Her breath turned icy. Her eyes glowed red. Her hair changed into white.",
        "Another presence emerged—darker, colder. A second version of Yvonne stood in her place. This form didn't cry, instead, bloodlust overflowed.",
        "The demon blood awakened.",
        "The ground cracked. Shadows swallowed light. The villagers—screaming—were torn apart by the surge of demonic power that had laid dormant until now.",
        "By sunrise, nothing remained of the village but scorched earth and ash."
    ]
}

# --- Story Flow Map ---
# Defines the sequence of story segments.
# The value is the key for the next segment.
# "END" signifies the end of the story for this version.

STORY_FLOW = {
    "prologue_start": "yvonne_childhood",
    "yvonne_childhood": "village_turns",
    "village_turns": "attack_and_awakening",
    "attack_and_awakening": "END" # This marks the end of the current story content
}

