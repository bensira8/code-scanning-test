import gradio as gr


def fn(text):
        html = ("<div>" + text + "</div>")
        return html


demo = gr.Interface(
            fn,
                inputs="text", outputs="html"
                )

demo.launch()
