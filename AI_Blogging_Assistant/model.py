import os
from apikey import google_gemini_api_key
import google.generativeai as genai

genai.configure(api_key=google_gemini_api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "generate a comprehensive,engaging blog post relevant to the given title and keywords. the blog title is \"How to win 2025 with the help of AI\" and the Keywords are online earning, motivations,low of attraction, win 2025. The blog should be approximately 250 words in length, suitable for online audience. Makesure to use seo techniques and subheadings. Ensure the content is original, informative and maintain a consistent tone throughout.Generate only the content without any explanation.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## How to Win 2025 with the Help of AI\n\n**Ready to dominate 2025?** The future is now, and Artificial Intelligence is the game-changer. Forget outdated strategies; this is about harnessing AI to amplify your goals and unlock incredible opportunities. Let’s dive in!\n\n###  AI: Your Secret Weapon for Online Earning\n\nThinking about boosting your income? AI can be your personal assistant. From identifying profitable niches to automating content creation, AI tools can significantly reduce workload while maximizing your online earning potential. Explore AI-powered writing software, social media scheduling tools, and even e-commerce platforms that use AI to optimize sales. Imagine spending less time on tedious tasks and more time on what truly matters – growing your income.\n\n###  Fueling Your Motivations with AI Insights\n\nStaying motivated can be tough. AI can help! Track your progress, analyze your habits, and receive personalized recommendations to stay on track.  AI-powered apps can identify your peak performance times, suggest tailored learning paths, and even provide positive reinforcement. It's like having a 24/7 personal coach in your pocket.\n\n###  The Law of Attraction Meets AI Power\n\nCombine the power of positive thinking with AI’s analytical capabilities.  Use AI to visualize your goals, monitor your progress, and maintain a clear focus on your desired outcomes.  When you pair the law of attraction with AI driven action, you create a potent recipe for success.\n\n###  Seize the Opportunity: Win 2025 \n\n2025 is your year! By embracing AI, you’re not just keeping up with the times, you’re defining them.  Leverage its power for online earning, cultivate unshakable motivation, and align your actions with the law of attraction. Get started today, and prepare to not only win 2025, but thrive in it!\n",
      ],
    },
  ]
)

# response = chat_session.send_message("INSERT_INPUT_HERE")

# print(response.text)