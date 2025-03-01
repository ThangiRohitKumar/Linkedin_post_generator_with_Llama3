# Linkedin_post_generator_with_Llama3
Developed a LinkedIn Post Generator using Llama 3, LangChain, Streamlit, and Groq, enhancing content creation for influencers.Implemented data collection and preprocessing techniques to extract and enrich metadata from influencer posts.

Key Steps in the Project:

Data Collection:

Manually collected previous posts from influencers and formats them into a JSON file. This data includes the post text and engagement metrics.
Pre-processing:

A preprocessing script is created to extract metadata from the posts using the Lama 3.2 model. This includes extracting tags, line counts, and languages, enriching the original JSON data.
Post Generation:

The enriched data is used to create a user interface (UI) with Streamlit, allowing users to select topics, lengths, and languages. When the "Generate" button is clicked, the tool generates a new post based on the selected criteria.
Technical Architecture:

The project is divided into two main stages:
Stage 1: Pre-processing the raw posts to extract metadata.
Stage 2: Generating new posts based on user input and the enriched data.
User Interface:

The UI is built using Streamlit, featuring dropdowns for topic selection, post length, and language. The user can generate a post that aligns with their selected parameters.
Integration with LLM:

The project integrates with the Groq cloud service to utilize the Llama 3 70b model for generating posts. The presenter demonstrates how to set up an API key and make calls to the model.
Prompt Engineering:

The importance of crafting effective prompts for the LLM to ensure the generated content matches the influencer's style. This includes using few-shot learning techniques to provide examples of desired outputs.
