class article_page(object):
    #selectors
    header = "//header"
    DTwitter = "api.twitter.com"
    DFacebook = "www.facebook.com"
    disclaimer = "/html/body/div[1]/div/div"
    disclaimerLink = "/html/body/div[1]/div/div/a"
    footer = "/html/body/footer/div[2]/div[1]/p[1]"
    facebook = "/html/body/main/div[3]/article/div[2]/a[1]"
    twitter = "/html/body/main/div[3]/article/div[2]/a[2]"
    zipcode = "/html/body/main/div[3]/article/div[5]/div/form/div[2]/div/div/input"
    zipNumber = "33126"
    matchbutton = "/html/body/main/div[3]/article/div[5]/div/form/div[2]/button"
    latestNewsFirst = "/html/body/main/div[3]/aside/nav[2]/a[1]"
    latestNewsLast = "/html/body/main/div[3]/aside/nav[2]/a[last()]"
    urlArticle = "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html"
    footerText = "ConsumerAffairs is not a government agency. Companies displayed may pay us to be Authorized or when you click a link, call a number or fill a form on our site. Our content is intended to be used for general information purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances and consult with your own investment, financial, tax and legal advisers."

    # initializes the class
    def __init__(self, wd):
        self.driver = wd



