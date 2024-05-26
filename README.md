# EmpowerMe - Financial Retirement Recommendation Engine

EmpowerMe is a recommendation tool designed to help individuals achieve a financially secure retirement. Using the Retrieval Augmented Generation (RAG) technique with LangChain and OpenAI's GPT-3.5-turbo model, EmpowerMe provides personalized retirement plan recommendations based on user profiles and relevant financial data.

## Features
- Personalized retirement plan recommendations
- Integration with OpenAI's GPT-3.5-turbo for natural language processing
- Retrieval Augmented Generation (RAG) using LangChain
- Secure and user-friendly interface for collecting and processing user data

## Prerequisites

You will need to install the required Python modules:
```
make install
```

## Web scrapper using JigsawStack API
Use the JigsawStack API to collect retirement plan data from various financial sites.
```
make scrape
```

## Query and Recommendation

Send a query to the LLM and get personalized retirement plan recommendations.
```
make send
```

References:
- LangChain
- OpenAI
- JigsawStack API