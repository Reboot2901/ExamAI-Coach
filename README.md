# 🎓 ExamAI Coach

A comprehensive AI-powered EdTech platform for exam preparation using local Ollama models.

## Setup Instructions

1. **Install Ollama**
   - Download from https://ollama.ai/download
   - Install the application

2. **Pull the llama3 model**
   ```
   ollama pull llama3
   ```

3. **Get Gemini API Key (Optional but recommended for Real-Time Google Search Grounding)**
   - Get a free API key at https://aistudio.google.com/
   - Create a `.env` file in the root directory (you can copy `.env.example`).
   - Add your key: `GEMINI_API_KEY=your_key_here`

4. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```
   streamlit run app.py
   ```

## Features

- **Dashboard**: Welcome message, study tools, recent activity, progress charts
- **Mistake Explainer**: Analyze answers with scores and feedback
- **Viva Examiner**: Practice viva questions with evaluation
- **Doubt Predictor**: Common doubts and mistakes for topics
- **AI Tutor Chat**: Interactive chat with AI tutor
- **Flashcard Generator**: Generate Q&A flashcards
- **Quiz Generator**: MCQ quizzes with explanations
- **Study Planner**: Personalized study plans
- **PDF Analyzer**: Analyze question papers for key topics

## Demo Credentials

- **Student**: student@example.com / password123
- **Admin**: admin@example.com / admin123

## Requirements

- Python 3.8+
- Ollama with llama3 model
- Streamlit
- requests
- pypdf

### 6. 📝 AI Quiz Generator
- Enter any topic to generate a quiz
- Creates **5 MCQ questions** with 4 options each
- Provides **correct answers** and **explanations**
- Interactive quiz interface with scoring

### 7. 📅 Study Planner Generator
- Input subject and days until exam
- Generates **personalized study plans**
- Day-wise breakdown with topics and activities
- Includes study tips and best practices

## 🛠️ Tech Stack

- **Frontend**: Streamlit (modern, responsive web UI)
- **LLM**: Ollama with llama3 model (local & private)
- **Search**: Gemini API with Google Search Grounding (real-time web integration)
- **PDF Processing**: PyPDF for text extraction
- **Language**: Python 3.8+
- **API**: Ollama REST API

## 📋 Prerequisites

Before running the application, ensure you have:

