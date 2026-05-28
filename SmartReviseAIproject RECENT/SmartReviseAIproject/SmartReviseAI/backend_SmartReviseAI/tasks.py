from ml.logic import generate_content


def parse_language_and_topic(text):
    if not isinstance(text, str) or not text.strip():
        return "General", ""

    if ":" in text:
        language, topic = text.split(":", 1)
        return language.strip() or "General", topic.strip()

    return "General", text.strip()


def generate_revision(language=None, topic=None):
    if topic is None and isinstance(language, str) and ":" in language:
        language, topic = parse_language_and_topic(language)

    language = (language or "General").strip()
    topic = (topic or "").strip()

    return generate_content(language, topic)
