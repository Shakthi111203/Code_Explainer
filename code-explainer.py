import google.generativeai as palm
import os

palm.configure(api_key =('AIzaSyDJdgLkJ1KJAHZqlk3WLbEV739xybREtUk'))

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

import gradio as gr
import os
import google.generativeai as palm

palm.configure(api_key="AIzaSyDJdgLkJ1KJAHZqlk3WLbEV739xybREtUk")

def get_completion(code_snippet):

  prompt = f"""
  Your task is to act as a Python Code Explainer.
  I'll give you a Code Snippet.
  Your job is to explain the Code Snippet step-by-step.
  Break down the code into as many steps as possible.
  Share intermediate checkpoints & steps along with results.
  Code Snippet is shared below, delimited with triple backticks:
  ```
  {code_snippet}
  ```
  """

  completion = palm.generate_text(
      model=model,
      prompt=prompt,
      temperature=0,
      max_output_tokens=500,
      )
  response = completion.result
  return response

iface = gr.Interface(fn=get_completion, inputs=[gr.Textbox(label="Insert Code Here",lines=5)],
                    outputs=[gr.Textbox(label="Explanation Here",lines=5)],
                    title="Python Code Explainer"
                    )

iface.launch(share=True)

iface.close()