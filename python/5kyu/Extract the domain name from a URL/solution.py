def domain_name(url):
    domain=url.split("//")[-1].split("/")[0]
    domain = domain.split(".")
    if domain[0] != 'www':
        return domain[0]
    return domain[1]
