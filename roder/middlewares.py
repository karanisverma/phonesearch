import base64
class ProxyMiddleware(object):
# overwrite process request
    def process_request(self, request, spider):
    # Set the location of the proxy
        # request.meta['proxy'] = "http://49.207.64.65:8080"
        request.meta['proxy'] = "http://183.207.228.122:80"