from config import GROQ_API_KEY
from groq import Groq

client= Groq(
    api_key=GROQ_API_KEY
)

def llm_refinement(context, question):

    prompt=f'''
    Answer the question using ONLY the context provided. 
    Answer that you don't know if you can't find relevant answer in provided context.
    Attach the source name,ONLY if you can find any with the given context
    
    question: {question}

    context: {context}

    '''
    response=client.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": f"{prompt}"
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    return response.choices[0].message.content


if __name__=="__main__":
    context='''Python is a high-level, interpreted programming language known for its remarkable readability and simple syntax, which makes it an excellent choice for beginners and experts alike.
    It supports multiple programming paradigms, including procedural, object-oriented, and functional programming, providing flexibility for diverse development needs.
    The language boasts an extensive standard library and a massive ecosystem of third-party packages, enabling developers to build complex applications with minimal code. 
    Python is the industry standard for data science, machine learning, and artificial intelligence, thanks to robust frameworks like NumPy, Pandas, and TensorFlow.
    Its dynamic typing and automatic memory management further streamline the development process, allowing for faster prototyping and iteration. 
    Beyond data tasks, it is widely used for web development, automation scripting, and system administration. A vibrant global community ensures continuous support, frequent updates, and a wealth of educational resources. 
    Because of its "batteries-included" philosophy, developers can solve complex problems efficiently without reinventing the wheel. 
    The cross-platform nature of Python allows code to run seamlessly on various operating systems, reinforcing its position as a truly versatile tool.
    Ultimately, Python's design philosophy prioritizes developer productivity, making it one of the most popular and influential languages in modern computing.'''

    question= "who created python"

    print(get_llm_response(context,question))
