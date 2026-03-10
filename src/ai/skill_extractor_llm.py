import json
import os

from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_skills_llm(text: str) -> set:
    """
    Extract professional skills from a text using an LLM.

    Parameters
    ----------
    text : str
        Resume or job description text.

    Returns
    -------
    set
        A set of extracted skills in lowercase.
    """

    if not text:
        return set()

    prompt = f"""
Extract all professional skills mentioned in the following text.

Skills may include:
- technical skills
- programming languages
- frameworks
- databases
- software tools
- cloud platforms
- analytical methods
- industry tools
- professional competencies

Return ONLY valid JSON in this format:

{{
  "skills": []
}}

TEXT:
{text}
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert resume analyzer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        content = response.choices[0].message.content.strip()

        # Parse JSON response
        skills_data = json.loads(content)

        skills = set(skill.lower() for skill in skills_data.get("skills", []))

        return skills

    except Exception as error:

        print("LLM skill extraction failed:", error)

        return set()