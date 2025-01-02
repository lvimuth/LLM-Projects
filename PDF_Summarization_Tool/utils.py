from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatGemini  # Use Gemini Chat model
from langchain.callbacks import get_gemini_callback  # Replace OpenAI callback
from pypdf import PdfReader

def process_text(text):
    # Splitting text into chunks
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # Using HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    
    # Creating a FAISS-based knowledge base
    knowledgeBase = FAISS.from_texts(chunks, embeddings)
    
    return knowledgeBase

def summerizer(pdf):
    if pdf is not None:
        # Read the PDF content
        pdf_reader = PdfReader(pdf)
        text = ''
        
        for page in pdf_reader.pages:
            text += page.extract_text() or ''
            
        # Process text into knowledge base
        knowledgeBase = process_text(text)
        
        print('knowledgeBase', knowledgeBase)
        
        # Define the query
        query = 'Summarize the content of the uploaded PDF file in approximately 3-5 sentences.'
        
        if query:
            # Perform similarity search
            docs = knowledgeBase.similarity_search(query)
            
            # Use Gemini Chat Model
            GeminiModel = 'gemini-chat-model'  # Replace with the specific Gemini model name
            llm = ChatGemini(model=GeminiModel, temperature=0.1)  # Initialize Gemini LLM
            
            chain = load_qa_chain(llm, chain_type='stuff')
            
            # Optionally monitor API usage
            # with get_gemini_callback() as cost:
            response = chain.run(input_documents=docs, question=query)
            # print(cost)
            
            return response
