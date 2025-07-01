import gradio as gr

class GradioUI:
    def __init__(self, agent):
        self.agent = agent

    def chat(self, message, history=None):
        if history is None:
            history = []
        try:
            output = self.agent.run(message)
            history.append((message, output))
            return "", history, history
        except Exception as e:
            error_message = f"Error: {str(e)}"
            history.append((message, error_message))
            return "", history, history

    def launch(self):
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot()
            msg = gr.Textbox(placeholder="Ask me anything...")
            clear = gr.Button("Clear")
            state = gr.State([])

            msg.submit(self.chat, [msg, state], [msg, state, chatbot])
            clear.click(lambda: [], None, chatbot)

        demo.launch()
