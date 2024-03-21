from data_collection.git_collector import fetch_commits
from data_processing.processor import clean_text
from nlp.nlp_analysis import analyze_text_with_chat_gpt


def main():
    commits = fetch_commits()
    for commit in commits:
        cleaned_message = clean_text(commit["message"])
        explanation = analyze_text_with_chat_gpt(cleaned_message)
        print(f"Explanation for commit by {commit['author']}: {explanation}\n---\n")


if __name__ == "__main__":
    main()
