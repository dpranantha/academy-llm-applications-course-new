# Building your first LLM Applications

In this series of exercises, you will build your own custom GPT Applications.

We have provided some skeleton code to help you get started, but you will need to complete and customise it.

Run the following prompt in the terminal to get started:

```bash
poetry run invoke chat-gpt-clone
```

## Exercise 1: Chat-GPT clone
The goal of this exercise is to create a clone of the Chat-GPT page.
By the end of this exercise, you should be able to chat with an AI assistant in your Streamlit app.

The code for this exercise is in the [pages/0_chat_gpt_clone.py](./pages/0_chat_gpt_clone.py) file.

Your tasks:
- Go to the Chat-GPT clone page by clicking on the sidebar.
- Interact with the page to see what functionality is already there.
- Explore the code.
    - How are the user/AI messages rendered?
    - What is stored in the session state?
    - How is the API called?
- Replace the hardcoded prompt with a configurable one from the sidebar.
- Replace the hardcoded temperature with a configurable one from the sidebar.
- Replace the hardcoded top_p with a configurable one from the sidebar.

### Reference
- https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps
- https://docs.streamlit.io/library/api-reference/widgets/st.text_area
- https://docs.streamlit.io/library/api-reference/widgets/st.slider
- https://docs.streamlit.io/library/api-reference/widgets/st.number_input
- https://docs.streamlit.io/library/api-reference/widgets/st.text_area
- https://docs.streamlit.io/library/api-reference/chat/st.chat_message


## Exercise 2: Summarizer-GPT
The goal of this exercise is to create a summarizer GPT.
By the end of this exercise, you should have an application that gives you a summarization of the user's input.

The code for this exercise is in the [pages/1_summarizer.py](./pages/1_summarizer.py) file.

Your tasks:
- Go to the Chat-GPT clone page by clicking on the sidebar.
- Interact with the page to see what functionality is already there.
- Explore the code. What components are there already?
- Write a prompt so the AI responds with a summary of the user input.

## Optional Exercise 3: Custom GPT
This is an open-ended exercise with no solution for the fast people.
It all is up to your imagination and creativity.

The goal of this exercise is to create your own custom GPT.
What it does is up to you!

This might be a good opportunity to change that one prompt you always use with Chat-GPT into a nice-looking application.

Feel free to use the code from the other pages as a starting point.
If you make something cool, please share screenshots with us.

The code for this exercise is in the [pages/02_custom_gpt.py](./pages/2_custom_gpt.py) file.

Some ideas from the internet:
- SEO Article Writer GPT
- Write critic GPT
- Personal Productivity Coach GPT
- Grammar Checker GPT
- Code Reviewer GPT
- Code translator GPT (e.g. Python to JavaScript)
- etc.

- BONUS: Add some guardrails to prevent your custom GPT bot from going off-topic and to moderate the content it produces.