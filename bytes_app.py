import os
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

client = genai.Client()

class ByteSlide(BaseModel):
    slide_number: int
    subtopic_heading: str = Field(description="A clear, engaging title for this micro-learning block.")
    slide_text: str = Field(description="The instructional content strictly limited to approximately 50-70 words.")
    key_takeaway: str = Field(description="A single sentence, high-impact summary or actionable insight.")

class BytesModuleDeck(BaseModel):
    topic_title: str
    total_slides: int
    slides: list[ByteSlide]

def generate_bytes_deck(raw_source_material: str, target_topic: str) -> BytesModuleDeck:
    
    system_prompt = """
    You are an expert Instructional Designer and Micro-Learning Agent. Your job is to take raw, 
    dense technical text and chunk it into an organized series of sequential modular text slides.
    
    CRITICAL CONSTRAINTS:
    1. Each slide's 'slide_text' MUST be incredibly concise, hitting a strict target of roughly 50 to 70 words.
    2. Do not water down complex engineering concepts; instead, explain them with high density and clear language.
    3. Ensure the structural sequence flows logically from fundamental concepts to advanced applications.
    """
    
    user_prompt = f"TOPIC FOCUS: {target_topic}\n\nRAW SOURCE MATERIAL TO PROCESS:\n\"\"\"\n{raw_source_material}\n\"\"\""
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            response_mime_type="application/json",
            response_schema=BytesModuleDeck,
            temperature=0.4
        )
    )
    
    return response.parsed

if __name__ == "__main__":
    print("="*60)
    print(" Welcome to Bytes: The Dynamic Micro-Learning Engine")
    print("="*60)
    
    focus = input("Enter the specific topic focus (e.g., Database Indexing): ")
    source_file_path = input("Enter the name/path of your source text file (e.g., notes.txt): ")
    
    if not os.path.exists(source_file_path):
        print(f"\n❌ Error: Could not find a file named '{source_file_path}' in this folder.")
        print("Please create the file first and paste your study material inside it.")
    else:
        with open(source_file_path, "r", encoding="utf-8") as f:
            dense_academic_text = f.read()
            
        deck = generate_bytes_deck(dense_academic_text, focus)
        
        print("\n" + "="*60)
        print(f"📱 APP NAME: BYTES | COURSE: {deck.topic_title.upper()}")
        print("="*60)
        print(f"Generated {deck.total_slides} micro-learning slides successfully.\n")
        
        for slide in deck.slides:
            word_count = len(slide.slide_text.split())
            print(f"--- [Slide {slide.slide_number} / {deck.total_slides}]: {slide.subtopic_heading} ---")
            print(f"📄 Content ({word_count} words):\n{slide.slide_text}\n")
            print(f"💡 Takeaway: {slide.key_takeaway}")
            print("-" * 60)