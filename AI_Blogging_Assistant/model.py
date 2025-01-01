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

image_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "\"How Will Be 2025 with AI? A Glimpse into the Future\n2025 is shaping up to be a landmark year, largely thanks to the rapid advancements in Artificial Intelligence. We’re not just talking about science fiction anymore; AI is actively transforming how we live, work, and interact with the world. So, what can we realistically expect in 2025? Let’s explore.\n\nThe Rise of Everyday AI Tools\nForget clunky interfaces and complex commands. In 2025, expect to see AI tools seamlessly integrated into our daily lives. From personalized shopping experiences to intelligent home assistants that anticipate your needs, AI will become increasingly intuitive and user-friendly. We’ll likely interact with AI without even realizing it, making everyday tasks smoother and more efficient.\n\nOpen AI: The Foundation of Innovation\nOpenAI will undoubtedly continue to play a pivotal role in shaping the AI landscape. Expect to see their models powering even more applications, from creative tools for artists and writers to advanced data analysis solutions for businesses. The accessibility of OpenAI’s resources will likely democratize AI development, leading to a surge of innovative products and services.\n\nCloude AI: The Power of Context\nCloude AI’s strength lies in its ability to understand context and nuance, moving beyond basic task completion to offer genuinely intelligent and helpful responses. In 2025, Cloude AI is poised to become a go-to for tasks requiring deeper understanding and critical thinking, further blurring the lines between human and artificial intelligence. Expect to see its applications in customer service, education, and creative fields.\n\nGenerative AI: Unleashing Creativity\nGet ready for an explosion of creative content thanks to Generative AI. From AI-generated art and music to customized video content and personalized learning materials, expect the quality and availability of AI-produced creative outputs to skyrocket in 2025. This will empower creators of all kinds and potentially transform the entertainment and media landscape.\n\n2025: The Dawn of the AI-Empowered Era\n2025 isn’t just about new gadgets; it's about an AI-powered paradigm shift. The integration of AI into our lives will be more profound than ever, offering unprecedented opportunities for efficiency, innovation, and personal growth. Prepare to witness a world where AI isn’t just a tool, but an integral part of our existence.\" summerize this blog post and generate a prompt to generate an image using hugging face to add in to the above mention blog post. give me only the Image Prompt as output. image should be realisitc natural 3d",
      ],
    },
    {
      "role": "model",
      "parts": [
        "**Summary:**\n\nThis blog post predicts that 2025 will be a landmark year for AI, with seamless integration into daily life. Everyday AI tools will become intuitive and user-friendly. OpenAI's models will power more applications, democratizing AI development, while Cloude AI will excel in understanding context, impacting customer service, education, and creative fields. Generative AI will explode, leading to a surge in AI-produced creative content. Ultimately, 2025 is presented as the beginning of an AI-empowered era where AI becomes an integral part of our existence, boosting efficiency, innovation, and personal growth.\n\n**Image Prompt:**\n\nA photorealistic 3D rendering of a modern, bright, open-concept living room. A transparent holographic interface floats mid-air, displaying complex data visualizations and intuitive control panels. A person is interacting with the interface by hand gestures. In the background, intelligent devices are seamlessly integrated into the furniture and environment, all reflecting a subtle, futuristic glow. The scene should convey a sense of seamless integration of technology into everyday life. The overall color scheme should be bright and inviting, suggesting a comfortable and optimistic future.\n",
      ],
    },
  ]
)

# response = chat_session.send_message("INSERT_INPUT_HERE")

# print(response.text)