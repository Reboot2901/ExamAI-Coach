import streamlit as st
from datetime import datetime

def init_user_data():
    """Initialize user data in session state"""
    if "user_data" not in st.session_state:
        st.session_state.user_data = {}

def get_user_data(user_id):
    """Get user data"""
    init_user_data()
    if user_id not in st.session_state.user_data:
        st.session_state.user_data[user_id] = {
            "mistakes": [],
            "viva_history": [],
            "chat_history": [],
            "quiz_scores": [],
            "pdf_analyses": []
        }
    return st.session_state.user_data[user_id]

def save_mistake_analysis(user_id, question, student_answer, ai_feedback, score):
    """Save mistake analysis"""
    data = get_user_data(user_id)
    data["mistakes"].append({
        "question": question,
        "student_answer": student_answer,
        "ai_feedback": ai_feedback,
        "score": score,
        "date": datetime.now().isoformat()
    })

def save_viva_attempt(user_id, subject, question, student_answer, evaluation):
    """Save viva attempt"""
    data = get_user_data(user_id)
    data["viva_history"].append({
        "subject": subject,
        "question": question,
        "student_answer": student_answer,
        "evaluation": evaluation,
        "date": datetime.now().isoformat()
    })

def save_chat_message(user_id, role, message):
    """Save chat message"""
    data = get_user_data(user_id)
    data["chat_history"].append({
        "role": role,
        "message": message,
        "date": datetime.now().isoformat()
    })

def save_quiz_score(user_id, topic, score, total_questions):
    """Save quiz score"""
    data = get_user_data(user_id)
    data["quiz_scores"].append({
        "topic": topic,
        "score": score,
        "total": total_questions,
        "date": datetime.now().isoformat()
    })

def save_pdf_analysis(user_id, filename, analysis):
    """Save PDF analysis"""
    data = get_user_data(user_id)
    data["pdf_analyses"].append({
        "filename": filename,
        "analysis": analysis,
        "date": datetime.now().isoformat()
    })

def get_user_stats(user_id):
    """Get user statistics"""
    data = get_user_data(user_id)
    return {
        "total_mistakes": len(data["mistakes"]),
        "total_vivas": len(data["viva_history"]),
        "total_chats": len(data["chat_history"]),
        "total_quizzes": len(data["quiz_scores"]),
        "total_pdfs": len(data["pdf_analyses"]),
        "avg_quiz_score": sum([q["score"] / q["total"] for q in data["quiz_scores"]]) / len(data["quiz_scores"]) if data["quiz_scores"] else 0
    }