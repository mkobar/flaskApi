import requests
from flask import Blueprint, request
from searchApi.blueprints import mockdata

raw = Blueprint("raw", __name__, url_prefix="/raw")

verbose = 9  # all the debug prints

# headers to use in Get
headers_Get = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/62.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


@raw.route("/google", methods=["GET"])
def googleRaw():
    # from
    # https://automatetheboringstuff.com/chapter11/
    q = request.args.get("q")  # not requests
    mock = request.args.get("mock")  # not requests
    print("q = " + q)
    if mock:
        print("mock = " + mock)
    print("Googling...")  # display text while downloading the Google page

    if mock:
        if q == "kittens":
            # return(jsonify(mockdata.mockDataKittensHtml))
            return mockdata.mockDataKittensHtml
            # return (mockData)
        elif q == "cats":
            return mockdata.mockDataCatsHtml
        elif q == "cars":
            return mockdata.mockDataCarsHtml
        else:
            # return ('{"message": "mocked"}')
            return mockdata.mockDataHtml
    # if (mock == 0):
    if q == "500":
        # 503 Server Error: Service Unavailable for url:
        #   https://www.google.com/sorry/index?continue=
        #   https://www.google.com/search%3Fq%3Dblocked%26oq%3D
        #   blocked%26hl%3Den%26gl%3Dus%26sourceid%3D
        #   chrome%26ie%3DUTF-8&hl=en&
        #   q=EgQyTvRhGNG5mOIFIhkA8aeDS7SXjlGndA50dtMVc_Y3HaUq6drtMgFy
        # res = requests.get('https://google.com/search?q=internal%20error&q=EgQyTvRhGN&usasourc=chrome&ved=xUTF-8')
        res = requests.get(
            "https://www.google.com/sorry/index?continue="
            "https://www.google.com/search%3Fq%3Dblocked%26"
            "oq%3Dblocked%26hl%3Den%26gl%3Dus%26sourceid%3D"
            "chrome%26ie%3DUTF-8&hl=en"
        )
    elif q == "400":
        res = requests.get(
            "https://google.com/sorry?q=&oq=&hl=en&gl=us&sourceid=chrome&ie=UTF-8"
        )
    else:
        res = requests.get(
            "https://www.google.com/search?q="
            + q
            + "&oq="
            + q
            + "&hl=en&gl=us&sourceid=chrome&ie=UTF-8",
            headers=headers_Get,
        )
    # res.raise_for_status()  # not in production
    if (res.status_code >= 400) and (res.status_code < 500):
        """
        return('<html><head></head><body><h2>Client ERROR Returned '+str(res.status_code)+
          '</h2><p>'+res.text+'<br></body></html>')
        """
        print("Client ERROR Returned " + str(res.status_code))
        return res.text

    if (res.status_code >= 500) and (res.status_code < 600):
        """
        return('<html><head></head><body><h2>Server Error Returned '+str(res.status_code)+
          '</h2><p>'+res.text+'<br></body></html>')
        """
        print("Server ERROR Returned " + str(res.status_code))
        return res.text

    #   print some html reponse information
    if verbose > 0:
        print("status code = " + str(res.status_code))
        if "blocked" in res.text:
            print("we've been blocked")
            return '{"message": "ERROR: we have been BLOCKED"}'
        print(res.headers.get("content-type", "unknown"))

    return res.text  # show html page


@raw.route("/ddg")
def ddgRaw():
    return '{"message": "ERROR: not yet supported"}'


@raw.route("/bing")
def bingRaw():
    return '{"message": "ERROR: not yet supported"}'


@raw.route("/multi")
# multiple engines
def multipleEnginesRaw():
    return '{"message": "ERROR: not yet supported"}'
