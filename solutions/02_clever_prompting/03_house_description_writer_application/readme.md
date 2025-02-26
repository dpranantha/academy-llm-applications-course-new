# House description writer application
During the previous exercise, we noticed that many of the house descriptions written by humans were actually very bad.

After some market research, we found that real estate agents do not like writing these descriptions. They prefer to spend their time on other tasks, such as finding new clients and showing houses. So, we decided to build an application that automatically generates house descriptions based on a pre-defined list of attributes, which repressent house features.

The agents are a bit worried that the generated descriptions might not be accurate, so we also want to automatically validate them, to ensure they contain the correct attributes.

We have already built a prototype of the application, but it is not yet finished. There is a basic user interface that allows users to input attributes like:
- Rent.
- City.
- Apartment type.

If the user presses the submit button, the application generates some text based on the user inputs and shows some information about the generated text. However, a lot of additional work is needed to make the application fully functional and that is where you come in!

It is your job to complete the application by doing the following:

1. Expand the house features: Incorporate additional attributes like neighborhood, number of rooms, number of bathrooms, and whatever else you think is relevant.
2. Develop system prompts: Write clear instructions to guide the language model into generating high-quality listing descriptions, which contain the relevant attributes and use the correct tone of voice.
3. Validating the response:
    - Check that the attributes extracted from the generated description corresponds to the JSON schema (using JSON mode does not guarantee the output matches any specific schema, only that it is a valid JSON and can be parsed without errors).
    - Remember that for each additional attribute you add, you should also add a validation function that checks if the generated text contains the attribute or not.

You can find the code for the application in the `[main.py](./main.py)` file.

Look for the 'YOUR CODE HERE' comments in the code to identify the specific areas that need your attention.

You can start the application by running the following command in your terminal at the root of this exercise:

```bash
uv run invoke house-description-writer
```

If you are completely stuck and need some inspiration, you can start the solution by running the following command in your terminal at the root of this exercise:

```bash
uv run invoke house-description-writer --solution
```

However, try to solve the exercise yourself before looking at the solution.