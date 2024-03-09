 
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

GOOGLE_API_KEY = 'AIzaSyAlmpL5nMrAWkTC_-xTDBs1Uo_A2dv8TBM'

# Configure API key
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is medium blogs")
 
response_text = response.candidates[0].content.parts[0].text
print(response_text)