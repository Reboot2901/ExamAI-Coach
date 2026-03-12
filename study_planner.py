from llm_helper import ask_llm
from prompts import study_planner_prompt

def generate_study_plan(subject, days_left):
    """
    Generate a personalized study plan for exam preparation.

    Args:
        subject (str): The subject for the exam
        days_left (int): Number of days until the exam

    Returns:
        str: The generated study plan
    """
    try:
        if days_left < 1:
            return "❌ Error: Please enter a valid number of days (at least 1)."

        if not subject.strip():
            return "❌ Error: Please enter a valid subject."

        prompt = study_planner_prompt(subject, days_left)
        response = ask_llm(prompt)

        if response.startswith("❌"):
            return response

        return response

    except Exception as e:
        return f"❌ Error: Failed to generate study plan: {str(e)}"

def display_study_plan(plan_text, subject="exam", days_left=7):
    """
    Display the study plan in a formatted way.

    Args:
        plan_text (str): The raw study plan text from AI
    """
    import streamlit as st

    if plan_text.startswith("❌"):
        st.error(plan_text)
        return

    st.subheader("📅 Your Personalized Study Plan")

    # Try to format the plan with better structure
    lines = plan_text.split('\n')
    current_day = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check if it's a day header
        if line.lower().startswith(('day ', 'day-', 'day:')) or 'day' in line.lower() and any(char.isdigit() for char in line):
            if current_day:
                pass # removed spacer
            st.subheader(f"📆 {line}")
            current_day = line
        elif line.startswith(('- ', '• ', '* ')):
            st.markdown(f"• {line[2:]}")
        elif line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
            st.write(line)
        else:
            st.write(line)

    # Add encouragement
    st.info("💡 **Tips for Success:**\n- Stick to the schedule but be flexible\n- Take regular breaks to avoid burnout\n- Get adequate sleep and nutrition\n- Review previous days' material\n- Practice with past papers when possible\n- Stay positive and consistent!")

    # Download button for the plan
    st.download_button(
        label="📥 Download Study Plan",
        data=plan_text,
        file_name=f"{subject}_study_plan_{days_left}_days.txt",
        mime="text/plain",
        type="primary",
        use_container_width=True
    )