import base64
class ProxyMiddleware(object):
# overwrite process request
    def process_request(self, request, spider):
    # Set the location of the proxy
    	# Hide my ass proxy
        request.meta['proxy'] = "http://183.207.228.122:80"
        # request.meta['proxy'] = "http://45.33.106.64:8123"