1. **Python 3.8 or higher** installed
   - [Download Python](https://www.python.org/downloads/)
   - Add to PATH during installation

2. **Ollama installed and running**
   - [Download Ollama](https://ollama.ai)
   - Install for your operating system

## 🚀 Installation & Setup

### Step 1: Install Ollama

Download and install Ollama from [https://ollama.ai](https://ollama.ai)

### Step 2: Pull the llama3 Model

Open terminal/command prompt and run:

```bash
ollama pull llama3
```

This downloads the llama3 model (~4-5 GB). One-time setup.

### Step 3: Start Ollama Server

Run Ollama in terminal:

```bash
ollama serve
```

Server runs on `http://localhost:11434`. Keep this terminal open.

### Step 4: Install Python Dependencies

Navigate to project folder:

```bash
cd path/to/ExamAI-Coach
```

Install requirements:

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

App opens at `http://localhost:8501`

## 📖 How to Use

### Mistake Explainer
1. Go to **Mistake Explainer** tab
2. Paste question and your answer
3. Click "Analyze Answer"
4. Review AI feedback and score

### Viva Examiner
1. Select subject from dropdown
2. Click "Generate Question"
3. Answer the viva question
4. Click "Evaluate Answer" for feedback
5. View history in sidebar

### Doubt Predictor
1. Enter a topic
2. Click "Predict Doubts"
3. Study common doubts and mistakes

### AI Study Chat
1. Go to **AI Study Chat** tab
2. Type your question in chat input
3. Get AI tutor responses
4. History saved in sidebar

### Upload Question Paper
1. Upload PDF in **Upload Question Paper** tab
2. Click "Analyze Question Paper"
3. Review key topics and questions

### AI Quiz Generator
1. Enter a topic in **AI Quiz Generator** tab
2. Click "Generate Quiz"
3. Answer the MCQs and submit
4. Review your score and explanations

### Study Planner Generator
1. Enter subject and days left in **Study Planner** tab
2. Click "Generate Study Plan"
3. Follow the personalized schedule
4. Download the plan if needed

## 📁 Project Structure

```
ExamAI-Coach/
├── app.py              # Main Streamlit application
├── llm_helper.py       # Ollama API integration
├── prompts.py          # AI prompt templates
├── pdf_helper.py       # PDF text extraction
├── quiz_generator.py   # MCQ quiz generation logic
├── study_planner.py    # Study plan generation
├── ui_styles.py        # Custom UI styles and helpers
├── requirements.txt    # Python dependencies
└── README.md          # This documentation
```

### File Descriptions

- **app.py**: Complete application with all 7 features, tabs, and sidebar
- **llm_helper.py**: Handles communication with Ollama API
- **prompts.py**: Optimized prompts for each AI feature
- **pdf_helper.py**: PDF processing using PyPDF
- **quiz_generator.py**: MCQ quiz generation and display logic
- **study_planner.py**: Study plan generation and formatting
- **ui_styles.py**: Custom CSS and UI helper functions
- **requirements.txt**: All Python package dependencies

## ⚙️ Configuration

### Ollama Settings

App connects to Ollama at `http://localhost:11434`. To change:

Edit `llm_helper.py`:

```python
OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Change if needed
MODEL_NAME = "llama3"  # Change model if needed
```

### Changing LLM Model

1. Pull new model: `ollama pull model_name`
2. Update `MODEL_NAME` in `llm_helper.py`

Popular models: `llama2`, `mistral`, `neural-chat`

## 🐛 Troubleshooting

### "Ollama not running" Error
- ✅ Ensure `ollama serve` is running
- ✅ Check `http://localhost:11434` accessible
- ✅ Restart Ollama if needed

### "Model not found" Error
- ✅ Run `ollama pull llama3`
- ✅ Wait for download completion

### PDF Upload Issues
- ✅ Ensure PDF is not password-protected
- ✅ Check file size (large PDFs may take time)

### Slow Responses
- ✅ Normal for first use
- ✅ Ensure 8GB+ RAM
- ✅ Close other applications

### Dependencies Issues
- ✅ Upgrade pip: `python -m pip install --upgrade pip`
- ✅ Install with: `pip install -r requirements.txt --user`

## 🎓 Use Cases

### For Students
- Get instant feedback on practice answers
- Practice viva questions with expert evaluation
- Identify and resolve common doubts
- Chat with AI tutor for personalized help
- Analyze past question papers for exam prep
- Test knowledge with auto-generated quizzes
- Create effective study plans for exam preparation

### For Educators
- Generate practice questions
- Evaluate student understanding
- Identify common misconceptions
- Provide additional learning resources

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test with Ollama running
5. Submit pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- **Streamlit** for the amazing web framework
- **Ollama** for local LLM accessibility
- **Meta** for Llama models
- **PyPDF** for PDF processing

---

**Made with ❤️ for students worldwide**

Happy studying! 🎓

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

## 📖 How to Use

### Using Mistake Explainer
1. Go to the **Mistake Explainer** tab
2. Paste the exam question in the first text area
3. Write your answer in the second text area
4. Click "Analyze Answer"
5. Review the detailed feedback, score, and study tips

### Using Viva Examiner
1. Go to the **Viva Examiner** tab
2. Select a subject from the dropdown
3. Click "Generate Question" to get a viva question
4. Type your answer in the provided text area
5. Click "Evaluate Answer" to get feedback
6. Click "Try Another Question" for more practice

### Using Doubt Predictor
1. Go to the **Doubt Predictor** tab
2. Enter a topic you want to study (e.g., "SQL Joins")
3. Click "Predict Doubts"
4. Review common doubts and exam mistakes for that topic

## 📁 Project Structure

```
ExamAI-Coach/
├── app.py              # Main Streamlit application
├── llm_helper.py       # Ollama API integration
├── prompts.py          # LLM prompt templates
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

### File Descriptions

- **app.py**: Main application with Streamlit UI, all three features, and error handling
- **llm_helper.py**: Helper module to communicate with Ollama API with error handling
- **prompts.py**: Prompt templates optimized for each feature
- **requirements.txt**: Python package dependencies

## ⚙️ Configuration

### Ollama Settings

The app connects to Ollama on `localhost:11434`. If you've configured Ollama on a different host/port, edit `llm_helper.py`:

```python
OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Change host/port if needed
MODEL_NAME = "llama3"  # Change model if needed
```

### Changing the LLM Model

To use a different Ollama model:

1. Pull the model: `ollama pull model_name`
2. Edit `llm_helper.py` and change `MODEL_NAME`

Popular models: `llama2`, `mistral`, `neural-chat`, `orca-mini`

## 🐛 Troubleshooting

### "Error: Ollama is not running"
- ✅ Make sure Ollama is running in a terminal with `ollama serve`
- ✅ Check that Ollama is accessible at `http://localhost:11434`
- ✅ On Windows/macOS, ensure Ollama desktop app is running

### "Model not found" error
- ✅ Pull the model: `ollama pull llama3`
- ✅ Wait for the download to complete (may take several minutes)

### Streamlit app not opening
- ✅ Make sure you ran `pip install -r requirements.txt`
- ✅ Try accessing manually: http://localhost:8501

### Slow responses
- ✅ This is normal on first use; llama3 generation takes time
- ✅ Ensure your system has adequate RAM (8GB minimum recommended)
- ✅ Close other heavy applications

### Dependencies installation fails
- ✅ Upgrade pip: `python -m pip install --upgrade pip`
- ✅ Try: `pip install streamlit requests --user`

## 🎓 Example Use Cases

### For Students
- Review exam papers and understand mistakes
- Practice viva questions from your courses
- Identify weak areas through doubt analysis
- Get personalized study tips

### For Teachers
- Generate practice questions for students
- Evaluate student understanding
- Identify common misconceptions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Ollama running
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Streamlit** for the amazing web app framework
- **Ollama** for making local LLMs accessible
- **Meta** for the Llama models

---

**Made with ❤️ for students worldwide**

Happy studying! 🎓