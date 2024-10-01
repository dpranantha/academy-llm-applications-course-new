# PyData QA Bot with Retrieval-Augmented Generation capabilities
In this exercise, you will build a PyData QA Bot with Retrieval-Augmented Generation capabilities.

Users will be able to chat with the bot and ask it questions. They will also be able to ask the bot to search the knowledge base it has access to, which contains information about the talks at the conference. To do this, users simply need to click a checkbox, then after the user submits their query, the bot will retrieve the _k_ most relevant documents from the vector database. Then, the query and the search results will be given to the LLM model, allowing it to generate an answer.


## What is provided
At the moment, the following functionality is implemented:
- The user can send a message to the LLM, and the LLM will generate a response.
- The application keeps track of the conversation history and renders it in the UI.
- The user can press the `Re-index` button to re-index the vector database. Currently, this only indexes the title of the talks. A lot more information is available in the knowledge base that still needs to be indexed.
- The user can click the checkbox, which will then trigger the search functionality. The search results will be sent to the LLN model, allowing it to generate an answer. However, not all the needed information is being added to the prompt yet. This is something you will need to implement.

## What you need to do
You need to complete the functionality of the application.
You can do that by doing the following:
1. Start the application. Try it out and see what works and what does not work yet.
2. Read the code and try to understand what is going on. Keep an eye out for the 'YOUR CODE HERE' comments in the code. These indicate the specific areas that need your attention.
3. Finish the `build_db` function in the `[main.py](./main.py)` file. To do this, you will need to:
    1. add metadata to each item in the vector database and,
    2. index additional fields such as the description and abstract of the talk.
4. Finish the `format_search_result` function in the `[main.py](./main.py)` file. This function should format the search results in a way that they can be used as input for the LLM model. Check out all the available metadata in the `build_db` function and think about which of these fields you want to use in the search results.
5. Give the LLM a system prompt that gives it more general information about the PyData conference and its tasks.
6. Allow the user to specify hyperparameters of the LLM, such as the `temperature` and `top_p` parameters.
5. Improve the prompt in the `format_search_instruction` function in the `[main.py](./main.py)` file. It works, but it can do a lot better.
6. Play around with the indexing hyperparameters of the chunk sizes and see if you can get better results.
7. Feel free to add additional features to the application as you see fit.

After adding a new feature, make sure you play around with the application to see if it works as expected.
For example, ask it questions such as:
- Which talks are about NLP?
- Which talk are about data visualization?
- When is the talk about LLM agents? And in which room is it?
- etc.

## How to run the application
To run the application, you need to do the following commands in the terminal with your virtual environment activated:

```bash
poetry run invoke pydata-qa-bot
```

If you are completely stuck and need some inspiration, you can start the solution by running the following command in your terminal at the root of this exercise:

```bash
poetry run invoke pydata-qa-bot --solution
```

However, try to solve the exercise yourself before looking at the solution.
