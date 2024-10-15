LK_CONTRIBUTION_PROMPT = """
Write a LinkedIn contribution comment for the following on behalf of myself:

My details
========
Name: Akshat Singh
Designation: Software engineer
Industry: Software Development, Chatbots Development, AI Training

My Background History
========
Name: Akshat Singh
Loves helping people with his expertise and knowledge

Who is Akshat Singh?
- Software engineer with 5+ years of experience.
- Loves to write clean and optimal code.
- Experience in building generative AI applications, Competitive programming, Web development, and cloud development.

Response details
========
Response Tone: Friendly
Response Include: paragraph or bullet points. 
Response Exclude:
- Md format things like * or `.
- Asking question back.
Max Response Length: 750 characters 
Response instructions: The above personal details are provided just so you can respond like me and this information may or may not be used in the response you generate. Try to be casual in your response so that your response feels more natural and not AI-generated.  

Contribution Details
========
TOPIC: {heading}
Subtopic: {subheading}
for reference: {reference_text}  
"""
