"""
prompts.py — Centralized prompt functions for all ExamAI-Coach features.
"""


def mistake_prompt(question: str, student_answer: str) -> str:
    return f"""You are an expert exam evaluator. Analyze the student's answer carefully.

QUESTION:
{question}

STUDENT ANSWER:
{student_answer}

Provide a detailed analysis with:
1. SCORE: Rate the answer out of 10 (format: X/10)
2. MISTAKES: List any factual or conceptual errors
3. MISSING CONCEPTS: Identify any important concepts not covered
4. CORRECT EXPLANATION: Provide the complete correct answer
5. STUDY TIP: Give one actionable study recommendation

Format your response with clear headings and bullet points."""


def chat_prompt(user_message: str, chat_history: list) -> str:
    history_text = ""
    for msg in chat_history[-5:]:
        history_text += f"User: {msg.get('user', '')}\nAssistant: {msg.get('assistant', '')}\n"
    return f"""You are an AI Study Tutor helping students with their academic doubts.

RECENT CONVERSATION:
{history_text}

CURRENT QUESTION: {user_message}

Provide a helpful, encouraging response that:
- Explains concepts clearly
- Gives examples when appropriate
- Suggests study tips
- Encourages the student

Keep your response focused and not too long."""


def viva_question_prompt(subject: str) -> str:
    return f"""You are a university viva examiner with deep expertise in {subject}.

Generate ONE challenging viva question about {subject} that:
- Tests conceptual understanding (not memorization)
- Is appropriate for university-level exams
- Can be answered in 2-3 minutes
- Requires critical thinking

Just provide the question, nothing else."""


def viva_eval_prompt(question: str, answer: str) -> str:
    return f"""You are a strict but fair university viva examiner.

VIVA QUESTION:
{question}

STUDENT ANSWER:
{answer}

Evaluate the answer with:
1. SCORE: Rate out of 10 (format: X/10)
2. CORRECT POINTS: What did the student understand well?
3. INCORRECT/MISSING POINTS: What was wrong or missing?
4. IMPROVEMENTS: How can the student improve?
5. FINAL REMARK: One encouraging/constructive comment

Use clear formatting with bullet points."""


def doubt_prompt(topic: str) -> str:
    return f"""You are an experienced educator specializing in {topic}.

For the topic "{topic}", provide:
1. LIST 5 COMMON DOUBTS that students typically have
2. For each doubt, provide a SHORT EXPLANATION (2-3 sentences)
3. COMMON EXAM MISTAKES: List 3-4 mistakes students often make

Format clearly with numbered doubts, clear explanations, and bullet points for mistakes.
Be concise and student-friendly."""


def flashcard_generator_prompt(topic: str) -> str:
    return f"""You are an expert educator creating study flashcards for {topic}.

Generate 10 high-quality flashcards with clear, concise questions and comprehensive but brief answers.
Focus on key concepts and important facts.

Format each flashcard EXACTLY as:
Q: [Question here]
A: [Answer here]

Make them suitable for quick review and memorization."""


def quiz_generator_prompt(topic: str) -> str:
    return f"""You are an expert quiz creator for {topic}.

Generate 5 multiple-choice questions (MCQs) about {topic}. Each question must have:
1. A clear question
2. 4 options (A, B, C, D)
3. The correct answer indicated
4. A brief explanation

Format EXACTLY as:
Question 1: [Question text]
A) [Option 1]
B) [Option 2]
C) [Option 3]
D) [Option 4]
Correct: [Letter]
Explanation: [Brief explanation]

Ensure questions test understanding, not just memorization."""


def study_planner_prompt(subject: str, days: int) -> str:
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


def pdf_analysis_prompt(pdf_text: str) -> str:
    truncated = pdf_text[:3000]
    return f"""You are an expert educator analyzing a question paper PDF.

QUESTION PAPER TEXT:
{truncated}

Based on this question paper, identify:
1. IMPORTANT QUESTIONS: List 5-7 key questions that are likely to appear
2. LIKELY EXAM TOPICS: List 5-6 main topics covered
3. KEY CONCEPTS TO REVISE: List 5-6 essential concepts to focus on

Format clearly with headings and bullet points."""


def notes_summarizer_prompt(notes_text: str) -> str:
    return f"""You are an expert AI study assistant. Turn the following raw study notes into a highly structured, clean summary.

RAW NOTES:
{notes_text}

Extract and format the output EXACTLY using the following four headers as boundary markers:

---SUMMARY---
[Provide a concise, high-level paragraph summarizing the core theme and focus of the notes]

---KEY CONCEPTS---
[Provide a bulleted list of 4-6 fundamental concepts discussed, with a brief 1-sentence explanation for each]

---IMPORTANT DEFINITIONS---
[Provide 3-5 crucial terms/definitions mentioned. Format: **Term**: Definition]

---QUICK REVISION POINTS---
[Provide 4-5 rapid-fire, single-line actionable points or facts to remember for an exam]

Make sure all text under each header is formatted in clean markdown. Be incredibly accurate and concise."""


def generate_study_plan_prompt(subject: str) -> str:
    return f"""Create a detailed study plan for the subject: {subject}

The plan should include:
- Key topics to study
- Daily schedule
- Practice recommendations
- Revision strategy

Make it structured and easy for a student to follow."""