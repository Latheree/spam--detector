"""Small labelled dataset. Add your own messages to make the model smarter."""

SPAM = [
    "Congratulations! You won a free iPhone. Click this link to claim now",
    "URGENT: your bank account is blocked. Verify your details immediately",
    "Win cash prizes today only. Reply YES to enter the lucky draw",
    "Get a loan approved in 5 minutes with no documents. Apply now",
    "You have been selected for a free gift card. Claim before midnight",
    "Earn 50000 rupees per week from home. No experience needed",
    "Limited offer! Buy one get three free. Click here to order",
    "Your account will be suspended. Update your password at this link",
    "Free recharge for 3 months. Click the link to get your reward",
    "Claim your lottery prize of 10 lakh now. Send your bank details",
    "Hot deal: 90 percent discount on all products, offer ends tonight",
    "Dear customer, your KYC has expired. Update now to avoid blocking",
    "Make money fast with this secret trick. Join now and earn daily",
    "You are the lucky winner of a free vacation. Call now to claim",
    "Exclusive offer just for you. Click to get a free credit card today",
    "Final notice: pay the pending fee now or your service will be cut",
    "Cheap medicines without prescription. Order now and save big",
    "Double your money in 7 days guaranteed. Invest today",
    "Free entry to win a car. Text WIN to 5000 now",
    "Your parcel is held. Pay the delivery fee at this link to release it",
]

HAM = [
    "Hey, are you coming to class tomorrow morning?",
    "Can you send me the notes from yesterday's lecture?",
    "Mom said dinner will be ready at eight tonight",
    "The lab submission deadline is Friday at 5 pm",
    "Let's meet at the library after the exam to study together",
    "Happy birthday! Hope you have a wonderful day",
    "I will call you in the evening after I reach home",
    "Did you finish the Python assignment? I am stuck on loops",
    "The professor moved the test to next Monday",
    "Thanks for helping me with the project yesterday",
    "Are we still going to the gym this evening?",
    "Please bring your ID card for the seminar tomorrow",
    "I reached the hostel safely, don't worry",
    "Can we discuss the group project after lunch?",
    "The bus is running ten minutes late today",
    "Good luck for your interview, you will do great",
    "Remember to submit the fee receipt to the office",
    "What time does the movie start on Saturday?",
    "I left my charger in your room, can you keep it?",
    "The meeting is at 3 pm in room 204, see you there",
]

MESSAGES = SPAM + HAM
LABELS = ["spam"] * len(SPAM) + ["not spam"] * len(HAM)
