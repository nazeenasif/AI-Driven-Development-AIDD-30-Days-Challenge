# agent/agent_core.py
class AgentCore:
    def __init__(self):
        pass

    def process_pdf(self, file_path):
        """
        Orchestrates PDF processing, including summarization and quiz generation.
        """
        from agent.summarizer import summarize_pdf
        from agent.quiz_generator import generate_quiz

        summary = summarize_pdf(file_path)
        quiz = generate_quiz(file_path)
        return summary, quiz

# Define agent object
agent = AgentCore()
