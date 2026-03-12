import streamlit as st
import re
from llm_helper import ask_llm
from prompts import quiz_generator_prompt


def generate_quiz(topic: str) -> dict:
    try:
        prompt = quiz_generator_prompt(topic)
        response, _ = ask_llm(prompt)
        if response.startswith("❌") or response.startswith("⚠️"):
            return {"error": response}
        return parse_quiz_response(response)
    except Exception as e:
        return {"error": f"Failed to generate quiz: {str(e)}"}


def parse_quiz_response(response: str) -> dict:
    questions = []
    blocks = re.split(r"Question \d+:", response)[1:]
    for i, block in enumerate(blocks[:5], 1):
        try:
            lines = block.strip().split("\n")
            question_text, options, correct_answer, explanation = "", {}, "", ""
            for line in lines:
                line = line.strip()
                if line.startswith(("A)", "B)", "C)", "D)")):
                    options[line[0]] = line[3:].strip()
                elif line.lower().startswith("correct:"):
                    correct_answer = line.split(":", 1)[1].strip()
                elif line.lower().startswith("explanation:"):
                    explanation = line.split(":", 1)[1].strip()
                elif not line.startswith(("A)", "B)", "C)", "D)")) and not question_text:
                    question_text += line + " "
            if question_text and options and correct_answer:
                questions.append({
                    "question": question_text.strip(),
                    "options": options,
                    "correct_answer": correct_answer,
                    "explanation": explanation
                })
        except Exception:
            continue
    return {"questions": questions}


def display_quiz(quiz_data: dict):
    if "error" in quiz_data:
        st.error(quiz_data["error"])
        return
    questions = quiz_data.get("questions", [])
    if not questions:
        st.warning("No quiz questions could be generated. Please try again.")
        return

    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = {}
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    for i, q in enumerate(questions, 1):
        st.subheader(f"Question {i}")
        st.write(q["question"])
        options_list = [f"{letter}) {text}" for letter, text in q["options"].items()]
        selected = st.radio(f"Select answer {i}:", options_list, key=f"quiz_q_{i}", index=None)
        if selected:
            st.session_state.quiz_answers[i] = selected[0]

    if st.button("Submit Quiz", type="primary", use_container_width=True):
        if len(st.session_state.quiz_answers) == len(questions):
            st.session_state.quiz_submitted = True
            st.rerun()
        else:
            st.warning("Please answer all questions before submitting.")

    if st.session_state.quiz_submitted:
        st.header("🏆 Quiz Results")
        correct_count = 0
        for i, q in enumerate(questions, 1):
            user_ans = st.session_state.quiz_answers.get(i, "")
            if user_ans == q["correct_answer"]:
                st.success(f"Question {i}: ✅ Correct!")
                correct_count += 1
            else:
                st.error(f"Question {i}: ❌ Wrong (Yours: {user_ans}, Correct: {q['correct_answer']})")
            with st.expander(f"Explanation for Q{i}"):
                st.write(q["explanation"])

        pct = (correct_count / len(questions)) * 100
        st.subheader(f"Final Score: {correct_count}/{len(questions)} ({pct:.1f}%)")
        if pct >= 80:
            st.balloons()
            st.success("🎉 Excellent work!")
        elif pct >= 60:
            st.info("👍 Good effort! Review the explanations above.")
        else:
            st.warning("📚 Keep studying! Check the explanations to improve.")

        if st.button("🔄 Take Another Quiz"):
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
            st.rerun()