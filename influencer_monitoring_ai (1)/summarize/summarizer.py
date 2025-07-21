import openai

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer  # You can also try LuhnSummarizer, LexRankSummarizer, etc.

def summarize_texts(texts, api_key=None):  # API key is now unused
    combined_text = "\n".join(texts)
    
    parser = PlaintextParser.from_string(combined_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    
    # Adjust the number of sentences in the summary (default: 5)
    summary_sentences = summarizer(parser.document, sentences_count=5)
    
    summary = " ".join(str(sentence) for sentence in summary_sentences)
    return summary

