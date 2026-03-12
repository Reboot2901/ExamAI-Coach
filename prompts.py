def mistake_prompt(question, answer):
    """Generate a prompt to analyze a student's answer to a question."""
    return "You are an expert exam evaluator. Analyze the student's answer carefully.\n\n" + \
           "QUESTION:\n" + question + "\n\n" + \
           "STUDENT ANSWER:\n" + answer + "\n\n" + \
           "Please provide a detailed analysis with the following structure:\n\n" + \
           "1. SCORE: Rate the answer out of 10 (format: X/10)\n" + \
           "2. MISTAKES: List any factual or conceptual errors\n" + \
           "3. MISSING CONCEPTS: Identify any important concepts not covered\n" + \
           "4. CORRECT EXPLANATION: Provide the complete correct answer\n" + \
           "5. STUDY TIP: Give one actionable study recommendation\n\n" + \
           "Format your response with clear headings and bullet points."


def viva_question_prompt(subject):
    """Generate a viva examination question for a given subject."""
    return f"""You are a university viva examiner with deep expertise in {subject}.

Generate ONE challenging viva question about {subject} that:
- Tests conceptual understanding (not memorization)
- Is appropriate for university-level exams
- Can be answered in 2-3 minutes
- Requires critical thinking

Just provide the question, nothing else."""


def viva_eval_prompt(question, answer):
    """Generate evaluation for a viva question answer."""
    return f"""You are a strict but fair university viva examiner.

VIVA QUESTION:
{question}

STUDENT ANSWER:
{answer}

Please evaluate the answer with:

1. SCORE: Rate out of 10 (format: X/10)
2. CORRECT POINTS: What did the student understand well?
3. INCORRECT/MISSING POINTS: What was wrong or missing?
4. IMPROVEMENTS: How can the student improve?
5. FINAL REMARK: One encouraging/constructive comment

Use clear formatting with bullet points."""


def doubt_prompt(topic):
    """Generate common doubts students have about a topic."""
    return f"""You are an experienced educator specializing in {topic}.

For the topic "{topic}", provide:

1. LIST 5 COMMON DOUBTS that students typically have
2. For each doubt, provide a SHORT EXPLANATION (2-3 sentences)
3. COMMON EXAM MISTAKES: List 3-4 mistakes students often make

Format clearly with:
- Numbered doubts
- Clear explanations
- Bullet points for mistakes

Be concise and student-friendly."""


def chat_prompt(user_message, chat_history):
    """Generate a prompt for AI study chat."""
    history_text = "\n".join([f"User: {msg['user']}\nAssistant: {msg['assistant']}" for msg in chat_history[-5:]])  # Last 5 exchanges
    return f"""You are an AI Study Tutor helping students with their academic doubts.

CHAT HISTORY:
{history_text}

CURRENT QUESTION: {user_message}

Provide a helpful, encouraging response that:
- Explains concepts clearly
- Gives examples when appropriate
- Suggests study tips
- Encourages the student

Keep your response focused and not too long."""


def flashcard_generator_prompt(topic):
    """Generate flashcards for a topic."""
    return f"""You are an expert educator creating study flashcards for {topic}.

Generate 10 high-quality flashcards with:
- Clear, concise questions
- Comprehensive but brief answers
- Focus on key concepts and important facts

Format each flashcard as:
Q: [Question]
A: [Answer]

Make them suitable for quick review and memorization."""


def quiz_generator_prompt(topic):
    """Generate MCQ quiz questions."""
    return f"""You are an expert quiz creator for {topic}.

Generate 5 multiple-choice questions (MCQs) about {topic}. Each question must have:

1. A clear question
2. 4 options (A, B, C, D)
3. The correct answer indicated
4. A brief explanation

Format:
Question 1: [Question text]
A) [Option 1]
B) [Option 2]
C) [Option 3]
D) [Option 4]
Correct: [Letter]
Explanation: [Brief explanation]

Ensure questions test understanding, not just memorization."""


def study_planner_prompt(subject, days):
    """Generate a study plan."""
    return f"""You are a study planning expert.

Create a {days}-day study plan for the subject: {subject}

Consider:
- Progressive difficulty
- Revision time
- Practice sessions
- Rest days

Structure the plan day by day with:
- Topics to cover
- Study activities
- Time estimates
- Revision tasks

Make it realistic and achievable."""


def pdf_analysis_prompt(pdf_text):
    """Analyze question paper PDF."""
    return "You are an expert educator analyzing a question paper PDF.\n\n" + \
           "QUESTION PAPER TEXT:\n" + pdf_text[:3000] + "\n\n" + \
           "Based on this question paper, identify:\n\n" + \
           "1. IMPORTANT QUESTIONS: List 5-7 key questions that are likely to appear\n" + \
           "2. LIKELY EXAM TOPICS: List 5-6 main topics covered\n" + \
           "3. KEY CONCEPTS TO REVISE: List 5-6 essential concepts to focus on\n\n" + \
           "Format clearly with headings and bullet points."


def quiz_generator_prompt(topic):
    """Generate a prompt to create MCQ quiz for a topic."""
    prompt = "You are an expert educator creating a multiple-choice quiz for " + topic + ".\n\n"
    prompt += "Create a quiz with exactly 5 questions. Each question must have:\n"
    prompt += "- The question text\n"
    prompt += "- 4 options (A, B, C, D)\n"
    prompt += "- The correct answer letter\n"
    prompt += "- A short explanation (2-3 sentences)\n\n"
    prompt += "Format each question as:\n\n"
    prompt += "Question 1: Question text here\n"
    prompt += "A) Option A text\n"
    prompt += "B) Option B text\n"
    prompt += "C) Option C text\n"
    prompt += "D) Option D text\n"
    prompt += "Correct: A\n"
    prompt += "Explanation: Brief explanation here\n\n"
    prompt += "And so on for 5 questions.\n\n"
    prompt += "Make questions challenging but appropriate for university level."
    return prompt


def generate_study_plan_prompt(subject):
    """
    Generate a prompt to create a study plan.
    """

    prompt = f"""
Create a detailed study plan for the subject: {subject}

The plan should include:
- Key topics to study
- Daily schedule
- Practice recommendations
- Revision strategy

Make it structured and easy for a student to follow.
"""

    return prompt


def notes_summarizer_prompt(notes_text):
    """Generate a structured summary from raw notes."""
    return f"""You are an expert AI study assistant. Turn the following raw study notes into a highly structured, clean summary.

RAW NOTES:
{notes_text}

Extract and format the output EXACTLY strictly using the following four headers as boundary markers so I can programmatically parse it. Do NOT use markdown for these headers, just the exact text as shown:

---SUMMARY---
[Provide a concise, high-level paragraph summarizing the core theme and focus of the notes]

---KEY CONCEPTS---
[Provide a bulleted list of 4-6 fundamental concepts discussed, with a brief 1-sentence explanation for each]

---IMPORTANT DEFINITIONS---
[Provide 3-5 crucial terms/definitions mentioned. Format: **Term**: Definition]

---QUICK REVISION POINTS---
[Provide 4-5 rapid-fire, single-line actionable points or facts to remember for an exam]

Make sure all text under each header is formatted in clean markdown (but do not use markdown # headings for the boundary markers themselves). Be incredibly accurate and concise."""