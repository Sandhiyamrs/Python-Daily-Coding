from gensim.summarization import summarize

def summarize_text(text):
    try:
        return summarize(text)
    except:
        return "Summary could not be generated."
