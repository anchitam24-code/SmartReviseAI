import re
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["smartrevise"]
dataset = db["python_library"]


def generate_content(language, topic):
    language = (language or "General").strip()
    topic = (topic or "").strip()

    if not topic:
        notes = f"No specific topic provided for {language}. Please enter a topic to generate study notes."
        return {
            "language": language,
            "topic": topic,
            "notes": notes,
            "mcqs": [],
            "practice_questions": []
        }

    escaped_topic = re.escape(topic)
    result = dataset.find_one({
        "content": {"$regex": escaped_topic, "$options": "i"}
    })

    if result:
        notes = result["content"]
    else:
        notes = f"No dataset content found for {topic}"

    return {
        "language": language,
        "topic": topic,
        "notes": notes,
        "mcqs": [
            f"What is {topic} in {language}?",
            f"Explain {topic} with example."
        ],
        "practice_questions": [
            f"Write a program related to {topic}",
            f"Explain real use of {topic}"
        ]
    }