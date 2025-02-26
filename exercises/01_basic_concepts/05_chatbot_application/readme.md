# Building your first LLM Applications

In this series of exercises, you will build your own custom LLM Applications.

We have provided some skeleton code to help you get started, but you will need to complete and customise it.

Run the following prompt in the terminal to get started:

```bash
poetry run invoke chatbot
```

If you are completely stuck and need some inspiration, you can start the solution by running the following command in your terminal at the root of this exercise:

```bash
poetry run invoke house-description-writer --solution
```

However, try to solve the exercise yourself before looking at the solution.

## Exercise 1: Chatbot App
The goal of this exercise is to create a clone of the Chat-GPT page, i.e. your very own chatbot.

By the end of this exercise, you should be able to chat with an AI assistant in your Streamlit app.

The code for this exercise is in the [0X_chatbot_application/pages/0_chatbot.py](./pages/0_chatbot.py) file.

Your tasks:
- Go to the Chatbot page by clicking on the sidebar.
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


## Exercise 2: Summarizer App
The goal of this exercise is to create a summarizer application.

By the end of this exercise, you should have an application that gives you a summarization of the user's input.

The code for this exercise is in the [0X_chatbot_application/pages/1_summarizer.py](./pages/1_summarizer.py) file.

Your tasks:
- Go to the Summarizer page by clicking on the sidebar.
- Interact with the page to see what functionality is already there.
- Explore the code. What components are there already?
- Write a prompt so the AI responds with a summary of the user input.

## Optional Exercise 3: Custom LLM App
This is an open-ended exercise with no solution for the fast people.
It all is up to your imagination and creativity.

The goal of this exercise is to create your own custom LLM Application.
What it does is up to you!

This might be a good opportunity to change that one prompt you always use with Gemini or Chat-GPT into a nice-looking application.

Feel free to use the code from the other pages as a starting point.
If you make something cool, please share screenshots with us.

The code for this exercise is in the [0X_chatbot_application/pages/02_custom_llm_application.py](./pages/2_custom_llm_application.py) file.

Some ideas from the internet:
- SEO Article Writer LLM
- Write critic LLM
- Personal Productivity Coach LLM
- Grammar Checker LLM
- Code Reviewer LLM
- Code translator LLM (e.g. Python to JavaScript)
- etc.

- BONUS: Add some guardrails to prevent your custom LLM bot from going off-topic and to moderate the content it produces!