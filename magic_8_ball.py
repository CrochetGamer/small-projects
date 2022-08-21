import random


def magic_ball() -> str:
    """
    Ask this crabby Magic 8 Ball a question out loud
    and run to see the answer.

    :return: `str`, a random answer.
    """

    # Possible responses that the Magic 8 Ball can give
    responses = ["Don't ask me!", "Next question, loser.",
                 "Go away.", "I've had enough of your questions.",
                 "Maybe you should ask your Mom that question.",
                 "Does that topic really concern me?", "You talk a lot, so no.",
                 "What? Sorry, I wasn't listening.",
                 "The answer is: You should see a therapist.",
                 "Wow, you've got more problems than a math book!",
                 "Hmmn...bring me cookies and I might answer.",
                 "Yes! I mean no! I can't decide...", "Nope.",
                 "Sure, I guess.", "You woke me up to ask that?!",
                 "I should ask you the same question.", "I don't think so.",
                 "How should I know?", "Maybe yes, maybe no.",
                 "Look inside yourself.", "That is a definite yes...I think.",
                 "I'm tired, ask again when I care.", "Ugh...this question again?",
                 "My sixth sense says....no.", "Magically yes!",
                 "I'm in a good mood so I'll say yes.",
                 "What is this, twenty questions?"]

    answer = random.choice(responses)
    return answer


print(magic_ball())