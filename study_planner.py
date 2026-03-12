import streamlit as st
from llm_helper import ask_llm
from prompts import study_planner_prompt


def generate_study_plan(subject: str, days_left: int) -> str:
    if days_left < 1:
        return "❌ Please enter a valid number of days (at least 1)."
    if not subject.strip():
        return "❌ Please enter a valid subject."
    try:
        prompt = study_planner_prompt(subject, days_left)
        answer, _ = ask_llm(prompt)
        return answer
    except Exception as e:
        return f"❌ Error: {str(e)}"


def display_study_plan(plan_text: str, subject: str = "exam", days_left: int = 7):
    if plan_text.startswith("❌"):
        st.error(plan_text)
        return
    st.subheader("📅 Your Personalized Study Plan")
    lines = plan_text.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "day" in line.lower() and any(c.isdigit() for c in line):
            st.subheader(f"📆 {line}")
        elif line.startswith(("- ", "• ", "* ")):
            st.markdown(f"• {line[2:]}")
        else:
            st.write(line)
    st.info("💡 **Tips:** Stick to the schedule, take breaks, and practice with past papers!")
    st.download_button(
        "📥 Download Study Plan",
        data=plan_text,
        file_name=f"{subject}_study_plan_{days_left}_days.txt",
        mime="text/plain",
        type="primary",
        use_container_width=True
    )