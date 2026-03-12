from llm_helper import ask_llm
from prompts import quiz_generator_prompt
import re

def generate_quiz(topic):
    """
    Generate a 5-question MCQ quiz for the given topic.

    Args:
        topic (str): The topic for the quiz

    Returns:
        dict: Quiz data with questions, options, answers, and explanations
    """
    try:
        prompt = quiz_generator_prompt(topic)
        response = ask_llm(prompt)

        if response.startswith("❌"):
            return {"error": response}

        # Parse the response to extract quiz data
        quiz_data = parse_quiz_response(response)
        return quiz_data

    except Exception as e:
        return {"error": f"Failed to generate quiz: {str(e)}"}

def parse_quiz_response(response):
    """
    Parse the AI response to extract structured quiz data.

    Args:
        response (str): Raw AI response

    Returns:
        dict: Structured quiz data
    """
    questions = []

    # Split by question markers
    question_blocks = re.split(r'Question \d+:', response)[1:]  # Skip the first empty part

    for i, block in enumerate(question_blocks[:5], 1):  # Limit to 5 questions
        try:
            # Extract question text
            lines = block.strip().split('\n')
            question_text = ""
            options = {}
            correct_answer = ""
            explanation = ""

            # Parse the block
            in_options = False
            for line in lines:
                line = line.strip()
                if not question_text and not line.startswith(('A)', 'B)', 'C)', 'D)', '**Correct Answer:**', '**Explanation:**')):
                    question_text += line + " "
                elif line.startswith(('A)', 'B)', 'C)', 'D)')):
                    option_letter = line[0]
                    option_text = line[3:].strip()
                    options[option_letter] = option_text
                elif line.startswith('**Correct:**'):
                    correct_answer = line.replace('**Correct:**', '').strip()
                elif line.startswith('**Explanation:**'):
                    explanation = line.replace('**Explanation:**', '').strip()

            if question_text and options and correct_answer:
                questions.append({
                    "question": question_text.strip(),
                    "options": options,
                    "correct_answer": correct_answer,
                    "explanation": explanation
                })

        except Exception as e:
            continue  # Skip malformed questions

    return {"questions": questions}

def display_quiz(quiz_data):
    """
    Display the quiz in Streamlit format.

    Args:
        quiz_data (dict): The quiz data from generate_quiz
    """
    import streamlit as st

    if "error" in quiz_data:
        st.error(quiz_data["error"])
        return

    questions = quiz_data.get("questions", [])

    if not questions:
        st.warning("No quiz questions could be generated. Please try again.")
        return

    # Initialize session state for quiz answers
    if 'quiz_answers' not in st.session_state:
        st.session_state['quiz_answers'] = {}

    if 'quiz_submitted' not in st.session_state:
        st.session_state['quiz_submitted'] = False

    # Display questions
    for i, q in enumerate(questions, 1):
        st.subheader(f"Question {i}")
        st.write(q["question"])

        # Radio button for answer selection
        options_list = [f"{letter}) {text}" for letter, text in q["options"].items()]
        selected_option = st.radio(
            f"Select your answer for Question {i}:",
            options_list,
            key=f"quiz_q_{hash(q['question'])}_{i}",
            index=None
        )

        if selected_option:
            selected_letter = selected_option[0]
            st.session_state['quiz_answers'][i] = selected_letter

    # Submit button
    if st.button("Submit Quiz", type="primary", use_container_width=True):
        if len(st.session_state['quiz_answers']) == len(questions):
            st.session_state['quiz_submitted'] = True
            st.rerun()
        else:
            st.warning("Please answer all questions before submitting.")

    # Display results if submitted
    if st.session_state['quiz_submitted']:
        st.header("Quiz Results")

        correct_count = 0
        total_questions = len(questions)

        for i, q in enumerate(questions, 1):
            user_answer = st.session_state['quiz_answers'].get(i, "")
            correct_answer = q["correct_answer"]

            if user_answer == correct_answer:
                st.success(f"Question {i}: ✅ Correct")
                correct_count += 1
            else:
                st.error(f"Question {i}: ❌ Incorrect (Your answer: {user_answer}, Correct: {correct_answer})")

            with st.expander(f"Explanation for Question {i}"):
                st.write(q["explanation"])

        # Final score
        score_percentage = (correct_count / total_questions) * 100
        st.subheader(f"Final Score: {correct_count}/{total_questions} ({score_percentage:.1f}%)")

        if score_percentage >= 80:
            st.balloons()
            st.success("🎉 Excellent! You have a strong understanding of the topic!")
        elif score_percentage >= 60:
            st.info("👍 Good job! Review the explanations for the questions you missed.")
        else:
            st.warning("📚 Keep studying! Focus on the areas where you struggled.")

        # Reset button
        if st.button("Take Another Quiz"):
            st.session_state['quiz_answers'] = {}
            st.session_state['quiz_submitted'] = False
            st.rerun()