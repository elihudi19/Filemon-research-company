class SiteLanguageMiddleware:
    """
    Inasoma ?lang=en au ?lang=sw kutoka URL, inaihifadhi kwenye session,
    na kuiweka kwenye request.LANG ili templates zote ziweze kuitumia.
    Chaguo-msingi ni Kiingereza ('en').
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        requested_lang = request.GET.get("lang")
        if requested_lang in ("en", "sw"):
            request.session["site_lang"] = requested_lang

        request.LANG = request.session.get("site_lang", "en")
        return self.get_response(request)
