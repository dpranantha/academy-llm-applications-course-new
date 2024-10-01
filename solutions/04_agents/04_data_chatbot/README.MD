# PyData QA Bot with Retrieval-Augmented Generation capabilities
In this exercise, you will build a chatbot that can interact with a dataset.

Users will be able to upload a dataset and ask the bot simple questions about it. Under the hood, the LLM agent will then translate these queries into actionable Pandas code, which can be executed to produce a result. As the Agent will use a form of ReAct prompting, the bot should be able to explain to the user how it arrived at the answer to their question.

## What is provided
At the moment, the following functionality is implemented:
- A dataset is read-in
- A query for the dataset is set
- The agent answers the query and returns a result.

## What you need to do
You need to complete the functionality of the application.
You can do that by doing the following:
1. Start the application. Try it out and see what works and what does not work yet.
2. Read the code in the `[main.py](./main.py)` file and try to understand what is going on. Keep an eye out for the 'YOUR CODE HERE' comments in the code. These indicate the specific areas that need your attention.
3. Add a title to the applicaiton page.
4. Use the `st.expander` function to add an option to visualise the uploaded data.
5. Add some typical user queries to the list of questions.
6. Allow the user to specify their own query
7. Pass additional arguments to the `create_pandas_dataframe_agent` function to
    - enhance the verbosity of responses and
    - allow for error handling.
8. Show the agent's working:
    1. Pass an additional argument to the `create_pandas_dataframe_agent` function to enable the model to return the intermediate steps.
    2. Add an option to visualize these steps.
9. Play around with the hyperparameters of the model. What is the effect on the agent output?
10. Feel free to add additional features to the application as you see fit.

After adding a new feature, make sure you play around with the application to see if it works as expected.
For example:
- Do the example queries return the correct result? What about it you provide your own?
- What happens if you replace the dataset?
- What happens if you ask a new query?
- What happens when you ask it to to return five rows of data? What happens if you increase this number?
- Is there a pattern to the queries the agent cannot answer?

## How to run the application
To run the application, you need to do the following commands in the terminal with your virtual environment activated:

```bash
poetry run invoke data-chatbot
```

If you are completely stuck and need some inspiration, you can start the solution by running the following command in your terminal at the root of this exercise:

```bash
poetry run invoke  data-chatbot --solution
```

However, try to solve the exercise yourself before looking at the solution.
