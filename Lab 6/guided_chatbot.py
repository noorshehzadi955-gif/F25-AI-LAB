from lab6_search import Retriever

# FAQ data: each question has an answer and a source.
FAQ = [
    {
        "id": "faq:password",
        "question": "How do I reset my password?",
        "answer": "Use the recovery link on the login page.",
        "source": "it_help.txt"
    },
    {
        "id": "faq:submit",
        "question": "Where do I submit my assignment?",
        "answer": "Use the assignment upload page in the learning portal.",
        "source": "assessment.txt"
    },
    {
        "id": "faq:late",
        "question": "Can illness justify a late submission?",
        "answer": "Request an extension with medical evidence before the deadline.",
        "source": "handbook.txt"
    },
    # Two additional FAQs as required by Task 1
    {
        "id": "faq:email",
        "question": "How can I contact IT support?",
        "answer": "Send your issue to the university IT help desk.",
        "source": "it_help.txt"
    },
    {
        "id": "faq:portal",
        "question": "How do I log in to the student portal?",
        "answer": "Open the student portal and enter your university login details.",
        "source": "student_guide.txt"
    }
]


def build_bot():
    records = []

    for faq in FAQ:
        records.append({
            "id": faq["id"],
            "question": faq["question"],
            "answer": faq["answer"],
            "source": faq["source"],
            "text": faq["question"] + " " + faq["answer"]
        })

    return Retriever(records)


def reply(engine, query):
    if not query.strip():
        return "Please enter a question."

    # Give a direct answer only when the question exactly matches.
    for faq in FAQ:
        if query.strip().casefold() == faq["question"].casefold():
            return faq["answer"] + " [source: " + faq["source"] + "]"

    # Otherwise, show suggestions instead of guessing an answer.
    hits = engine.search(query, k=3)

    if not hits:
        return "No matching FAQ. Please contact the help desk."

    lines = ["Possible matches; type one of these exact questions:"]
    for record, score in hits:
        lines.append(record["question"] + f" (similarity {score:.3f})")

    return "\n".join(lines)


if __name__ == "__main__":
    engine = build_bot()

    print("FAQ Assistant")
    print("Type exit to stop.\n")

    while True:
        query = input("You: ")

        if query.strip().lower() == "exit":
            print("Bot: Goodbye!")
            break

        print("Bot:", reply(engine, query))
        print()
