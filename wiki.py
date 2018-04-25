import wikipedia as wiki
def wikisearch(message):
    try:
        return str(wiki.summary(message))
    except Exception:
        return str("did you mean?\n")+str("\n".join(wiki.search(message)))


