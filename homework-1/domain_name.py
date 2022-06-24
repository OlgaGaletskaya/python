def domain_name(url):
    if  url.startswith("http://") :
        url = url.replace("http://", "")
    elif  url.startswith("https://") : 
        url = url.replace("https://", "")
    if  url.startswith("www.") :
        url = url.replace("www.", "")
    domain= url.split(".")[0]
    return domain